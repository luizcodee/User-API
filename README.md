# API de Usuários - Projeto UNIFECAF

## Integrantes do Grupo
- Adriel Pereira Luis Monteiro (RA: 78944)
- Emily de Souza (RA: 104584)
- Joice Barbosa Santos (RA: 102859)
- Luiz Henrique de Almeida Santos (RA: 88078)
- Matheus Bondezan de Souza (RA: 96122)

## Professor
Rodrigo Moreira

## Tema
**API de Usuários**

## Descrição do Sistema
Esta API permite o cadastro, consulta, atualização e exclusão de usuários. O objetivo é facilitar o gerenciamento de usuários de forma centralizada, segura e automatizada, podendo ser utilizada por sistemas integrados (aplicativos, sites, etc) ou usuários finais.

## Funcionalidades Principais
- Cadastro de usuário (POST)
- Consulta de usuários (GET - listar todos ou buscar por ID)
- Atualização de dados do usuário (PUT)
- Exclusão de usuário (DELETE)
- Validação de dados (e-mail válido, senha segura)

## Tecnologias Utilizadas
- **Python**: linguagem principal
- **FastAPI**: framework para criação da API
- **SQLite**: banco de dados simples para armazenar usuários
- **Pydantic**: validação de dados
- **Uvicorn**: servidor ASGI para rodar a API
- **Postman**: ferramenta para testar as requisições
- **Git/GitHub**: controle de versão

## Instalação e Execução
1. Clone o repositório ou baixe os arquivos.
2. Instale as dependências:
   ```bash
   pip install fastapi uvicorn pydantic
   ```
3. Execute a API:
   ```bash
   uvicorn main:app --reload
   ```
4. Acesse a documentação automática em: [http://localhost:8000/docs](http://localhost:8000/docs)

## Estrutura do Projeto
- `main.py`: arquivo principal com toda a lógica da API
- `usuarios.db`: banco de dados SQLite gerado automaticamente

## Endpoints da API

### 1. Cadastro de Usuário
- **POST** `/usuarios`
- **Body Exemplo:**
  ```json
  {
    "nome": "João Silva",
    "email": "joao@email.com",
    "senha": "senha123"
  }
  ```
- **Validações:**
  - E-mail deve ser válido
  - Senha deve ter pelo menos 6 caracteres
  - E-mail não pode ser duplicado

### 2. Listar Todos os Usuários
- **GET** `/usuarios`
- **Resposta:** Lista de usuários cadastrados

### 3. Buscar Usuário por ID
- **GET** `/usuarios/{id}`
- **Resposta:** Dados do usuário ou erro se não encontrado

### 4. Atualizar Usuário
- **PUT** `/usuarios/{id}`
- **Body Exemplo:**
  ```json
  {
    "nome": "João Silva",
    "email": "joao@email.com",
    "senha": "novaSenha123"
  }
  ```
- **Validações:** Iguais ao cadastro

### 5. Excluir Usuário
- **DELETE** `/usuarios/{id}`
- **Resposta:** Mensagem de sucesso ou erro se não encontrado

## Cenários de Teste
1. **Cadastro de usuário:**
   - Testar cadastro com dados válidos e inválidos
   - Testar cadastro com e-mail já existente
2. **Consulta de usuários:**
   - Listar todos
   - Buscar por ID existente e inexistente
3. **Atualização de dados:**
   - Atualizar usuário existente
   - Tentar atualizar usuário inexistente
   - Testar validações
4. **Exclusão de usuário:**
   - Excluir usuário existente
   - Tentar excluir usuário inexistente
5. **Validação de dados:**
   - E-mail inválido
   - Senha curta
   - Campos obrigatórios vazios

## Organização do Grupo
- **Desenvolvimento:** Todos
- **Testes:** Emily
- **Documentação:** Joice
- **Apresentação:** Luiz

## Observações
- O banco de dados é criado automaticamente ao rodar a API.
- Utilize o Postman ou a documentação Swagger para testar as rotas.
- Para dúvidas ou melhorias, entre em contato com o grupo.

