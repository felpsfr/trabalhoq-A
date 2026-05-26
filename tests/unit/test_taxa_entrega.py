"""Testes unitários para src/taxa_entrega.py.

Cobertura por classes de equivalência e valores-limite:
- distância (negativa, zero, dentro do raio base, na borda, acima do raio, fora da cobertura)
- valor do pedido (zero, abaixo, igual e acima do limite de frete grátis)
"""
import pytest

from src.taxa_entrega import (
    RAIO_BASE_KM,
    RAIO_MAXIMO_KM,
    TAXA_BASE,
    VALOR_FRETE_GRATIS,
    calcular_taxa,
)


class TestDistanciaValida:
    def test_distancia_dentro_do_raio_base_cobra_taxa_fixa(self):
        assert calcular_taxa(distancia_km=1.0) == TAXA_BASE
        assert calcular_taxa(distancia_km=3.0) == TAXA_BASE  # limite

    def test_distancia_acima_do_raio_base_cobra_adicional_por_km(self):
        # 4 km → 5,00 + 1 * 1,50 = 6,50
        assert calcular_taxa(distancia_km=4.0) == 6.50

    def test_distancia_no_limite_maximo_de_cobertura(self):
        # 15 km → 5,00 + 12 * 1,50 = 23,00
        assert calcular_taxa(distancia_km=RAIO_MAXIMO_KM) == 23.00


class TestDistanciaInvalida:
    @pytest.mark.parametrize("distancia", [0, -1, -10.5])
    def test_distancia_nao_positiva_lanca_value_error(self, distancia):
        with pytest.raises(ValueError):
            calcular_taxa(distancia_km=distancia)

    def test_distancia_fora_da_cobertura_lanca_value_error(self):
        with pytest.raises(ValueError):
            calcular_taxa(distancia_km=RAIO_MAXIMO_KM + 0.1)


class TestFreteGratis:
    def test_pedido_no_limite_de_frete_gratis_zera_taxa(self):
        assert calcular_taxa(distancia_km=10.0, valor_pedido=VALOR_FRETE_GRATIS) == 0.0

    def test_pedido_acima_do_limite_de_frete_gratis_zera_taxa(self):
        assert calcular_taxa(distancia_km=10.0, valor_pedido=200.00) == 0.0

    def test_pedido_abaixo_do_limite_mantem_taxa_normal(self):
        # 5 km, pedido R$ 79,99 → taxa = 5,00 + 2 * 1,50 = 8,00
        assert calcular_taxa(distancia_km=5.0, valor_pedido=79.99) == 8.00

    def test_valor_pedido_negativo_lanca_value_error(self):
        with pytest.raises(ValueError):
            calcular_taxa(distancia_km=2.0, valor_pedido=-1.0)
