# PBL 2 — Diagnóstico de Qualidade · Startup Local Eats

> Entrega da Aula 3 · Disciplina de Qualidade de Software — Senac-RS
> Enunciado original: [../docs/enunciados/pbl-2-papeis-qa.md](../docs/enunciados/pbl-2-papeis-qa.md)

## Integrantes

- Felipe Ferreira Ribeiro - Matrícula: 782410083

## 1. Diagnóstico da Situação Atual

A startup Local Eats está em fase inicial, focada em entregar funcionalidades rapidamente para atender à demanda da associação de comerciantes. O cenário apresentado — erros ao finalizar pedidos, pedidos duplicados, funcionalidades chegando à produção com defeitos e ausência de responsável claro pela qualidade — é **sintomático de startups jovens**, em que a qualidade acaba sendo tratada como consequência, e não como parte do processo.

### 1.1 Papéis que provavelmente existem hoje

Com base no cenário e em configurações típicas de startups em estágio inicial, provavelmente existem:

- **Desenvolvedor(es) full-stack** — escrevem, testam pontualmente e publicam o próprio código.
- **Gerente de Produto / Product Owner** — prioriza funcionalidades e representa os interesses da associação de comerciantes.
- **Analista de Sistemas / UX informal** — alguém (eventualmente o próprio dev ou o PO) pensando nos fluxos.
- **Fundador(es) / liderança técnica** — atuando como arquiteto, DevOps e gerente simultaneamente.
- **Suporte** — recebe reclamações dos usuários e repassa para os desenvolvedores.

Não há evidência de um papel dedicado de **QA / Analista de Qualidade**.

### 1.2 Responsável pela qualidade atualmente

Na prática, a qualidade está **difusa**: desenvolvedores testam o próprio código antes do deploy, o PO eventualmente valida uma funcionalidade antes do release e usuários acabam atuando como “testadores involuntários” em produção. O resultado é previsível: **ninguém tem a qualidade como responsabilidade primária**, e defeitos escapam.

### 1.3 Problemas causados pela falta de clareza nas responsabilidades

- **Defeitos recorrentes em produção** porque não há uma etapa de validação estruturada antes do release (explica pedidos duplicados e erros de finalização).
- **Falta de rastreabilidade de defeitos** — bugs reportados pelo suporte podem se perder ou ser reabertos múltiplas vezes sem registro central.
- **Retrabalho**: desenvolvedores interrompem novas entregas para corrigir problemas que poderiam ter sido encontrados antes.
- **Ausência de critérios objetivos de qualidade** (*Definition of Done*): o que é “pronto” muda de pessoa para pessoa.
- **Desgaste do relacionamento com a associação de comerciantes**, que percebe o produto instável.
- **Risco de silenciar sintomas**, já que quem desenvolveu também valida — tende a enxergar o próprio código como correto.

### 1.4 Responsabilidade individual vs. compartilhada

A qualidade **não pode ser responsabilidade de uma única pessoa**. Ter um papel de QA é importante, pois concentra conhecimento específico (técnicas de teste, gestão de defeitos, planejamento), mas a **responsabilidade pela qualidade precisa ser compartilhada por todo o time**: o desenvolvedor escreve código testável e testa o próprio trabalho; o PO define critérios de aceite; o DevOps garante a estabilidade do pipeline; o QA lidera práticas e atua em cenários que exigem olhar crítico. Em um contexto como o da Local Eats, onde os defeitos atingem diretamente os comerciantes, esse modelo compartilhado é especialmente necessário.

## 2. Papéis da Equipe (proposta)

