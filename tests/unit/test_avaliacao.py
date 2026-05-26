"""Testes unitários para src/avaliacao.py.

Cada bloco abaixo corresponde a uma iteração TDD (Red → Green → Refactor)
documentada em pbl/aula-09-testes-unitarios-tdd.md.
"""
import pytest

from src.avaliacao import Restaurante, calcular_media


class TestCalcularMedia:
    """Iteração 1 — cálculo da média."""

    def test_lista_vazia_retorna_zero(self):
        assert calcular_media([]) == 0.0

    def test_unica_nota_retorna_a_propria_nota(self):
        assert calcular_media([4]) == 4.0

    def test_media_de_varias_notas(self):
        assert calcular_media([5, 4, 3]) == 4.0

    def test_media_arredondada_para_uma_casa(self):
        # (4 + 5 + 4 + 3) / 4 = 4.0
        assert calcular_media([4, 5, 4, 3]) == 4.0
        # (5 + 4) / 2 = 4.5
        assert calcular_media([5, 4]) == 4.5
        # (5 + 5 + 4) / 3 = 4.666... → 4.7
        assert calcular_media([5, 5, 4]) == 4.7


class TestValidacaoDeNota:
    """Iteração 2 — validação de entradas inválidas."""

    @pytest.mark.parametrize("nota_invalida", [0, 6, -1, 10, 100])
    def test_nota_fora_do_intervalo_lanca_value_error(self, nota_invalida):
        with pytest.raises(ValueError):
            calcular_media([4, nota_invalida])

    @pytest.mark.parametrize("nota_invalida", [3.5, "5", None, [4]])
    def test_nota_nao_inteira_lanca_value_error(self, nota_invalida):
        with pytest.raises(ValueError):
            calcular_media([nota_invalida])


class TestRestaurante:
    """Iteração 3 — encapsular comportamento em uma entidade Restaurante."""

    def test_restaurante_novo_tem_media_zero_e_zero_avaliacoes(self):
        r = Restaurante(nome="Cantina da Nonna")
        assert r.media == 0.0
        assert r.total_avaliacoes == 0

    def test_adicionar_avaliacoes_atualiza_media_e_contagem(self):
        r = Restaurante(nome="Sushi do Bairro")
        r.adicionar_avaliacao(5)
        r.adicionar_avaliacao(4)
        r.adicionar_avaliacao(3)
        assert r.total_avaliacoes == 3
        assert r.media == 4.0

    def test_adicionar_nota_invalida_nao_altera_estado(self):
        r = Restaurante(nome="Tacos del Sol")
        r.adicionar_avaliacao(5)
        with pytest.raises(ValueError):
            r.adicionar_avaliacao(7)
        assert r.total_avaliacoes == 1
        assert r.media == 5.0
