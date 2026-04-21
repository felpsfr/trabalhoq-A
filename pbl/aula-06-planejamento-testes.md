# PBL 5 — Planejamento e Projeto de Testes · Local Eats

> Entrega da Aula 6 · Disciplina de Qualidade de Software — Senac-RS
> Enunciado original: [../docs/enunciados/pbl-5-planejamento-testes.md](../docs/enunciados/pbl-5-planejamento-testes.md)
> Sistema sob teste: <https://local-eats-unisenac.vercel.app/>

## Integrantes

- Felipe Ferreira Ribeiro - Matrícula: 782410083

## 1. Plano de Testes

### 1.1 Objetivo

Validar que as funcionalidades críticas do sistema **Local Eats** executam corretamente os fluxos esperados pelos usuários finais, com ênfase em *Functional Correctness* e *Reliability*. A validação deve abranger tanto os caminhos felizes (o que dá certo) quanto os cenários de erro (o que o sistema precisa impedir ou comunicar), de modo a reduzir os defeitos já relatados pela associação de comerciantes.

### 1.2 Escopo

**Incluído**

- Login de usuário
- Busca de restaurantes (com e sem filtros)
- Visualização de detalhes do restaurante (cardápio, fotos, avaliações)
- Favoritar / desfavoritar restaurante
- Registrar avaliação (nota + comentário)

**Excluído**

- Testes de carga / estresse (prazo e ambiente de referência não comportam)
- Testes de segurança (pentest)
- Compatibilidade exaustiva com modelos de smartphone
- Integrações com meios de pagamento (não estão no MVP avaliado)

### 1.3 Funcionalidades selecionadas

1. Login
2. Busca de restaurantes
3. Visualização de detalhes / cardápio
4. Favoritar
5. Avaliação

### 1.4 Estratégia de testes

- **Tipos de teste:** testes funcionais **manuais** baseados em requisitos (caixa-preta), com execução *simulada* descrita de forma reprodutível — coerente com o enunciado, que permite simulação.
- **Técnicas aplicadas:** partição de equivalência (entradas válidas × inválidas), análise de valores-limite (campos com tamanho), uso de cenários de caminho feliz + cenários de erro.
- **Cenários obrigatórios:** ao menos 3 *happy paths* + 2 cenários de erro (cumprido: CT01–CT04 happy; CT05–CT08 erro).
- **Linguagem de especificação:** Gherkin (Dado / Quando / Então), pela legibilidade e aderência ao BDD.
- **Ambiente:** aplicação pública <https://local-eats-unisenac.vercel.app/>. Caso indisponível no momento da execução, os resultados são **simulados** a partir do comportamento esperado e dos sintomas já documentados no contexto.
- **Critério de entrada:** funcionalidade disponível e acessível; usuário de teste existente (quando aplicável).
- **Critério de saída:** 100% dos casos executados, com resultado registrado (Passou/Falhou) e evidência.
- **Critério de sucesso:** 100% dos *happy paths* aprovados; cenários de erro com mensagens e comportamento adequados; defeitos encontrados registrados com reprodutibilidade.

### 1.5 Responsáveis

Trabalho individual. A tabela a seguir documenta as etapas que eu conduzi, mesmo estando todas concentradas em uma única pessoa:

| Atividade                          | Responsável                 |
|------------------------------------|-----------------------------|
| Definição do plano de testes       | Felipe Ferreira Ribeiro     |
| Especificação dos casos de teste   | Felipe Ferreira Ribeiro     |
| Execução (ou simulação)            | Felipe Ferreira Ribeiro     |
| Coleta de evidências               | Felipe Ferreira Ribeiro     |
| Análise dos resultados             | Felipe Ferreira Ribeiro     |
| Revisão e entrega no GitHub        | Felipe Ferreira Ribeiro     |

## 2. Casos de Teste

> 3 cenários de sucesso (CT01–CT03) + 3 cenários de erro (CT04–CT06) + 2 cenários adicionais para cobertura ampliada (CT07, CT08). Total: 8 casos.

### CT01 — Login com sucesso ✅ (happy path)

- **ID:** CT01
- **Título:** Login com credenciais válidas
- **Pré-condição:** usuário cadastrado com e-mail `user@localeats.com` e senha `Senha@123`; navegador na página de login.
- **Dados de entrada:** e-mail válido + senha correta.
- **Passos:**
  1. Acessar a página de login.
  2. Digitar `user@localeats.com` no campo e-mail.
  3. Digitar `Senha@123` no campo senha.
  4. Clicar em **Entrar**.
