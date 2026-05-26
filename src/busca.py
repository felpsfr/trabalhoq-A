"""Busca e filtro de restaurantes no Local Eats.

Permite filtrar uma lista de restaurantes por nome (substring, case-insensitive)
e/ou por categoria (Italiana, Japonesa, Brasileira, Mexicana, etc.).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class RestauranteInfo:
    nome: str
    categoria: str
    nota: float


def filtrar(
    restaurantes: List[RestauranteInfo],
    termo: Optional[str] = None,
    categoria: Optional[str] = None,
) -> List[RestauranteInfo]:
    """Retorna restaurantes que combinem com `termo` (no nome) e/ou `categoria`.

    - Termo vazio ou None → não filtra por nome.
    - Categoria "Todos" ou None → não filtra por categoria.
    - Comparações são case-insensitive.
    """
    resultado = list(restaurantes)

    if termo:
        termo_norm = termo.strip().lower()
        if termo_norm:
            resultado = [r for r in resultado if termo_norm in r.nome.lower()]

    if categoria and categoria.strip().lower() != "todos":
        cat_norm = categoria.strip().lower()
        resultado = [r for r in resultado if r.categoria.lower() == cat_norm]

    return resultado
