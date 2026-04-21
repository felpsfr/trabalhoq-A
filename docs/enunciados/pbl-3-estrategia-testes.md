# PBL 3 — Estratégia Inicial de Testes

> Centro Universitário Senac-RS
> ADS - Análise e Desenvolvimento de Sistemas / SPI - Sistemas para Internet
> Unidade Curricular: Qualidade de Software
> Prof.: Luciano Zanuz

## Atividade PBL — Aula 4 · Estratégia Inicial de Testes — LocalEats

### Contexto

Vocês fazem parte da equipe de Qualidade de Software de uma startup responsável pela plataforma **LocalEats**, desenvolvida para conectar moradores e turistas a restaurantes independentes da cidade.

O sistema possui versão web e aplicativo mobile e permite que os usuários:

- Busquem restaurantes por tipo de culinária, localização e faixa de preço
- Visualizem cardápios, fotos e avaliações
- Salvem locais favoritos
- Recebam recomendações personalizadas
- Compartilhem experiências

Devido ao prazo de um grande evento gastronômico, a primeira versão do sistema foi desenvolvida rapidamente e colocada em produção. Após o lançamento, começaram a surgir diversos problemas, como:

- Lentidão em horários de pico
- Telas confusas e pouco intuitivas
- Resultados incorretos nas buscas
- Falhas em determinados smartphones
- Dificuldade para concluir ações simples
- Avaliações que desaparecem após atualização
- Inconsistências entre versão web e mobile

A associação de comerciantes está preocupada com a reputação da plataforma e solicitou uma avaliação técnica da qualidade do sistema.

### Objetivo da Atividade

Definir uma **estratégia inicial de testes**, considerando:

- Níveis de teste
- Prioridade baseada em risco
- Uso da pirâmide de testes
- Possibilidade de testes em produção

> ⚠ Importante: não é necessário escrever casos de teste nesta atividade. O foco é **estratégia, não execução**.

> 👉 Pensem como uma equipe de QA decidindo: *“O que testar primeiro, onde testar e por quê?”*

### Tarefas

Elaborem um documento contendo:

**1. Funcionalidades principais.** Listem de 4 a 6 funcionalidades do sistema.

**2. Níveis de teste.** Para cada funcionalidade, indiquem:

- Teste unitário: o que seria testado nessa camada?
- Teste de integração: o que conecta com o quê?
- Teste de sistema: qual fluxo completo?
- Teste de aceitação: o usuário consegue fazer o quê?

> 👉 Não detalhar *como* testar, apenas indicar *onde* e *por quê*.

**3. Prioridades e riscos.**

- Quais funcionalidades são mais críticas?
- Onde um erro causaria maior impacto?

> 👉 Justifiquem.

**4. Pirâmide de testes.**

- Onde concentrar maior quantidade de testes?
- Onde usar menos testes?

> 👉 Justifiquem com base em custo, risco e eficiência.

**5. Testes em produção.**

- O sistema deveria usar testes em produção?
- Em quais situações?

> 👉 Justifiquem.

### Entregável

- **Formato:** arquivo Markdown (`.md`)
- **Entrega:** repositório do grupo no GitHub — `/pbl/aula-04-estrategia-inicial-testes.md`
- Trabalho individual ou em grupo (até 4 integrantes)
- Modelo de referência: <https://github.com/lucianozanuz/pbl-qualidade-software-2026-1/blob/main/pbl/aula-04-estrategia-inicial-testes.md>

### Avaliação (Rubrica — Unisenac-RS)

**D — Não atingiu as competências mínimas**
Não identifica corretamente funcionalidades do sistema; não compreende os níveis de teste; não apresenta análise de risco; respostas superficiais ou incoerentes; ausência de justificativas.

**C — Atingiu parcialmente as competências**
Identifica algumas funcionalidades corretamente; apresenta níveis de teste, mas com erros ou superficialidade; análise de risco pouco desenvolvida; justificativas genéricas ou incompletas.

**B — Atingiu plenamente as competências**
Identifica corretamente as funcionalidades principais; classifica adequadamente os níveis de teste; apresenta análise de risco coerente; aplica corretamente a pirâmide de testes; justifica suas decisões de forma clara.

**A — Atingiu as competências com excelência**
Apresenta visão clara e estruturada do sistema; identifica corretamente prioridades com base em risco e impacto; aplica a pirâmide de testes de forma estratégica; relaciona conceitos com os problemas reais do sistema; propõe uso consciente de testes em produção; justificativas bem elaboradas e com pensamento crítico.

### Dica final

Para obter conceito A, vocês devem:

- Ir além da descrição → **explicar decisões**
- Conectar com os problemas reais do sistema
- Demonstrar pensamento crítico e estratégico