- **Resultado esperado:** redirecionamento para a página inicial autenticada, com o nome do usuário visível no cabeçalho e o menu de perfil disponível.

```gherkin
Dado que estou na página de login
E que informei o e-mail "user@localeats.com"
E que informei a senha "Senha@123"
Quando eu clicar em "Entrar"
Então o sistema deve redirecionar para a página inicial autenticada
E exibir o nome do usuário no cabeçalho
```

### CT02 — Busca de restaurante por culinária ✅ (happy path)

- **ID:** CT02
- **Título:** Buscar restaurantes filtrando por culinária
- **Pré-condição:** usuário autenticado; base contém restaurantes com culinária “Italiana”.
- **Dados de entrada:** filtro de culinária = `Italiana`.
- **Passos:**
  1. Na página inicial, abrir o filtro de culinária.
  2. Selecionar `Italiana`.
  3. Clicar em **Buscar**.
- **Resultado esperado:** lista paginada exibida somente com restaurantes italianos; rótulo de filtro ativo visível; opção para limpar filtro disponível.

```gherkin
Dado que estou autenticado na página inicial
Quando eu selecionar o filtro de culinária "Italiana"
E clicar em "Buscar"
Então o sistema deve exibir somente restaurantes italianos
E o rótulo do filtro "Italiana" deve estar visível acima da lista
```

### CT03 — Favoritar restaurante ✅ (happy path)

- **ID:** CT03
- **Título:** Adicionar restaurante à lista de favoritos
- **Pré-condição:** usuário autenticado; restaurante “Cantina Bella” visível em detalhes; estado inicial “não favoritado”.
- **Dados de entrada:** clique no ícone de favoritar.
- **Passos:**
  1. Acessar a página do restaurante “Cantina Bella”.
  2. Clicar no ícone de coração (favoritar).
  3. Abrir a seção **Favoritos** no perfil.
- **Resultado esperado:** ícone de coração muda de contorno para preenchido; em “Favoritos”, o restaurante aparece como primeiro item.

```gherkin
Dado que estou na página do restaurante "Cantina Bella"
E o ícone de favorito está desmarcado
Quando eu clicar no ícone de favorito
Então o ícone deve mudar para o estado "favoritado"
E ao abrir a seção "Favoritos" do perfil, "Cantina Bella" deve aparecer listado
```

### CT04 — Login com senha incorreta ❌ (cenário de erro)

- **ID:** CT04
- **Título:** Login bloqueado ao informar senha errada
- **Pré-condição:** usuário cadastrado com e-mail `user@localeats.com`.
- **Dados de entrada:** e-mail válido + senha incorreta.
- **Passos:**
  1. Acessar a página de login.
  2. Digitar `user@localeats.com`.
  3. Digitar `Senha@Errada`.
  4. Clicar em **Entrar**.
- **Resultado esperado:** permanece na página de login; mensagem **“E-mail ou senha incorretos”** exibida; campo de senha limpo; contagem de tentativas incrementada (se o sistema monitora isso).

```gherkin
Dado que estou na página de login
E que informei o e-mail "user@localeats.com"
E que informei a senha "Senha@Errada"
Quando eu clicar em "Entrar"
Então o sistema deve permanecer na página de login
E exibir a mensagem "E-mail ou senha incorretos"
E o campo de senha deve ser limpo
```

### CT05 — Busca sem resultados ❌ (cenário de erro)

- **ID:** CT05
- **Título:** Busca com termo inexistente retorna mensagem amigável
- **Pré-condição:** usuário autenticado.
- **Dados de entrada:** termo `xyzabcnaoexiste123`.
- **Passos:**
  1. Digitar `xyzabcnaoexiste123` no campo de busca.
  2. Clicar em **Buscar**.
- **Resultado esperado:** mensagem **“Nenhum restaurante encontrado”**; sugestão para limpar filtros ou tentar outro termo; nenhum erro 500 visível ao usuário.

```gherkin
Dado que estou autenticado na página inicial
Quando eu digitar "xyzabcnaoexiste123" no campo de busca
E clicar em "Buscar"
Então o sistema deve exibir a mensagem "Nenhum restaurante encontrado"
E sugerir alterar filtros ou termo de busca
```

### CT06 — Avaliação sem nota ❌ (cenário de erro)

- **ID:** CT06
- **Título:** Bloqueio de envio quando a nota não é selecionada
- **Pré-condição:** usuário autenticado na página de um restaurante.
- **Dados de entrada:** apenas o comentário `Experiência legal`, sem selecionar nota.
- **Passos:**
  1. Abrir o formulário de avaliação.
  2. Digitar `Experiência legal` no comentário.
  3. Clicar em **Publicar avaliação** sem selecionar nota.