| Papel                                   | Principais responsabilidades                                                                 | Relação com a qualidade |
|-----------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------|
| **Desenvolvedor(a) Full-Stack**         | Implementar funcionalidades; escrever testes unitários e de integração; revisar PRs; corrigir bugs. | Produz código testável, aplica *clean code*, participa do *code review*, escreve testes automatizados. |
| **QA / Analista de Qualidade**          | Planejar e executar testes manuais e exploratórios; registrar e acompanhar defeitos; definir critérios de aceite junto ao PO; apoiar automação. | Dono(a) das práticas de QA e guardião(ã) da qualidade do produto entregue. |
| **Analista de Sistemas / Analista de Negócio** | Levantar e detalhar requisitos; traduzir necessidades da associação em histórias de usuário; validar regras de negócio. | Garante a qualidade **a montante**: requisitos claros diminuem defeitos antes de existirem. |
| **DevOps / SRE**                         | Automatizar CI/CD; monitorar produção; configurar alertas; gerenciar ambientes. | Garante estabilidade do pipeline, feedback rápido (builds/testes automáticos) e observabilidade em produção. |
| **Product Owner (PO)**                   | Priorizar backlog; definir *Definition of Done*; validar entregas junto aos stakeholders. | Conecta qualidade do produto com valor de negócio; aprova/rejeita com base em critérios objetivos. |
| **Designer UX/UI** (mesmo que fracionário) | Prototipar fluxos e telas; conduzir testes de usabilidade; definir padrões visuais. | Reduz defeitos de usabilidade e retrabalho, atacando sintomas como “telas confusas” e “dificuldade para concluir ações”. |

## 3. Responsabilidades relacionadas à qualidade

| Atividade de qualidade                                  | Responsável principal | Apoio                   |
|---------------------------------------------------------|-----------------------|-------------------------|
| Detalhar requisitos e critérios de aceite               | Analista de Sistemas + PO | QA (revisa testabilidade) |
| Revisar histórias antes do desenvolvimento (*refinement*) | PO                    | QA, Dev, Analista        |
| Escrever testes unitários                                | Desenvolvedor          | QA (revisão de cobertura) |
| Revisar Pull Requests (*code review*)                    | Desenvolvedor          | Tech Lead / par          |
| Projetar e executar testes manuais/exploratórios         | QA                    | Dev                      |
| Automatizar testes de integração e E2E                   | QA + Dev              | DevOps                   |
| Registrar e acompanhar defeitos                          | QA                    | Time todo (todos podem abrir bug) |
| Validar funcionalidade antes do release                  | QA + PO               | Dev                      |
| Configurar pipeline CI/CD com gates de qualidade         | DevOps                | Dev, QA                  |
| Monitorar métricas e alertas em produção                 | DevOps / SRE          | QA                       |
| Conduzir retrospectivas focadas em qualidade             | Time todo             | Facilitador (Scrum Master/QA) |

## 4. Práticas de QA Recomendadas

1. **Definition of Done (DoD) compartilhada** — uma funcionalidade só é “pronta” quando: tem testes automatizados passando, foi revisada por outra pessoa (*code review*), foi validada pelo QA e aceita pelo PO. Isso cria um critério objetivo e impede releases com defeitos óbvios.
2. **Registro padronizado de defeitos** — template obrigatório com passos para reproduzir, resultado obtido, resultado esperado, severidade, ambiente e screenshots/vídeos. Ferramenta única (Jira, Linear, GitHub Issues) para evitar perdas no fluxo do suporte.
3. **Testes exploratórios semanais** — sessões curtas (60-90 min) com foco em uma área do produto, registrando achados em *session notes*. Excelente complemento aos testes baseados em requisito, especialmente para encontrar problemas de UX (o que claramente aflige o Local Eats).
4. **Pipeline de CI com *gates* automáticos** — cada PR executa lint, testes unitários e testes de integração; nenhum merge é permitido sem build verde. Introdução gradual de testes E2E para os fluxos críticos (cadastro, pedido).
5. **Triagem diária de bugs e *bug bash* antes do release** — reunião curta para priorizar defeitos abertos e sessão conjunta de exploração antes de releases importantes (especialmente o evento gastronômico da associação).

## 5. Anúncios de Contratação

### 5.1 Vaga 1 — Analista de Qualidade de Software (QA) Pleno

**Empresa:** Local Eats
**Local:** Porto Alegre — RS
**Modelo:** Híbrido (2 dias presenciais no escritório)

**Sobre a vaga**

