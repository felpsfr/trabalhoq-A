"""Testes unitários para src/busca.py."""
import pytest

from src.busca import RestauranteInfo, filtrar


@pytest.fixture
def catalogo():
    return [
        RestauranteInfo(nome="Cantina da Nonna", categoria="Italiana", nota=4.7),
        RestauranteInfo(nome="Sushi do Bairro", categoria="Japonesa", nota=4.5),
        RestauranteInfo(nome="Boteco do Zé", categoria="Brasileira", nota=4.2),
        RestauranteInfo(nome="Tacos del Sol", categoria="Mexicana", nota=4.6),
        RestauranteInfo(nome="Pizzaria Bella", categoria="Italiana", nota=4.4),
    ]


class TestFiltroPorTermo:
    def test_termo_vazio_retorna_todos(self, catalogo):
        assert filtrar(catalogo, termo="") == catalogo
        assert filtrar(catalogo, termo=None) == catalogo

    def test_termo_substring_case_insensitive(self, catalogo):
        resultado = filtrar(catalogo, termo="sushi")
        assert len(resultado) == 1
        assert resultado[0].nome == "Sushi do Bairro"

        resultado = filtrar(catalogo, termo="DA")
        nomes = {r.nome for r in resultado}
        assert nomes == {"Cantina da Nonna"}

    def test_termo_sem_correspondencia_retorna_lista_vazia(self, catalogo):
        assert filtrar(catalogo, termo="vegano") == []


class TestFiltroPorCategoria:
    def test_categoria_todos_nao_filtra(self, catalogo):
        assert filtrar(catalogo, categoria="Todos") == catalogo

    def test_filtra_apenas_categoria_solicitada(self, catalogo):
        resultado = filtrar(catalogo, categoria="Italiana")
        assert len(resultado) == 2
        assert all(r.categoria == "Italiana" for r in resultado)

    def test_categoria_inexistente_retorna_lista_vazia(self, catalogo):
        assert filtrar(catalogo, categoria="Tailandesa") == []


class TestFiltroCombinado:
    def test_termo_e_categoria_aplicados_juntos(self, catalogo):
        resultado = filtrar(catalogo, termo="pizza", categoria="Italiana")
        assert len(resultado) == 1
        assert resultado[0].nome == "Pizzaria Bella"

    def test_termo_combinado_com_categoria_que_nao_bate(self, catalogo):
        resultado = filtrar(catalogo, termo="pizza", categoria="Japonesa")
        assert resultado == []