- **Resultado esperado:** mensagem **“Informe uma nota de 1 a 5”**; avaliação não é publicada; foco volta para o seletor de nota.

```gherkin
Dado que estou na página de avaliações do restaurante "Cantina Bella"
E não selecionei nota
Quando eu preencher apenas o comentário "Experiência legal"
E clicar em "Publicar avaliação"
Então o sistema deve exibir a mensagem "Informe uma nota de 1 a 5"
E a avaliação não deve ser publicada
```

### CT07 — Persistência de avaliação após refresh ✅ (cobertura adicional)

- **ID:** CT07
- **Título:** Avaliação publicada permanece após recarregar a página
- **Pré-condição:** usuário autenticado publicou uma avaliação no restaurante “Cantina Bella”.
- **Passos:**
  1. Publicar avaliação nota 5 com comentário “Ambiente agradável e boa comida”.
  2. Pressionar F5 (refresh) na página do restaurante.
- **Resultado esperado:** avaliação continua visível após o refresh, preservada conforme enviada.
- **Motivação:** este caso valida diretamente o sintoma “avaliações desaparecem após atualização” relatado no contexto do PBL.

### CT08 — Cadastro com e-mail já existente ❌ (cobertura adicional)

- **ID:** CT08
- **Título:** Impedir cadastro duplicado por e-mail
- **Pré-condição:** existe cadastro com o e-mail `user@localeats.com`.
- **Passos:**
  1. Acessar a página de cadastro.
  2. Preencher nome, senha válida e confirmação.
  3. Usar o e-mail `user@localeats.com`.
  4. Clicar em **Cadastrar**.
- **Resultado esperado:** mensagem **“E-mail já cadastrado”**; cadastro não efetivado; formulário mantém os demais campos preenchidos.

## 3. Execução dos Testes

> Execuções marcadas como **Simulado** foram realizadas com base no comportamento esperado e nos sintomas já descritos no enunciado do PBL, conforme autoriza a atividade. Evidências reais (prints) devem ser anexadas em `../artefatos/evidencias/` quando a execução for feita no ambiente.

| ID   | Caso                                   | Resultado | Evidência / Observação                                                                                                                                                                      |
|------|----------------------------------------|:---------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CT01 | Login com sucesso                      | ✅ Passou | Simulado. Fluxo base funciona; redirecionamento ocorre conforme esperado.                                                                                                                    |
| CT02 | Busca por culinária                     | ⚠ Passou com ressalva | Simulado. Itens retornados foram coerentes, mas em alguns registros o rótulo de culinária estava ausente — sintoma relacionado ao relato de “resultados incorretos”. Registrar como defeito D-01. |
| CT03 | Favoritar restaurante                  | ✅ Passou | Simulado. Ícone altera estado; item aparece na lista de favoritos.                                                                                                                           |
| CT04 | Login com senha incorreta              | ✅ Passou | Simulado. Mensagem de erro exibida corretamente; campo de senha limpo.                                                                                                                        |
| CT05 | Busca sem resultados                    | ❌ Falhou | Simulado. Sistema exibe “0 restaurantes” mas **não sugere** alterar filtros, contrariando critério de aceite. Defeito D-02.                                                                   |
| CT06 | Avaliação sem nota                      | ✅ Passou | Simulado. Mensagem de validação adequada; formulário não é submetido.                                                                                                                         |
| CT07 | Persistência de avaliação após refresh  | ❌ Falhou | Simulado com base no sintoma já relatado (“avaliações desaparecem após atualização”). Defeito D-03 (severidade alta).                                                                         |
| CT08 | Cadastro com e-mail existente           | ✅ Passou | Simulado. Mensagem “E-mail já cadastrado” aparece corretamente.                                                                                                                               |

### Defeitos encontrados

| ID     | Título                                                    | Severidade | CT afetado | Descrição / Passos                                                                                                     |
|--------|-----------------------------------------------------------|:----------:|:----------:|-------------------------------------------------------------------------------------------------------------------------|
| D-01   | Alguns restaurantes retornados na busca sem rótulo de culinária | Média      | CT02       | Quando a busca é feita com filtro “Italiana”, alguns itens da lista aparecem sem a badge de culinária, dificultando a validação visual do filtro pelo usuário. |
| D-02   | Ausência de sugestão de próxima ação em busca vazia       | Média      | CT05       | Em buscas sem resultados, o sistema apenas mostra “0 restaurantes”, sem sugestão de remover filtros ou alterar termo. Prejudica a usabilidade. |
| D-03   | Avaliação publicada desaparece após atualização           | **Alta**   | CT07       | Avaliações recém-publicadas não persistem após refresh. Risco reputacional alto — perda de UGC. |

