"""POM — página Meus Favoritos."""
from __future__ import annotations

from playwright.sync_api import Page, expect


class FavoritosPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.titulo = page.get_by_role("heading", name="Meus Favoritos")
        self.mensagem_vazio = page.get_by_text("Você ainda não tem favoritos")

    def deve_estar_carregada(self) -> None:
        expect(self.titulo).to_be_visible()