A Local Eats está buscando um(a) Analista de Qualidade Pleno(a) para estruturar nossa prática de QA. Você vai atuar diretamente com desenvolvedores, PO e DevOps para definir critérios de qualidade, conduzir testes manuais e exploratórios, liderar a construção de uma suíte de testes automatizados e garantir que os pedidos feitos na nossa plataforma cheguem corretamente aos restaurantes parceiros. É uma oportunidade para criar processo do zero em um produto com impacto direto no comércio local.

**Principais responsabilidades**

- Planejar e executar testes funcionais e exploratórios das funcionalidades web e mobile.
- Especificar casos de teste claros e com boa cobertura de cenários de sucesso e erro.
- Registrar e acompanhar defeitos, priorizando com base em impacto.
- Apoiar desenvolvedores na escrita de testes unitários e de integração.
- Automatizar testes E2E de fluxos críticos (Cypress, Playwright ou similar).
- Participar do refinamento das histórias, garantindo critérios de aceite testáveis.
- Contribuir para a *Definition of Done* e para o pipeline de CI/CD.

**Requisitos obrigatórios**

- Experiência com testes manuais de aplicações web e mobile.
- Capacidade de escrever e executar casos de teste estruturados (Gherkin é um diferencial).
- Domínio de ferramentas de gestão de defeitos (Jira, Linear, Azure DevOps, GitHub Issues).
- Conhecimento de API REST e uso de ferramentas como Postman/Insomnia.
- Noções de Git e fluxos de branches.
- Boa comunicação escrita e trabalho em equipe.

**Requisitos desejáveis**

- Experiência com automação de testes (Cypress, Playwright, Selenium).
- Conhecimento de testes de performance (k6, JMeter) e contrato (Pact).
- Experiência em startups ou ambientes de produto.
- Familiaridade com metodologias ágeis (Scrum, Kanban).

**Certificações desejáveis**

- ISTQB CTFL (*Certified Tester Foundation Level*)
- CTFL-AT (*Agile Tester*)

### 5.2 Vaga 2 — Pessoa Desenvolvedora Full-Stack

**Empresa:** Local Eats
**Local:** Porto Alegre — RS
**Modelo:** Híbrido (2 dias presenciais no escritório)

**Sobre a vaga**

Buscamos um(a) desenvolvedor(a) full-stack que **pense em qualidade desde a primeira linha**. Você vai evoluir a plataforma Local Eats (web + mobile), corrigir a dívida técnica acumulada na primeira versão e contribuir para transformar nosso pipeline em algo que entregue valor com frequência e confiança. Se você gosta de escrever testes e usar código legível como ferramenta de comunicação, vai se sentir em casa.

**Principais responsabilidades**

- Implementar e evoluir funcionalidades no back-end e no front-end da plataforma.
- Escrever testes unitários e de integração para cada entrega.
- Participar ativamente de *code reviews*.
- Colaborar com QA e PO na definição de critérios de aceite.
- Contribuir para o pipeline de CI/CD e para as práticas de monitoramento.
- Corrigir bugs com análise de causa-raiz (não apenas sintoma).

**Requisitos obrigatórios**

- Experiência com JavaScript/TypeScript, Node.js e algum framework front-end (React, Vue, Angular).
- Prática com bancos relacionais (PostgreSQL/MySQL) e APIs REST.
- Experiência escrevendo testes automatizados (Jest, Vitest, Mocha).
- Conhecimento sólido de Git e fluxos colaborativos (*pull requests*, revisão de código).
- Inglês técnico suficiente para leitura de documentação.

**Requisitos desejáveis**

- Experiência com React Native ou Flutter.
- Conhecimento de Docker, pipelines CI/CD (GitHub Actions, GitLab CI).
- Noções de arquitetura limpa, SOLID e TDD.
- Experiência com observabilidade (logs, métricas, tracing).

**Cursos / trilhas relevantes**

- Trilhas de engenharia de qualidade (Rocketseat, Alura, Coursera — *Software Testing and Automation*).
- Fundamentos de Clean Code e Refactoring (livros do Robert C. Martin e Martin Fowler).

## Referências

- ISTQB Foundation Level Syllabus
- Material de aula — Prof. Luciano Zanuz
- *Agile Testing*, Lisa Crispin & Janet Gregory (referência para QA em times ágeis)
