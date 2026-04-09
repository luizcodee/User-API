import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_cadastro_usuario():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post("/usuarios", json={
            "nome": "Usuário Teste",
            "email": "teste1@exemplo.com",
            "senha": "123456"
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["email"] == "teste1@exemplo.com"

@pytest.mark.asyncio
async def test_listar_usuarios():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.get("/usuarios")
        assert resp.status_code == 200
        assert isinstance(resp.json(), list)

@pytest.mark.asyncio
async def test_buscar_usuario_por_id():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Cria usuário
        resp = await ac.post("/usuarios", json={
            "nome": "Busca ID",
            "email": "buscaid@exemplo.com",
            "senha": "123456"
        })
        user_id = resp.json()["id"]
        # Busca por ID
        resp = await ac.get(f"/usuarios/{user_id}")
        assert resp.status_code == 200
        assert resp.json()["email"] == "buscaid@exemplo.com"

@pytest.mark.asyncio
async def test_atualizar_usuario():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Cria usuário
        resp = await ac.post("/usuarios", json={
            "nome": "Atualiza Teste",
            "email": "atualiza@exemplo.com",
            "senha": "123456"
        })
        user_id = resp.json()["id"]
        # Atualiza
        resp = await ac.put(f"/usuarios/{user_id}", json={
            "nome": "Atualizado",
            "email": "atualiza@exemplo.com",
            "senha": "654321"
        })
        assert resp.status_code == 200
        assert resp.json()["nome"] == "Atualizado"

@pytest.mark.asyncio
async def test_excluir_usuario():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Cria usuário
        resp = await ac.post("/usuarios", json={
            "nome": "Excluir Teste",
            "email": "excluir@exemplo.com",
            "senha": "123456"
        })
        user_id = resp.json()["id"]
        # Exclui
        resp = await ac.delete(f"/usuarios/{user_id}")
        assert resp.status_code == 200
        # Confirma exclusão
        resp = await ac.get(f"/usuarios/{user_id}")
        assert resp.status_code == 404

@pytest.mark.asyncio
async def test_validacao_email_invalido():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post("/usuarios", json={
            "nome": "Inválido",
            "email": "emailinvalido",
            "senha": "123456"
        })
        assert resp.status_code == 422

@pytest.mark.asyncio
async def test_validacao_senha_curta():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post("/usuarios", json={
            "nome": "Inválido",
            "email": "valido@exemplo.com",
            "senha": "123"
        })
        assert resp.status_code == 422 or resp.status_code == 400
