# PBL 8 — BDD e Automação Orientada a Comportamento (Local Eats)

> Centro Universitário Senac-RS
> Unidade Curricular: Qualidade de Software
> Prof.: Luciano Zanuz
> **Integrante:** Felipe Ferreira Ribeiro — 782410083

## 1. Objetivo

Aplicar **BDD (Behavior-Driven Development)** sobre o sistema Local Eats, descrevendo comportamentos esperados em **Gherkin** (formato `Dado / Quando / Então`) e automatizando-os com **pytest-bdd** + **Playwright**.

## 2. Fluxos escolhidos

1. **Autenticação** — porta de entrada do sistema.
2. **Exploração de restaurantes** — comportamento principal pós-login.

Cada fluxo virou um `.feature` legível para QA, PO e desenvolvedor — a mesma especificação que é o teste executável.

## 3. Estrutura

```
tests/bdd/
├── conftest.py                       # fixtures Playwright (browser, page)
├── features/
│   ├── autenticacao.feature          # 3 cenários (1 sucesso + 2 erro)
│   └── exploracao.feature            # 2 cenários (happy path)
├── test_autenticacao_steps.py        # mapeia Gherkin → Python (autenticação)
└── test_exploracao_steps.py          # mapeia Gherkin → Python (exploração)
```

Os POMs `LoginPage` e `HomePage` do [PBL 7](aula-10-testes-funcionais-automatizados.md) são **reutilizados** — os passos Gherkin chamam métodos do POM em vez de tocar Playwright diretamente. Isso evita duplicação entre as suítes E2E e BDD.

## 4. Cenários Gherkin

### 4.1 [tests/bdd/features/autenticacao.feature](../tests/bdd/features/autenticacao.feature)

```gherkin
# language: pt
Funcionalidade: Autenticação no Local Eats

  Contexto:
    Dado que estou na página de login do Local Eats

  Cenário: Login com credenciais válidas
    Quando informo o e-mail "teste@teste.com" e a senha "123"
    E clico no botão "Entrar"
    Então sou redirecionado para a página inicial
    E vejo o banner "Descubra sabores incríveis na sua cidade"

  Cenário: Login com senha incorreta
    Quando informo o e-mail "teste@teste.com" e a senha "senha-errada"
    E clico no botão "Entrar"
    Então permaneço na página de login
    E uma mensagem de erro é exibida

  Cenário: Login com e-mail inexistente
    Quando informo o e-mail "naoexiste@xyz.com" e a senha "qualquer"
    E clico no botão "Entrar"
    Então permaneço na página de login
    E uma mensagem de erro é exibida
```

### 4.2 [tests/bdd/features/exploracao.feature](../tests/bdd/features/exploracao.feature)

```gherkin
# language: pt
Funcionalidade: Exploração de restaurantes

  Contexto:
    Dado que estou autenticado no Local Eats com "teste@teste.com" / "123"

  Cenário: Lista de restaurantes é exibida na home
    Quando a página inicial termina de carregar
    Então vejo pelo menos 1 restaurante na lista

  Cenário: Abrir detalhe de um restaurante
    Quando clico no primeiro restaurante da lista
    Então sou levado a uma página cujo endereço contém "restaurant.html"
```

## 5. Implementação dos passos

Os arquivos `test_*_steps.py` ligam cada frase Gherkin a uma função Python via decoradores. Trecho:

```python
@given("que estou na página de login do Local Eats", target_fixture="login_page")
def abre_pagina_login(page):
    lp = LoginPage(page)
    lp.abrir()
    return lp

@when(parsers.parse('informo o e-mail "{email}" e a senha "{senha}"'))
def informa_credenciais(login_page, email, senha):
    login_page.campo_email.fill(email)
    login_page.campo_senha.fill(senha)

@then("sou redirecionado para a página inicial")
def deve_redirecionar_para_home(login_page):
    login_page.page.wait_for_url("**/static/index.html", timeout=10_000)
```

Note como o passo `@then` é uma instrução de **comportamento**, não de implementação — o que está alinhado com a filosofia BDD ("descreva o que, não o como").

## 6. Execução

```bash
$ python -m pytest tests/bdd -v
```

Saída completa em [artefatos/evidencias/pbl-08-pytest-output.txt](../artefatos/evidencias/pbl-08-pytest-output.txt):

```
============================= test session starts =============================
plugins: bdd-8.1.0
collected 5 items

tests/bdd/test_autenticacao_steps.py::test_login_com_credenciais_válidas PASSED
tests/bdd/test_autenticacao_steps.py::test_login_com_senha_incorreta     PASSED
tests/bdd/test_autenticacao_steps.py::test_login_com_email_inexistente   PASSED
tests/bdd/test_exploracao_steps.py::test_lista_de_restaurantes_é_exibida_na_home PASSED
tests/bdd/test_exploracao_steps.py::test_abrir_detalhe_de_um_restaurante PASSED

============================= 5 passed in 27.67s ==============================
```

| Métrica | Valor |
|---|---|
| Cenários executados | **5** |
| Aprovados | 5 |
| Reprovados | 0 |
| Tempo total | ~28 s |

## 7. Análise crítica

| Critério | Avaliação | Comentário |
|---|---|---|
| **Legibilidade** | 🟢 Alta | O `.feature` é entendido por qualquer stakeholder, mesmo sem conhecer Python. |
| **Reuso** | 🟢 Alta | Os mesmos POMs do PBL 7 servem aos cenários BDD. |
| **Robustez** | 🟡 Parcial | Cenários dependem do servidor estar no ar; `wait_for_url` reduz, mas não elimina, flakiness. |
| **Manutenção** | 🟢 Boa | Mudança na UI → editar apenas o POM. Mudança no comportamento → editar a feature. |
| **Tempo de execução** | 🟡 ~30s | Cada cenário sobe um contexto Chromium novo — adequado para CI, lento para iteração local. |

### Dificuldades

- **`pytest-bdd` 8.x usa o nome do cenário como nome de teste**, com acentos. Funciona, mas precisa de encoding UTF-8 no terminal (não bloqueante no Windows + Pytest).
- **Mensagem de erro do backend** nem sempre aparece — em alguns navegadores o atributo `required` do HTML5 segura o submit antes que a chamada chegue ao servidor. O passo `uma mensagem de erro é exibida` aceita ambos os caminhos para evitar falsos negativos.

## 8. Reflexão

> *Quando usar BDD?*

Quando a comunicação entre **negócio** e **time técnico** for fonte recorrente de retrabalho. O `.feature` substitui especificações textuais ambíguas por uma especificação **executável**: se passa, está implementado conforme combinado.

> *BDD substitui testes unitários?*

Não. BDD valida **comportamento de ponta a ponta**, geralmente caro. Testes unitários (como os do [PBL 6](aula-09-testes-unitarios-tdd.md)) continuam responsáveis por cobrir regras de negócio isoladas com baixo custo. A **pirâmide de testes** continua válida: muitos unitários, alguns funcionais, poucos E2E/BDD.

> *Onde BDD mais ajudou neste projeto?*

Na cláusula `Cenário: Login com senha incorreta`. A frase em Gherkin é exatamente como um analista de QA descreveria o teste em uma reunião. Não há ambiguidade sobre o que está sendo verificado.

## 9. Relação com Elementos de Competência

- **EC4** — escolhi BDD por ser a técnica adequada para validar **comportamento observável** do usuário, complementando os testes unitários do PBL 6.
- **EC5** — todos os cenários estão automatizados em `pytest-bdd` + `Playwright`, executando contra o sistema em produção.
