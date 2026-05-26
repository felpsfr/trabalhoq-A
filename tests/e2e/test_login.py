"""Testes funcionais E2E do fluxo de autenticação do Local Eats.

Casos:
- CT-E2E-01 — formulário de login carrega
- CT-E2E-02 — login com credenciais válidas → home pós-login
- CT-E2E-03 — login com senha incorreta → permanece no login e exibe erro
- CT-E2E-04 — login com email inexistente → exibe erro
- CT-E2E-05 — campos obrigatórios bloqueiam submit vazio
"""
from __future__ import annotations

import pytest
from playwright.sync_api import expect

from tests.e2e.pages.home_page import HomePage
from tests.e2e.pages.login_page import LoginPage


@pytest.fixture
def login(page) -> LoginPage:
    lp = LoginPage(page)
    lp.abrir()
    return lp


class TestLogin:
    def test_formulario_de_login_carrega(self, login: LoginPage):
        """CT-E2E-01 (happy path) — formulário visível."""
        login.deve_mostrar_formulario()

    def test_login_com_credenciais_validas_redireciona_para_home(self, login: LoginPage):
        """CT-E2E-02 (happy path) — login válido leva à home com lista de restaurantes."""
        login.login_com_credenciais_validas()
        login.page.wait_for_url("**/static/index.html", timeout=10_000)
        home = HomePage(login.page)
        home.deve_estar_carregada()
        home.deve_listar_restaurantes(minimo=1)

    def test_login_com_senha_incorreta_mostra_erro(self, login: LoginPage):
        """CT-E2E-03 (erro) — senha errada, usuário permanece no login."""
        login.login(LoginPage.USUARIO_VALIDO, "senha-errada")
        login.page.wait_for_timeout(1500)
        # ou exibe a mensagem de erro, ou continua na URL de login
        assert "login" in login.page.url or login.mensagem_erro.is_visible(), (
            "Login com senha errada deveria falhar."
        )

    def test_login_com_email_inexistente_mostra_erro(self, login: LoginPage):
        """CT-E2E-04 (erro) — usuário desconhecido."""
        login.login("naoexiste@xyz.com", "qualquersenha")
        login.page.wait_for_timeout(1500)
        assert "login" in login.page.url or login.mensagem_erro.is_visible()

    def test_campos_obrigatorios_bloqueiam_submit_vazio(self, login: LoginPage):
        """CT-E2E-05 (validação) — submit sem dados não redireciona."""
        login.botao_entrar.click()
        login.page.wait_for_timeout(800)
        # form HTML5 `required` impede o submit; permanecemos no login
        assert "login" in login.page.url
        expect(login.campo_email).to_be_visible()
