# AC3 – Atividade Hands-On de Quality Assurance
**Grupo:** Projeto Final – API de Usuários  
**Professor:** Rodrigo Moreira  
**Instituição:** UNIFECAF  

**Integrantes:**
- Adriel Pereira Luis Monteiro (RA: 78944) – Execução do sistema
- Emily de Souza (RA: 104584) – Execução dos testes
- Joice Barbosa Santos (RA: 102859) – Documentação
- Luiz Henrique de Almeida Santos (RA: 88078) – Coleta de evidências
- Matheus Bondezan de Souza (RA: 96122) – Análise de bugs e melhorias

---

## PASSO 1 – Descrição do Sistema

**Nome do sistema:** API de Usuários

**Objetivo:** Gerenciar usuários de forma centralizada, segura e automatizada via API REST.

**O que o sistema faz:**
- Permite cadastrar, consultar, atualizar e excluir usuários
- Valida os dados recebidos (formato de e-mail e tamanho mínimo de senha)
- Armazena os dados em banco SQLite

**Como funciona (fluxo resumido):**
1. O cliente envia uma requisição HTTP (POST, GET, PUT, DELETE) para os endpoints da API
2. A API valida os dados com Pydantic
3. A operação é executada no banco de dados SQLite
4. A API retorna a resposta com os dados ou mensagem de erro correspondente

---

## PASSO 2 – Escopo dos Testes

**O que será testado:**
- Todos os endpoints da API: POST /usuarios, GET /usuarios, GET /usuarios/{id}, PUT /usuarios/{id}, DELETE /usuarios/{id}

**Partes do sistema validadas:**
- Cadastro de usuário
- Listagem de usuários
- Busca por ID
- Atualização de dados
- Exclusão de usuário
- Validação de e-mail e senha

**Tipos de teste aplicados:**
- Teste funcional (fluxo completo de cada operação)
- Teste de API (validação de status code e resposta JSON)
- Validação de dados (entradas inválidas)
- Testes com erro proposital (campos vazios, dados incorretos)

---

## PASSO 3 – Casos de Teste

| ID | Nome | Objetivo | Entrada | Passos | Resultado Esperado |
|----|------|----------|---------|--------|--------------------|
| CT01 | Cadastro de usuário válido | Verificar se o cadastro funciona com dados corretos | nome, email válido, senha com 6+ caracteres | POST /usuarios com JSON válido | Status 200, retorna usuário com ID |
| CT02 | Listar todos os usuários | Verificar se a listagem retorna todos os cadastros | Nenhuma | GET /usuarios | Status 200, retorna lista (array JSON) |
| CT03 | Buscar usuário por ID | Verificar se a busca por ID retorna o usuário correto | ID de usuário existente | GET /usuarios/{id} | Status 200, retorna dados do usuário |
| CT04 | Atualizar dados do usuário | Verificar se a atualização altera os dados corretamente | ID existente + novos dados válidos | PUT /usuarios/{id} com JSON atualizado | Status 200, retorna usuário com dados atualizados |
| CT05 | Excluir usuário | Verificar se a exclusão remove o usuário corretamente | ID de usuário existente | DELETE /usuarios/{id} | Status 200, mensagem de confirmação |
| CT06 | Buscar usuário com ID inexistente | Verificar o comportamento com ID que não existe | ID inválido (ex: 9999) | GET /usuarios/9999 | Status 404, mensagem de erro |
| CT07 | Cadastro com e-mail inválido | Verificar rejeição de e-mail fora do formato padrão | email: "emailinvalido" | POST /usuarios com email sem @ | Status 422, erro de validação |
| CT08 | Cadastro com senha curta | Verificar rejeição de senha com menos de 6 caracteres | senha: "123" | POST /usuarios com senha curta | Status 422 ou 400, erro de validação |

---

## PASSO 4 – Execução dos Testes

