"""POM da página inicial (pós-login) do Local Eats.

URL real: https://local-eats-unisenac.vercel.app/static/index.html
"""
from __future__ import annotations

from playwright.sync_api import Locator, Page, expect


class HomePage:
    URL = "https://local-eats-unisenac.vercel.app/static/index.html"

    CATEGORIAS = ("Todos", "Italiana", "Japonesa", "Brasileira", "Mexicana")

    def __init__(self, page: Page) -> None:
        self.page = page
        self.banner = page.get_by_role(
            "heading", name="Descubra sabores incríveis na sua cidade"
        )
        self.campo_busca = page.get_by_placeholder("Buscar restaurantes...")
        self.link_explorar = page.get_by_role("link", name="Explorar")
        self.link_favoritos = page.get_by_role("link", name="Meus Favoritos")
        self.link_pedidos = page.get_by_role("link", name="Meus Pedidos")
        # cards de restaurante são <a href="restaurant.html?id=N">
        self.cards_restaurante = page.locator("a[href^='restaurant.html?id=']")

    # ---------- ações ----------
    def buscar(self, termo: str) -> None:
        if self.campo_busca.is_visible():
            self.campo_busca.fill(termo)
            self.campo_busca.press("Enter")

    def filtrar_por_categoria(self, categoria: str) -> None:
        if categoria not in self.CATEGORIAS:
            raise ValueError(f"Categoria inválida: {categoria}.")
        # botões/links de categoria possuem o nome diretamente
        botao = self.page.get_by_role("button", name=categoria).or_(
            self.page.get_by_role("link", name=categoria)
        )
        botao.first.click()
        self.page.wait_for_load_state("networkidle")

    def abrir_primeiro_restaurante(self) -> None:
        self.cards_restaurante.first.click()

    def ir_para_favoritos(self) -> None:
        self.link_favoritos.click()

    def ir_para_pedidos(self) -> None:
        self.link_pedidos.click()

    # ---------- consultas ----------
    def total_restaurantes(self) -> int:
        return self.cards_restaurante.count()

    def restaurantes(self) -> Locator:
        return self.cards_restaurante

    # ---------- assertions ----------
    def deve_estar_carregada(self) -> None:
        expect(self.banner).to_be_visible()
        expect(self.link_explorar).to_be_visible()
        expect(self.link_favoritos).to_be_visible()
        expect(self.link_pedidos).to_be_visible()

    def deve_listar_restaurantes(self, minimo: int = 1) -> None:
        expect(self.cards_restaurante.first).to_be_visible()
        assert self.total_restaurantes() >= minimo, (
            f"Esperado pelo menos {minimo} restaurante(s), encontrado {self.total_restaurantes()}."
        )
