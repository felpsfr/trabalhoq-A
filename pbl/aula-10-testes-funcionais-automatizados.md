# PBL 7 — Testes Funcionais Automatizados (Local Eats)

> Centro Universitário Senac-RS
> Unidade Curricular: Qualidade de Software
> Prof.: Luciano Zanuz
> **Integrante:** Felipe Ferreira Ribeiro — 782410083

## 1. Objetivo

Automatizar testes funcionais (caixa-preta, *end-to-end*) do sistema **Local Eats** usando **Playwright** + **Pytest**, com aplicação do padrão **Page Object Model (POM)** para separar lógica de UI da lógica de teste.

## 2. Fluxos selecionados

| Fluxo | Justificativa |
|---|---|
| **Login** | Porta de entrada do sistema — sem login não há acesso a Explorar/Favoritos/Pedidos. Alta criticidade. |
| **Home pós-login (Explorar)** | Tela central; lista os restaurantes para descoberta. |
| **Navegação para detalhe do restaurante / Favoritos / Pedidos** | Garante que os principais links do menu funcionam. |

## 3. Ambiente

- **Aplicação sob teste:** <https://local-eats-unisenac.vercel.app/>
- **Credenciais de teste** (placeholder fornecido pelo próprio sistema): `teste@teste.com` / `123`
- **Stack:** Python 3.14, Pytest 9.0, Playwright 1.60 (Chromium headless)
- **Instalação:**
  ```bash
  python -m pip install -r requirements.txt
  python -m playwright install chromium
  python -m pytest tests/e2e -v
  ```

## 4. Arquitetura — Page Object Model

```
tests/e2e/
├── conftest.py                # fixtures de browser/page (Playwright)
├── pages/
│   ├── login_page.py          # POM da tela de login
│   ├── home_page.py           # POM da home pós-login
│   └── favoritos_page.py      # POM dos Favoritos
├── test_login.py              # 5 cenários de autenticação
└── test_home.py               # 5 cenários de navegação/listagem
```

**Benefícios obtidos pela aplicação do POM:**

1. **Mudanças de UI** ficam isoladas em 1 arquivo. Se o `#loginEmail` virar `#email`, basta editar [tests/e2e/pages/login_page.py](../tests/e2e/pages/login_page.py).
2. **Reuso real**: `login_com_credenciais_validas()` é chamado tanto pelo `test_login_com_credenciais_validas_redireciona_para_home` quanto pela fixture `home` do [test_home.py](../tests/e2e/test_home.py).
3. **Legibilidade dos testes**: `login.deve_mostrar_formulario()` é mais expressivo que três `expect(...)` encadeados.

## 5. Casos de teste implementados (10)

### Fluxo de login — [tests/e2e/test_login.py](../tests/e2e/test_login.py)

| ID | Cenário | Tipo |
|---|---|---|
| CT-E2E-01 | Formulário de login carrega | Happy path |
| CT-E2E-02 | Login com credenciais válidas redireciona para home | Happy path |
| CT-E2E-03 | Login com senha incorreta exibe erro | Erro |
| CT-E2E-04 | Login com email inexistente exibe erro | Erro |
| CT-E2E-05 | Submit vazio é bloqueado pelos campos `required` | Validação |

Exemplo em Gherkin do CT-E2E-02:
```gherkin
Dado que estou na página de login do Local Eats
E que informei o e-mail "teste@teste.com"
E que informei a senha "123"
Quando eu clicar em Entrar
Então sou redirecionado para /static/index.html
E vejo o banner "Descubra sabores incríveis na sua cidade"
E vejo pelo menos um restaurante listado
```

### Fluxo da home — [tests/e2e/test_home.py](../tests/e2e/test_home.py)

| ID | Cenário | Tipo |
|---|---|---|
| CT-E2E-06 | Home carrega após login | Happy path |
| CT-E2E-07 | Home lista pelo menos 1 restaurante | Happy path |
| CT-E2E-08 | Clicar em um card abre `restaurant.html?id=N` | Happy path |
| CT-E2E-09 | Link "Meus Favoritos" navega para `profile.html` | Happy path |
| CT-E2E-10 | Link "Meus Pedidos" navega para `orders.html` | Happy path |

## 6. Geração inicial — Playwright Codegen

O esqueleto inicial dos testes foi gerado via:

```bash
python -m playwright codegen https://local-eats-unisenac.vercel.app/
```

Os passos capturados (`page.goto`, `page.locator('#loginEmail').fill(...)`, etc.) serviram de base, **mas foram refatorados** para o padrão POM antes de virarem testes definitivos.

## 7. Execução e evidências

```bash
$ python -m pytest tests/e2e -v
```

Saída completa em [artefatos/evidencias/pbl-07-pytest-output.txt](../artefatos/evidencias/pbl-07-pytest-output.txt):

```
============================= test session starts =============================
platform win32 -- Python 3.14.0, pytest-9.0.3
configfile: pytest.ini
collected 10 items

tests/e2e/test_home.py .....                       [ 50%]
tests/e2e/test_login.py .....                      [100%]

============================= 10 passed in 36.08s =============================
```

| Métrica | Valor |
|---|---|
| Testes executados | **10** |
| Aprovados | 10 |
| Reprovados | 0 |
| Tempo total | ~36 s |

**Screenshots capturados como evidência visual** ([artefatos/evidencias/](../artefatos/evidencias/)):
- `01_login.png` — formulário de login
- `02_home_pos_login.png` — Explorar com a lista de restaurantes
- `03_detalhe_restaurante.png` — página do restaurante
- `04_favoritos.png` — Meus Favoritos
- `05_pedidos.png` — Meus Pedidos
- `06_login_erro.png` — credenciais inválidas com a mensagem de erro

## 8. Observações e desafios

- **Seletores baseados em texto são frágeis.** Onde possível, usei `getByRole` e `#id` (estáveis); só usei texto na navegação por menu, que é parte da interface estável do sistema.
- **Limpeza de sessão:** o login persiste em cookies/local. Cada teste recebe um `context` novo via `conftest.py`, garantindo isolamento.
- **Espera explícita** (`wait_for_url`) em vez de `sleep`, evitando flakiness.
- **Timeout reduzido para 15s** (`set_default_timeout`) — falha rápido em vez de pendurar a suíte.

## 9. Reflexão

> *Testes automatizados substituem testes manuais?*

Não. Os testes automatizados validam **regressão** com baixo custo, mas não substituem a exploração manual — defeitos como o **D-02** (estado vazio sem orientação) detectado no PBL 5 são percebidos por um humano antes de virarem um caso automatizado. A regra é: cada bug encontrado manualmente deve gerar um teste automatizado para garantir que não volte.

> *O POM compensa o esforço extra?*

Sim. Em **uma única refatoração** do projeto (quando descobri que a URL real era `/static/login.html`, não `/`), só precisei editar `LoginPage.URL` em um lugar. Sem POM, isso teria que ser feito em cada teste.

> *Onde a automação ainda não chega?*

- Validações **visuais** (cores, espaçamento, contraste) precisam de testes específicos (`@axe-core/playwright`, snapshots).
- Validações de **acessibilidade** real (leitor de tela, navegação por teclado) ainda exigem inspeção humana.

## 10. Relação com Elementos de Competência

- **EC4** — projetei os testes selecionando técnicas adequadas (POM para organização, parametrização para reduzir duplicação, separação happy/erro).
- **EC5** — todos os testes são automatizados e executam contra o sistema real em produção.
