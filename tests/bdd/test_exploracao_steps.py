"""Steps Gherkin → Python para features/exploracao.feature."""
from __future__ import annotations

from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when

from tests.e2e.pages.home_page import HomePage
from tests.e2e.pages.login_page import LoginPage

scenarios("features/exploracao.feature")


@given(
    parsers.parse('que estou autenticado no Local Eats com "{email}" / "{senha}"'),
    target_fixture="home_page",
)
def autentica_e_retorna_home(page, email: str, senha: str):
    lp = LoginPage(page)
    lp.abrir()
    lp.login(email, senha)
    page.wait_for_url("**/static/index.html", timeout=10_000)
    return HomePage(page)


@when("a página inicial termina de carregar")
def aguarda_home_carregar(home_page: HomePage):
    home_page.page.wait_for_load_state("networkidle")


@when("clico no primeiro restaurante da lista")
def clica_primeiro_restaurante(home_page: HomePage):
    home_page.page.wait_for_load_state("networkidle")
    home_page.abrir_primeiro_restaurante()
    home_page.page.wait_for_load_state("networkidle")


@then(parsers.parse("vejo pelo menos {n:d} restaurante na lista"))
def deve_ver_n_restaurantes(home_page: HomePage, n: int):
    expect(home_page.cards_restaurante.first).to_be_visible()
    assert home_page.total_restaurantes() >= n


@then(parsers.parse('sou levado a uma página cujo endereço contém "{trecho}"'))
def deve_estar_em_url_que_contem(home_page: HomePage, trecho: str):
    assert trecho in home_page.page.url, f"URL atual: {home_page.page.url}"
