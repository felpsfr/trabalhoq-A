"""Testes funcionais E2E da home (Explorar) e navegação do Local Eats.

Casos:
- CT-E2E-06 — home carrega após login com banner, busca e menu
- CT-E2E-07 — home lista pelo menos 1 restaurante
- CT-E2E-08 — clicar em um card abre a página do restaurante
- CT-E2E-09 — navegar para Meus Favoritos
- CT-E2E-10 — navegar para Meus Pedidos
"""
from __future__ import annotations

import pytest
from playwright.sync_api import expect

from tests.e2e.pages.home_page import HomePage
from tests.e2e.pages.login_page import LoginPage


@pytest.fixture
def home(page) -> HomePage:
    """Autentica e retorna a HomePage pronta."""
    lp = LoginPage(page)
    lp.abrir()
    lp.login_com_credenciais_validas()
    page.wait_for_url("**/static/index.html", timeout=10_000)
    return HomePage(page)


class TestHome:
    def test_home_carrega_apos_login(self, home: HomePage):
        """CT-E2E-06 — happy path."""
        home.deve_estar_carregada()

    def test_home_lista_restaurantes(self, home: HomePage):
        """CT-E2E-07 — pelo menos 1 restaurante visível."""
        home.deve_listar_restaurantes(minimo=1)

    def test_clicar_em_card_abre_pagina_do_restaurante(self, home: HomePage):
        """CT-E2E-08 — navegação para o detalhe."""
        home.abrir_primeiro_restaurante()
        home.page.wait_for_load_state("networkidle")
        assert "restaurant.html" in home.page.url

    def test_navega_para_meus_favoritos(self, home: HomePage):
        """CT-E2E-09 — Meus Favoritos."""
        home.ir_para_favoritos()
        home.page.wait_for_load_state("networkidle")
        assert "profile.html" in home.page.url

    def test_navega_para_meus_pedidos(self, home: HomePage):
        """CT-E2E-10 — Meus Pedidos."""
        home.ir_para_pedidos()
        home.page.wait_for_load_state("networkidle")
        assert "orders.html" in home.page.url
