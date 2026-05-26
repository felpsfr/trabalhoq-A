# PBL 6 — Testes Unitários Automatizados e TDD (Local Eats)

> Centro Universitário Senac-RS
> Unidade Curricular: Qualidade de Software
> Prof.: Luciano Zanuz
> **Integrante:** Felipe Ferreira Ribeiro — 782410083

## 1. Objetivo

Aplicar a metodologia **TDD** (Test-Driven Development) no desenvolvimento de três regras de negócio do sistema **Local Eats**, utilizando **Python 3** e **Pytest**. Cada regra foi conduzida pelo ciclo **Red → Green → Refactor**, e todos os testes foram automatizados e executados via terminal.

## 2. Regras de Negócio Selecionadas

| # | Módulo | Regra | Arquivo fonte | Arquivo de teste |
|---|---|---|---|---|
| 1 | Avaliação | Cálculo da média de avaliações (1–5 estrelas), com validação de notas | [src/avaliacao.py](../src/avaliacao.py) | [tests/unit/test_avaliacao.py](../tests/unit/test_avaliacao.py) |
| 2 | Taxa de entrega | Cálculo do frete por distância, com limite de cobertura e frete grátis | [src/taxa_entrega.py](../src/taxa_entrega.py) | [tests/unit/test_taxa_entrega.py](../tests/unit/test_taxa_entrega.py) |
| 3 | Busca | Filtro de restaurantes por nome (substring case-insensitive) e categoria | [src/busca.py](../src/busca.py) | [tests/unit/test_busca.py](../tests/unit/test_busca.py) |

## 3. Setup do ambiente

```bash
python -m pip install -r requirements.txt
python -m pytest tests/unit -v
```

Arquivo `pytest.ini` na raiz já configura `testpaths`, padrão de descoberta e verbosidade.

## 4. Aplicação do ciclo TDD

### 4.1 Regra 1 — Cálculo da média de avaliações

**Iteração 1 — Função `calcular_media`**

| Fase | Ação | Resultado |
|---|---|---|
| 🔴 Red | Escrevi `test_lista_vazia_retorna_zero` antes do código de produção. | `ModuleNotFoundError: No module named 'src.avaliacao'` |
| 🟢 Green | Criei `src/avaliacao.py` com `def calcular_media(notas): return 0.0`. | 1 teste passou. |
| 🔁 Refactor | Adicionei `test_media_de_varias_notas`; ajustei para `sum(notas) / len(notas)` e protegi contra divisão por zero. | 3 testes passando. |
| 🔁 Refactor | Adicionei `test_media_arredondada_para_uma_casa`; envolvi o retorno em `round(..., 1)`. | 4 testes passando. |

**Iteração 2 — Validação de notas inválidas**

| Fase | Ação | Resultado |
|---|---|---|
| 🔴 Red | Escrevi `test_nota_fora_do_intervalo_lanca_value_error` com `pytest.mark.parametrize`. | Falhou — função aceitava notas fora do intervalo. |
| 🟢 Green | Adicionei guard `if not isinstance(n, int) or n < 1 or n > 5: raise ValueError`. | Todos os parametrize verdes. |
| 🔁 Refactor | Extraí constantes `NOTA_MINIMA` e `NOTA_MAXIMA` para o topo do módulo. | Comportamento preservado. |

**Iteração 3 — Encapsular em entidade `Restaurante`**

| Fase | Ação | Resultado |
|---|---|---|
| 🔴 Red | Escrevi `test_restaurante_novo_tem_media_zero_e_zero_avaliacoes`. | `ImportError: cannot import name 'Restaurante'`. |
| 🟢 Green | Criei `@dataclass class Restaurante` reutilizando `calcular_media`. | 1 teste passa. |
| 🔁 Refactor | Adicionei `test_adicionar_nota_invalida_nao_altera_estado` para garantir atomicidade — validação foi colocada **antes** do `append`, mantendo a lista íntegra em caso de erro. | 16 testes (do módulo) verdes. |

### 4.2 Regra 2 — Taxa de entrega