| ID | Resultado | Comportamento Observado | Compatível com Esperado? |
|----|-----------|------------------------|--------------------------|
| CT01 | ✅ Passou | Retornou status 200 e o objeto do usuário com ID gerado | Sim |
| CT02 | ✅ Passou | Retornou status 200 e array com os usuários cadastrados | Sim |
| CT03 | ✅ Passou | Retornou status 200 e os dados do usuário pelo ID informado | Sim |
| CT04 | ✅ Passou | Retornou status 200 e os dados atualizados do usuário | Sim |
| CT05 | ✅ Passou | Retornou status 200 e mensagem "Usuário excluído com sucesso" | Sim |
| CT06 | ✅ Passou | Retornou status 404 e "Usuário não encontrado" | Sim |
| CT07 | ✅ Passou | Retornou status 422 com detalhes do erro de validação do Pydantic | Sim |
| CT08 | ⚠️ Parcial | Retorna 422 pelo Pydantic, mas o código trata como podendo ser 400 também | Parcialmente – inconsistência identificada |

**Como executar os testes automatizados:**
```bash
pytest test_main.py -v
```

**Como executar os testes da AC3:**
```bash
# Inicie a API primeiro
uvicorn main:app --reload

# Em outro terminal
python ac3_testes.py
```

> **Evidência:** Tirar print do terminal após rodar `pytest test_main.py -v` e `python ac3_testes.py`

---

## PASSO 5 – Registro de Evidências

Evidências a serem coletadas:

1. **Print do terminal** – resultado do comando `pytest test_main.py -v` mostrando todos os testes passando
2. **Print do terminal** – resultado do `python ac3_testes.py` mostrando os testes automatizados
3. **Print do Swagger UI** – acesse `http://localhost:8000/docs` e tire print da interface com os endpoints
4. **Print do Postman** – requisição POST /usuarios com dados válidos (status 200)
5. **Print do Postman** – requisição POST /usuarios com email inválido (status 422)
6. **Print do Postman** – requisição GET /usuarios/9999 com ID inexistente (status 404)

> **Instrução:** Inserir os prints aqui no documento após a execução.

---

## PASSO 6 – Testes com Erro Proposital

| Entrada Inválida | Endpoint | Comportamento Observado | Status Retornado |
|-----------------|----------|------------------------|-----------------|
| Campo `nome` vazio (`""`) | POST /usuarios | Pydantic aceita string vazia — não rejeita | 200 (comportamento inesperado) |
| Email sem `@` (`"emailinvalido"`) | POST /usuarios | Pydantic rejeita com mensagem de erro | 422 |
| Senha com 3 caracteres (`"123"`) | POST /usuarios | Validator rejeita com "A senha deve ter pelo menos 6 caracteres" | 422 |
| ID inexistente (`9999`) | GET /usuarios/9999 | API retorna mensagem "Usuário não encontrado" | 404 |
| Body vazio (`{}`) | POST /usuarios | Pydantic exige os campos obrigatórios | 422 |
| Tipo incorreto no ID (`"abc"`) | GET /usuarios/abc | FastAPI rejeita por tipo inválido | 422 |

> **Evidência:** Tirar prints de cada requisição no Postman ou no terminal.

---

## PASSO 7 – Testes de API

### Testes Válidos

**Teste válido 1 – Cadastro de usuário**
- Método: POST
- Endpoint: `/usuarios`
- Body:
```json
{
  "nome": "Usuário Teste",
  "email": "teste@exemplo.com",
  "senha": "123456"
}
```
- Status esperado: `200`
- Resposta esperada: objeto com `id`, `nome`, `email`, `senha`

---

**Teste válido 2 – Listar usuários**
- Método: GET
- Endpoint: `/usuarios`
- Status esperado: `200`
- Resposta esperada: array JSON com os usuários cadastrados

---

### Testes Inválidos

**Teste inválido 1 – Email inválido**
- Método: POST
- Endpoint: `/usuarios`
- Body:
```json
{
  "nome": "Inválido",
  "email": "emailinvalido",
  "senha": "123456"
}
```
- Status esperado: `422`
- Resposta esperada: erro de validação do campo email

---

**Teste inválido 2 – ID inexistente**
- Método: GET
- Endpoint: `/usuarios/9999`
- Status esperado: `404`
- Resposta esperada: `{"detail": "Usuário não encontrado"}`

