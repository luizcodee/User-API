<<<<<<< HEAD
# 🧪 QA – Testes de API de Usuários

Projeto desenvolvido para a disciplina de Quality Assurance, com foco na validação de uma API de gerenciamento de usuários.

---

## 🎯 Objetivo

Garantir a qualidade da API validando as principais funcionalidades:

* Cadastro de usuários
* Listagem de usuários
* Busca por ID
* Atualização de dados
* Exclusão de usuários

---

## 🔗 API utilizada

Projeto original desenvolvido por Luiz:
https://github.com/luizcodee/User-API

---

## 👩‍💻 Meu papel no projeto

* Criação de casos de teste
* Execução de testes manuais (Postman)
* Validação de regras de negócio
* Documentação dos testes
* Identificação e registro de bugs

---

## 🧪 Tipos de testes realizados

### ✔ Testes funcionais

* Cadastro
* Listagem
* Busca por ID
* Atualização
* Exclusão

### ❌ Testes de validação

* Email inválido
* Senha curta
* ID inexistente

---

## 🐞 Bugs identificados

* Cadastro permitido com nome vazio
* Inconsistência na validação de senha

📄 Mais detalhes em:
docs/relatorio-bugs.md

---

## 📸 Evidências

As evidências dos testes estão disponíveis em:

📁 docs/evidencias/

---

## 🧾 Casos de teste

Documentação completa disponível em:

📄 docs/casos-de-teste.md

---

## ⚙️ Testes automatizados

Testes automatizados implementados com:

* Python
* Pytest
* HTTPX

📁 Local:
tests/test_api.py

---

## 🧪 Testes no Postman

Collection disponível em:

📁 postman/collection.json

---

## 📁 Estrutura do projeto

```
qa-user-api-tests/
 ├── docs/
 │    ├── casos-de-teste.md
 │    ├── evidencias.md
 │    ├── relatorio-bugs.md
 │    └── evidencias/
 │
 ├── tests/
 │    └── ac3_testes.py
 │    └── test_api.py
 │
 ├── postman/
 │    └── collection.json
 │
 └── README.md
```

---

## 👩‍💻 Autora

Joice Barbosa

---

=======
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
- `test_main.py`: testes automatizados dos endpoints

## Testes Automatizados (Quality Assurance)

O projeto inclui testes automatizados para garantir a qualidade e o correto funcionamento da API, cobrindo os seguintes cenários:
- Cadastro de usuário
- Consulta de usuários (listar todos e buscar por ID)
- Atualização de dados do usuário
- Exclusão de usuário
- Validação de dados (e-mail e senha)

### Ferramentas utilizadas para testes
- **pytest**: framework de testes
- **httpx**: cliente HTTP assíncrono para testar endpoints

### Instalação das dependências de teste
```bash
pip install pytest httpx
```

### Como rodar os testes
```bash
pytest
```

Os testes estão no arquivo `test_main.py` e cobrem todos os cenários exigidos pela atividade.

### Testes manuais
Você pode testar manualmente usando o Postman ou a interface Swagger UI disponível em [http://localhost:8000/docs](http://localhost:8000/docs).

## Organização do Grupo
- Desenvolvimento: Todos
- Testes: Emily
- Documentação: Joice
- Apresentação: Luiz

---
Projeto desenvolvido para a disciplina de Engenharia de Software - UNIFECAF
>>>>>>> 074a0ae383c97142d450c19f086e325aa08b9e71
