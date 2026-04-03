from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, validator
import sqlite3

app = FastAPI()

# Modelo de dados do usuário
class User(BaseModel):
    id: int | None = None
    nome: str
    email: EmailStr
    senha: str

    @validator('senha')
    def senha_segura(cls, v):
        if len(v) < 6:
            raise ValueError('A senha deve ter pelo menos 6 caracteres')
        return v

def get_db():
    conn = sqlite3.connect('usuarios.db')
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

criar_tabela()

@app.post('/usuarios', response_model=User)
def criar_usuario(user: User):
    conn = get_db()
    try:
        cur = conn.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)',
                           (user.nome, user.email, user.senha))
        conn.commit()
        user.id = cur.lastrowid
        return user
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail='E-mail já cadastrado')
    finally:
        conn.close()

@app.get('/usuarios', response_model=list[User])
def listar_usuarios():
    conn = get_db()
    cur = conn.execute('SELECT * FROM usuarios')
    usuarios = [User(**dict(row)) for row in cur.fetchall()]
    conn.close()
    return usuarios

@app.get('/usuarios/{user_id}', response_model=User)
def buscar_usuario(user_id: int):
    conn = get_db()
    cur = conn.execute('SELECT * FROM usuarios WHERE id = ?', (user_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return User(**dict(row))
    raise HTTPException(status_code=404, detail='Usuário não encontrado')

@app.put('/usuarios/{user_id}', response_model=User)
def atualizar_usuario(user_id: int, user: User):
    conn = get_db()
    cur = conn.execute('SELECT * FROM usuarios WHERE id = ?', (user_id,))
    if not cur.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    try:
        conn.execute('UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?',
                     (user.nome, user.email, user.senha, user_id))
        conn.commit()
        user.id = user_id
        return user
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail='E-mail já cadastrado')
    finally:
        conn.close()

@app.delete('/usuarios/{user_id}')
def deletar_usuario(user_id: int):
    conn = get_db()
    cur = conn.execute('SELECT * FROM usuarios WHERE id = ?', (user_id,))
    if not cur.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    conn.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return {'mensagem': 'Usuário excluído com sucesso'}

