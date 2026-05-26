"""Cálculo da taxa de entrega para pedidos do Local Eats.

Regras:
- Distância <= 0 km   → ValueError (entrega inválida).
- Distância <= 3 km   → taxa fixa de R$ 5,00.
- 3 km < distância    → R$ 5,00 + R$ 1,50 por km excedente.
- Distância > 15 km   → fora da área de cobertura → ValueError.
- Pedidos acima de R$ 80,00 ganham frete grátis (taxa = 0).
"""
from __future__ import annotations


TAXA_BASE = 5.00
ADICIONAL_POR_KM = 1.50
RAIO_BASE_KM = 3.0
RAIO_MAXIMO_KM = 15.0
VALOR_FRETE_GRATIS = 80.00


def calcular_taxa(distancia_km: float, valor_pedido: float = 0.0) -> float:
    """Retorna a taxa de entrega arredondada para 2 casas decimais."""
    if distancia_km <= 0:
        raise ValueError("Distância deve ser maior que zero.")
    if distancia_km > RAIO_MAXIMO_KM:
        raise ValueError(f"Distância {distancia_km}km fora da área de cobertura (máx {RAIO_MAXIMO_KM}km).")
    if valor_pedido < 0:
        raise ValueError("Valor do pedido não pode ser negativo.")

    if valor_pedido >= VALOR_FRETE_GRATIS:
        return 0.0

    if distancia_km <= RAIO_BASE_KM:
        return TAXA_BASE

    km_excedentes = distancia_km - RAIO_BASE_KM
    return round(TAXA_BASE + km_excedentes * ADICIONAL_POR_KM, 2)
