# Projeto — Qualidade de Software (Local Eats)

Repositório das atividades do PBL da disciplina de **Qualidade de Software** do Centro Universitário Senac-RS (Prof. Luciano Zanuz), aplicadas ao estudo de caso da plataforma **Local Eats**.

## Integrantes do grupo

- Felipe Ferreira Ribeiro — Matrícula: 782410083

## Objetivo do repositório

Reunir todas as entregas do PBL da disciplina, servindo como:

- Portfólio de aprendizagem
- Registro da evolução do projeto ao longo do semestre
- Evidência das competências desenvolvidas
- Base para a avaliação por competências

## Estrutura do repositório

```
local-eats-pbl/
├── README.md
├── requirements.txt                  # Dependências Python (Pytest, Playwright, pytest-bdd)
├── pytest.ini                        # Configuração Pytest
├── pbl/                              # Entregas das atividades (documentação)
│   ├── aula-02-atributos-qualidade-iso25000.md   # PBL 1
│   ├── aula-03-diagnostico-qa.md                 # PBL 2
│   ├── aula-04-estrategia-inicial-testes.md      # PBL 3
│   ├── aula-05-testes-funcionais-estruturais.md  # PBL 4
│   ├── aula-06-planejamento-testes.md            # PBL 5
│   ├── aula-09-testes-unitarios-tdd.md           # PBL 6
│   ├── aula-10-testes-funcionais-automatizados.md # PBL 7
│   └── aula-12-bdd-automacao-comportamento.md    # PBL 8
├── src/                              # Módulos de negócio (PBL 6 — TDD)
│   ├── avaliacao.py
│   ├── taxa_entrega.py
│   └── busca.py
├── tests/
│   ├── unit/                         # Testes unitários (PBL 6)
│   ├── e2e/                          # Testes funcionais Playwright (PBL 7)
│   │   └── pages/                    # Page Object Model
│   └── bdd/                          # Testes BDD pytest-bdd (PBL 8)
│       └── features/                 # Specs Gherkin (.feature)
├── artefatos/
│   └── evidencias/                   # Outputs e screenshots gerados pelos testes
├── docs/
│   └── enunciados/                   # Enunciados originais (referência)
└── scripts/                          # Scripts auxiliares (probes, captura de screenshots)
```

## Atividades PBL avaliadas

| #  | Atividade                                         | Entrega                                                                              |
|----|---------------------------------------------------|--------------------------------------------------------------------------------------|
| 1  | Atributos de qualidade da ISO 25000               | [pbl/aula-02-atributos-qualidade-iso25000.md](pbl/aula-02-atributos-qualidade-iso25000.md) |
| 2  | Papéis, Responsabilidades e Práticas de QA        | [pbl/aula-03-diagnostico-qa.md](pbl/aula-03-diagnostico-qa.md)                       |
| 3  | Estratégia Inicial de Testes                      | [pbl/aula-04-estrategia-inicial-testes.md](pbl/aula-04-estrategia-inicial-testes.md) |
| 4  | Testes Funcionais vs Estruturais                  | [pbl/aula-05-testes-funcionais-estruturais.md](pbl/aula-05-testes-funcionais-estruturais.md) |
| 5  | Planejamento e projeto de testes                  | [pbl/aula-06-planejamento-testes.md](pbl/aula-06-planejamento-testes.md)             |
| **6** | **Testes Unitários Automatizados e TDD**       | [pbl/aula-09-testes-unitarios-tdd.md](pbl/aula-09-testes-unitarios-tdd.md)           |
| **7** | **Testes Funcionais Automatizados (Playwright)** | [pbl/aula-10-testes-funcionais-automatizados.md](pbl/aula-10-testes-funcionais-automatizados.md) |
| **8** | **BDD e Automação Orientada a Comportamento**  | [pbl/aula-12-bdd-automacao-comportamento.md](pbl/aula-12-bdd-automacao-comportamento.md) |

## Elementos de Competência (EC) avaliados

- **EC1** — Compreender fundamentos de qualidade de software e sua aplicação no desenvolvimento.
- **EC2** — Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.
- **EC4** — Planejar e projetar testes selecionando técnicas adequadas.
- **EC5** — Implementar testes manuais e automatizados (incluindo TDD e BDD).

### Mapeamento PBL × EC

| Atividade PBL | EC1 | EC2 | EC4 | EC5 |
|---------------|:---:|:---:|:---:|:---:|
| PBL 1 — ISO 25000                                | ✔ |   |   |   |
| PBL 2 — Papéis e práticas de QA                  | ✔ | ✔ |   |   |
| PBL 3 — Estratégia inicial de testes             | ✔ |   | ✔ |   |
| PBL 4 — Funcionais vs Estruturais                | ✔ |   | ✔ |   |
| PBL 5 — Planejamento e projeto de testes         | ✔ |   | ✔ | ✔ |
| **PBL 6 — Testes Unitários + TDD**               |   |   | ✔ | ✔ |
| **PBL 7 — Testes Funcionais Automatizados**      |   |   | ✔ | ✔ |
| **PBL 8 — BDD**                                  |   |   | ✔ | ✔ |

## Como rodar os testes localmente

```bash
# 1. Instalar dependências
python -m pip install -r requirements.txt

# 2. Instalar o navegador do Playwright (apenas uma vez)
python -m playwright install chromium

# 3. Rodar a suíte completa (unitários + E2E + BDD)
python -m pytest -v

# Ou parcial:
python -m pytest tests/unit -v        # PBL 6 (35 testes)
python -m pytest tests/e2e  -v        # PBL 7 (10 testes E2E)
python -m pytest tests/bdd  -v        # PBL 8 (5 cenários BDD)
```

> Os testes E2E e BDD executam contra o ambiente em produção `https://local-eats-unisenac.vercel.app/`
> usando as credenciais públicas de demonstração `teste@teste.com` / `123`.

### Resumo da última execução

| Suíte | Testes | Aprovados | Tempo |
|---|---|---|---|
| Unitários (PBL 6) | 35 | 35 | ~0,2 s |
| E2E Playwright (PBL 7) | 10 | 10 | ~36 s |
| BDD pytest-bdd (PBL 8) | 5 | 5 | ~28 s |
| **Total** | **50** | **50** | ~65 s |

Saídas completas em [artefatos/evidencias/](artefatos/evidencias/).

## Contexto do projeto — Local Eats

Plataforma digital (web + mobile) que conecta moradores e turistas a restaurantes independentes, permitindo:

- Busca por tipo de culinária, localização e faixa de preço
- Visualização de cardápios, fotos e avaliações
- Salvamento de favoritos
- Recomendações personalizadas
- Compartilhamento de experiências

Ambiente de referência da aplicação: <https://local-eats-unisenac.vercel.app/>

## Metodologia

Aprendizagem Baseada em Problemas (PBL), com foco no desenvolvimento de competências em qualidade de software a partir de um estudo de caso contínuo.

## Boas práticas adotadas

- Commits frequentes e descritivos
- Organização clara das pastas
- Separação entre enunciados (`docs/enunciados/`), entregas (`pbl/`), código (`src/`) e testes (`tests/`)
- Page Object Model nos testes E2E
- Reuso dos POMs entre as suítes E2E e BDD
- Evidências de execução versionadas em `artefatos/evidencias/`
