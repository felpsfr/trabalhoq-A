"""Cálculo de média de avaliações de restaurantes.

Regras de negócio extraídas do contexto Local Eats:
- Cada avaliação é um inteiro de 1 a 5 (estrelas).
- A média é arredondada em uma casa decimal.
- Um restaurante sem avaliações retorna média 0.0 e contagem 0.
- Avaliações fora do intervalo [1, 5] são rejeitadas com ValueError.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List


NOTA_MINIMA = 1
NOTA_MAXIMA = 5


def calcular_media(notas: Iterable[int]) -> float:
    """Retorna a média das notas arredondada a 1 casa decimal.

    Lança ValueError se qualquer nota estiver fora de [1, 5].
    Lista vazia retorna 0.0 (restaurante sem avaliações).
    """
    notas = list(notas)
    if not notas:
        return 0.0
    for n in notas:
        if not isinstance(n, int) or n < NOTA_MINIMA or n > NOTA_MAXIMA:
            raise ValueError(f"Nota inválida: {n!r}. Deve ser inteiro entre {NOTA_MINIMA} e {NOTA_MAXIMA}.")
    return round(sum(notas) / len(notas), 1)


@dataclass
class Restaurante:
    """Agregador simples de avaliações de um restaurante."""

    nome: str
    avaliacoes: List[int] = field(default_factory=list)

    def adicionar_avaliacao(self, nota: int) -> None:
        if not isinstance(nota, int) or nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
            raise ValueError(f"Nota inválida: {nota!r}.")
        self.avaliacoes.append(nota)

    @property
    def media(self) -> float:
        return calcular_media(self.avaliacoes)

    @property
    def total_avaliacoes(self) -> int:
        return len(self.avaliacoes)
