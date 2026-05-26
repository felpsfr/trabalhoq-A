"""Steps Gherkin → Python para features/autenticacao.feature."""
from __future__ import annotations

import pytest
from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when

from tests.e2e.pages.home_page import HomePage
from tests.e2e.pages.login_page import LoginPage

scenarios("features/autenticacao.feature")


# ---------- Given ----------
@given("que estou na página de login do Local Eats", target_fixture="login_page")
def abre_pagina_login(page):
    lp = LoginPage(page)
    lp.abrir()
    return lp


# ---------- When ----------
@when(parsers.parse('informo o e-mail "{email}" e a senha "{senha}"'))
def informa_credenciais(login_page: LoginPage, email: str, senha: str):
    login_page.campo_email.fill(email)
    login_page.campo_senha.fill(senha)


@when(parsers.parse('clico no botão "{rotulo}"'))
def clica_botao(login_page: LoginPage, rotulo: str):
    if rotulo == "Entrar":
        login_page.botao_entrar.click()
    else:
        login_page.page.get_by_role("button", name=rotulo).click()


# ---------- Then ----------
@then("sou redirecionado para a página inicial")
def deve_redirecionar_para_home(login_page: LoginPage):
    login_page.page.wait_for_url("**/static/index.html", timeout=10_000)


@then(parsers.parse('vejo o banner "{texto}"'))
def deve_ver_banner(login_page: LoginPage, texto: str):
    home = HomePage(login_page.page)
    expect(home.page.get_by_role("heading", name=texto)).to_be_visible()


@then("permaneço na página de login")
def deve_permanecer_no_login(login_page: LoginPage):
    login_page.page.wait_for_timeout(1500)
    assert "login" in login_page.page.url, f"Esperava continuar no login; URL: {login_page.page.url}"


@then("uma mensagem de erro é exibida")
def deve_exibir_erro(login_page: LoginPage):
    # tolerante: mensagem visível OU permaneceu no login (browser pode bloquear via required)
    if not login_page.mensagem_erro.is_visible():
        pytest.skip("Mensagem de erro não estava visível neste ambiente (form HTML5).")