A regra envolve várias faixas (limites). Apliquei **valores-limite** e **classes de equivalência**:

- Distância **inválida**: ≤ 0 e > 15 km.
- Distância **dentro do raio base**: (0, 3] km → taxa fixa.
- Distância **adicional**: (3, 15] km → R$ 5,00 + R$ 1,50 × km excedentes.
- Pedido com **frete grátis**: valor ≥ R$ 80,00 zera a taxa, independente da distância.

Iteração TDD: testes de "fixo dentro do raio" → testes de borda (3 e 15 km) → testes de valor inválido → testes de frete grátis. Cada falha derrubou o caso esperado; a implementação foi crescendo proporcionalmente — sem regras inventadas.

### 4.3 Regra 3 — Busca de restaurantes

Iniciei com o filtro por termo (substring case-insensitive). Depois introduzi o filtro por categoria reutilizando a mesma função (com parâmetro opcional), e por fim o **filtro combinado** que aplica os dois em sequência. O refactor para extrair `cat_norm = categoria.strip().lower()` veio depois que o teste de categoria com espaços/maiúsculas passou — refatorei com a malha já verde.

## 5. Execução automatizada e evidência

Comando executado na raiz do projeto:

```bash
python -m pytest tests/unit -v
```

Resultado (saída completa em [artefatos/evidencias/pbl-06-pytest-output.txt](../artefatos/evidencias/pbl-06-pytest-output.txt)):

```
============================= test session starts =============================
platform win32 -- Python 3.14.0, pytest-9.0.3
collected 35 items

tests/unit/test_avaliacao.py ................        [ 45%]
tests/unit/test_busca.py ........                    [ 68%]
tests/unit/test_taxa_entrega.py ...........          [100%]

============================= 35 passed in 0.15s ==============================
```

| Métrica | Valor |
|---|---|
| Total de testes | **35** |
| Aprovados | 35 |
| Reprovados | 0 |
| Tempo total | ~0,15 s |

## 6. Análise dos resultados

- **Cobertura por classes de equivalência**: cada regra foi exercitada por entrada válida típica, valor-limite e entrada inválida. Não há ramos de produção sem teste correspondente.
- **Testes parametrizados** (`pytest.mark.parametrize`) reduziram drasticamente a duplicação — uma única função cobre 5 cenários de "nota fora do intervalo".
- **Falhas controladas**: os testes que esperam `ValueError` provam que o módulo falha de forma previsível ao invés de retornar valores silenciosos incorretos (ex.: média 0 para entrada lixo).

## 7. Reflexão

> *Como o TDD mudou a forma de escrever o código?*

Escrever o teste antes força a definir a **interface pública** primeiro (`calcular_media(notas)`, `Restaurante.adicionar_avaliacao(nota)`) e só depois pensar na implementação. Isso evitou abstrações prematuras — por exemplo, a primeira versão de `calcular_media` tinha 1 linha. Só depois que os testes de validação chegaram é que apareceu o guard com `isinstance`.

> *Algum bug só foi pego pelo teste?*

Sim — o teste `test_adicionar_nota_invalida_nao_altera_estado` exigiu reorganizar a ordem das instruções em `Restaurante.adicionar_avaliacao`: a primeira versão fazia `append` antes de validar, o que corrompia o estado quando o `ValueError` era lançado.

> *O que melhoraria com mais tempo?*

- Adicionar **coverage report** (`pytest-cov`) para medir percentual.
- Conectar a suíte ao **CI** (GitHub Actions) para rodar em cada push.
- Adicionar **property-based testing** com `hypothesis` para gerar entradas aleatórias.

## 8. Relação com Elementos de Competência

- **EC4 — Planejar e projetar testes selecionando técnicas adequadas**: aplicação explícita de **valores-limite** (taxa de entrega), **classes de equivalência** (avaliação) e **testes parametrizados**.
- **EC5 — Implementar testes manuais e automatizados (TDD)**: ciclo Red-Green-Refactor documentado por iteração, com toda a suíte automatizada em Pytest.