---

> **Evidência:** Tirar prints das 4 requisições no Postman mostrando status code e resposta.

---

## PASSO 8 – Automação de Testes

Os testes automatizados estão no arquivo `ac3_testes.py`.

Utiliza a biblioteca `requests` conforme solicitado na atividade.  
Requer a API rodando localmente: `uvicorn main:app --reload`

**Como executar:**
```bash
python ac3_testes.py
```

> Ver arquivo `ac3_testes.py` para o código completo.

---

## PASSO 9 – Identificação de Bugs

### Bug 1 – Campo `nome` vazio é aceito sem validação

**Título:** API aceita cadastro com nome vazio  
**Descrição:** O campo `nome` aceita string vazia `""` sem retornar erro, pois o Pydantic não valida tamanho mínimo de string por padrão.  
**Como reproduzir:**
```json
POST /usuarios
{
  "nome": "",
  "email": "teste@exemplo.com",
  "senha": "123456"
}
```
**Comportamento atual:** Retorna status 200 e cadastra o usuário com nome vazio  
**Comportamento esperado:** Retornar status 422 com mensagem de erro  
**Impacto:** Permite cadastro de usuários com dados incompletos, comprometendo a integridade dos dados  
**Sugestão de correção:** Adicionar validação `min_length=1` no campo `nome` do modelo Pydantic:
```python
nome: str = Field(min_length=1)
```

---

### Bug 2 – Código de status inconsistente para senha curta

**Título:** Validação de senha retorna 422 ou 400 de forma inconsistente  
**Descrição:** O teste `test_validacao_senha_curta` aceita tanto `422` quanto `400` como resposta válida (`assert resp.status_code == 422 or resp.status_code == 400`), indicando que o comportamento não é padronizado.  
**Como reproduzir:**
```json
POST /usuarios
{
  "nome": "Teste",
  "email": "teste@exemplo.com",
  "senha": "123"
}
```
**Comportamento atual:** Pode retornar 422 (Pydantic) ou 400 (HTTPException) dependendo do fluxo  
**Comportamento esperado:** Sempre retornar 422 para erros de validação de entrada  
**Impacto:** Dificulta o tratamento de erros no lado do cliente (frontend/app integrado)  
**Sugestão de correção:** Remover a condição dupla no teste e garantir que a validação sempre passe pelo Pydantic (status 422), sem tratamento manual como HTTPException para esse caso.

---

## PASSO 10 – Sugestões de Melhoria

### Melhoria Técnica 1 – Validação de nome vazio
Adicionar `Field(min_length=1)` no campo `nome` para garantir que não sejam cadastrados usuários com nome em branco. Isso resolve o Bug 1 identificado.

### Melhoria Técnica 2 – Padronizar erros de validação
Unificar todos os erros de validação de entrada para retornar sempre status `422`, removendo o uso de `HTTPException(status_code=400)` para casos que já são tratados pelo Pydantic. Isso torna a API mais previsível para quem a consome.

### Melhoria Geral – Documentar os erros possíveis no Swagger
Adicionar `responses` nos decoradores dos endpoints para documentar os possíveis erros (400, 404, 422) diretamente na interface do Swagger UI (`/docs`). Isso facilita o entendimento da API por outros desenvolvedores e testadores.

---

## PASSO 11 – Revisão Final

| Item obrigatório | Status |
|-----------------|--------|
| Descrição do sistema | ✅ |
| Escopo dos testes | ✅ |
| 5 casos de teste (mínimo) | ✅ (8 casos) |
| Execução registrada | ✅ |
| Evidências (prints) | ⚠️ Pendente – inserir prints após execução |
| Testes com erro proposital | ✅ |
| Testes de API (2 válidos + 2 inválidos) | ✅ |
| 2 testes automatizados (ac3_testes.py) | ✅ |
| 2 bugs identificados | ✅ |
| Melhorias propostas | ✅ |

---

*Projeto desenvolvido para a disciplina de Engenharia de Software – UNIFECAF*