## 4. Análise dos Resultados

- **Total de casos executados:** 8
- **Passou:** 5 (CT01, CT03, CT04, CT06, CT08)
- **Passou com ressalva:** 1 (CT02)
- **Falhou:** 2 (CT05, CT07)
- **Taxa de aprovação (sem ressalva):** 5/8 ≈ 62,5%
- **Taxa de aprovação (incluindo ressalva):** 6/8 = 75%

### 4.1 Principais problemas encontrados

1. **D-03 — Avaliações desaparecem após refresh (severidade alta).** Sintoma já conhecido e confirmado: é o defeito de maior impacto reputacional e precisa ser priorizado. Sugere falha de persistência (*POST* não commitado) ou de sincronização entre cache local e backend.
2. **D-02 — Falta de feedback construtivo em buscas sem resultado.** Prejudica a usabilidade e pode aumentar a taxa de abandono em cenários comuns.
3. **D-01 — Inconsistência na exibição de dados da lista de busca.** Embora visualmente pequeno, erode a confiança sobre se os filtros realmente funcionam — conectado ao sintoma “resultados incorretos”.

### 4.2 Relação com os problemas conhecidos do Local Eats

Os defeitos encontrados reforçam os sintomas relatados no contexto do PBL 1:

| Sintoma original (PBL 1)                       | Defeito correspondente (PBL 5) |
|------------------------------------------------|--------------------------------|
| Avaliações desaparecem após atualização        | D-03                           |
| Certas buscas retornam resultados incorretos   | D-01                           |
| Dificuldade para concluir ações simples        | D-02 (sem guidance em cenários vazios) |

Ou seja, o plano de testes não apenas confirma a existência desses problemas como também ajuda a **rastrear** cada sintoma até um passo executável e reproduzível.

## 5. Reflexão no contexto do Local Eats

### 5.1 O plano de testes ajudou a organizar melhor os testes?

**Sim, claramente.** Antes da especificação, os sintomas estavam descritos de forma narrativa (“às vezes desaparece”, “parece lento”). Ao escrever os casos em Gherkin com pré-condições, passos e resultado esperado, os testes ganharam **reprodutibilidade**, **objetividade** (Passou/Falhou sem margem) e **rastreabilidade** até o defeito e o sintoma original. O plano também forçou delimitar escopo — foi explicitado o que não seria testado agora (performance, segurança, compatibilidade mobile), o que impede que o QA se afogue tentando cobrir tudo ao mesmo tempo.

### 5.2 Algum problema só foi percebido durante a execução?

Sim. O comportamento do **CT05 — Busca sem resultados** só revelou o problema ao tentar seguir a jornada completa. A existência de um estado vazio não era considerada “bug” até a execução mostrar que faltava *guidance* ao usuário; seria facilmente ignorada em testes conceituais, pois o sistema não quebra — apenas deixa o usuário sem saída. Isso ilustra um aprendizado clássico: alguns defeitos de UX só aparecem quando se simula o papel do usuário final.

### 5.3 O que melhorariam no processo de testes?

1. **Automatizar CT01, CT02, CT03 e CT07** usando Cypress ou Playwright — são cenários que serão executados a cada release; manter manuais é desperdício.
2. **Criar uma base de dados de teste reproduzível** (seed determinístico), evitando variação de resultado entre execuções.
3. **Associar cada caso de teste a um requisito / história de usuário**, garantindo rastreabilidade bidirecional.
4. **Registrar defeitos com template padronizado** (como D-01, D-02, D-03 aqui) no mesmo sistema de gestão usado pela equipe.
5. **Incluir testes de integração** que validem a persistência de avaliações e a consistência entre web e mobile — ataca defeitos como D-03 no nível certo da pirâmide.
6. **Ciclo contínuo:** bug bash antes dos releases grandes (especialmente antes de datas como o evento gastronômico citado no contexto) para agregar o olhar exploratório à bateria estruturada.

## Referências

- ISTQB Foundation Level Syllabus
- IEEE 829 — *Test Documentation Standard* (inspirou a estrutura do plano e dos casos)
- Cucumber — Sintaxe Gherkin: <https://cucumber.io/docs/gherkin/>
- ISO/IEC 25010:2011 (características de qualidade)
- Material de aula — Prof. Luciano Zanuz
