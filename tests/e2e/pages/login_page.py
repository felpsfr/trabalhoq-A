"""POM da página de login do Local Eats.

URL: https://local-eats-unisenac.vercel.app/  (redireciona para /static/login.html)
Seletores reais coletados via Playwright sobre o ambiente em produção.
"""
from __future__ import annotations

from playwright.sync_api import Page, expect


class LoginPage:
    URL = "https://local-eats-unisenac.vercel.app/"

    # Credenciais de teste fornecidas pelo próprio sistema (placeholder do form)
    USUARIO_VALIDO = "teste@teste.com"
    SENHA_VALIDA = "123"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.campo_email = page.locator("#loginEmail")
        self.campo_senha = page.locator("#loginPassword")
        self.botao_entrar = page.locator("button.primary-btn", has_text="Entrar")
        self.aba_criar_conta = page.get_by_role("button", name="Criar Conta")
        self.mensagem_erro = page.locator("#errorMsg")

    def abrir(self) -> None:
        self.page.goto(self.URL, wait_until="networkidle")

    def login(self, email: str, senha: str) -> None:
        self.campo_email.fill(email)
        self.campo_senha.fill(senha)
        self.botao_entrar.click()

    def login_com_credenciais_validas(self) -> None:
        self.login(self.USUARIO_VALIDO, self.SENHA_VALIDA)

    def deve_mostrar_formulario(self) -> None:
        expect(self.campo_email).to_be_visible()
        expect(self.campo_senha).to_be_visible()
        expect(self.botao_entrar).to_be_visible()

    def deve_mostrar_mensagem_de_erro(self) -> None:
        expect(self.mensagem_erro).to_be_visible()
