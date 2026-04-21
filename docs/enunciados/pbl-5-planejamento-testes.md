# PBL 5 — Planejamento e Projeto de Testes

> Centro Universitário Senac-RS
> ADS - Análise e Desenvolvimento de Sistemas / SPI - Sistemas para Internet
> Unidade Curricular: Qualidade de Software
> Prof.: Luciano Zanuz

## 🧩 Atividade PBL — Aula 6 · Planejamento e Execução de Testes — LocalEats

### 📌 Contexto

Após compreender diferentes perspectivas de testes (caixa-preta e caixa-branca), a equipe de Qualidade do sistema **LocalEats** precisa dar um próximo passo importante:

> 👉 **Organizar e executar testes de forma estruturada e profissional.**

Até agora, os testes eram pensados de forma mais conceitual. Agora, o desafio é transformar esse pensamento em artefatos reais de QA.

O sistema ainda apresenta problemas como:

- Funcionalidades inconsistentes
- Comportamentos inesperados
- Falhas em cenários específicos
- Dificuldade em reproduzir erros

A equipe precisa garantir que: *“Os testes sejam planejados, documentados e executados de forma controlada.”*

👉 Link para o sistema LocalEats: <https://local-eats-unisenac.vercel.app/>

### 🎯 Objetivo da Atividade

Aplicar, de forma prática e estruturada:

- Planejamento de testes
- Especificação de casos de teste
- Execução de testes e análise de resultados

> ⚠️ Importante: não é necessário implementar código. Foco em organização, clareza e raciocínio. Utilizar o contexto do sistema LocalEats. Simular execuções, caso o sistema não esteja implementado.

### 📝 Tarefas

Elaborem um documento contendo:

#### 🔹 1. Plano de Testes

Criem um plano de testes simplificado para o sistema. Descrever:

- **Objetivo** — O que vocês pretendem validar?
- **Escopo** — O que será testado? O que **não** será testado?
- **Funcionalidades selecionadas** — Ex.: login, busca, pedido, avaliação
- **Estratégia de testes** — Tipos de teste utilizados (funcional, etc.); abordagem adotada
- **Responsáveis** — Quem faz o quê na equipe

#### 🔹 2. Casos de Teste

Criar **mínimo de 5 casos de teste**. Cada caso deve conter:

- ID
- Título
- Pré-condição
- Passos
- Dados de entrada (se aplicável)
- Resultado esperado

Incluir obrigatoriamente:

- Pelo menos **3 cenários de sucesso** (*happy path*)
- Pelo menos **2 cenários de erro**

Exemplos de casos de teste descritos na linguagem **Gherkin** para a aplicação web <https://www.saucedemo.com/>:

```gherkin
CT01 - Login com sucesso
Dado que estou na página de login
E que informei o username standard_user
E que informei o password secret_sauce
Quando eu clicar em Login
Então o sistema apresenta a página contendo a lista de produtos disponíveis para compra

CT02 - Login sem sucesso
Dado que estou na página de login
E que informei o username standard_user
E que informei o password secret_saucee
Quando eu clicar em Login
Então o sistema continua na página de login e apresenta a mensagem
"Epic sadface: Username and password do not match any user in this service"
abaixo do campo password, em um quadro na cor vermelha e com a fonte na cor branca
```

#### 🔹 3. Execução dos Testes

Executar (ou simular) os testes definidos. Para cada caso:

- Informar Resultado (**Passou / Falhou**)
- Registrar Evidência (descrição ou print)

#### 🔹 4. Análise dos Resultados

Responder:

- Quantos testes foram executados?
- Quantos passaram? Quantos falharam?
- Quais os principais problemas encontrados?

#### 🔹 5. Reflexão no contexto do LocalEats

Responder:

- O plano de testes ajudou a organizar melhor os testes?
- Algum problema só foi percebido durante a execução?
- O que melhorariam no processo de testes?

### 📦 Entregável

- **Formato:** arquivo Markdown (`.md`)
- **Entrega:** repositório do grupo no GitHub — `/pbl/aula-06-planejamento-testes.md`
- Trabalho individual ou em grupo (até 4 integrantes)
- Modelo de referência: <https://github.com/lucianozanuz/pbl-qualidade-software-2026-1/blob/main/pbl/aula-06-planejamento-testes.md>

### 📊 Avaliação (Rubrica — Unisenac-RS)

**🔴 D — Não atingiu as competências mínimas**
Não apresenta plano de testes estruturado; casos de teste ausentes ou mal definidos; não executa os testes; não registra resultados ou evidências.

**🟡 C — Atingiu parcialmente as competências**
Plano de testes superficial; casos de teste pouco detalhados; execução incompleta ou pouco clara; evidências insuficientes.

**🔵 B — Atingiu plenamente as competências**
Plano de testes coerente e organizado; casos bem estruturados; execução consistente; identificação de falhas relevantes; análise adequada dos resultados.

**🟢 A — Atingiu as competências com excelência**
Plano de testes claro, completo e bem estruturado; casos de teste detalhados e bem pensados; execução com evidências claras e organizadas; identificação crítica de problemas do sistema; reflexão consistente sobre o processo. Diferenciais: uso adequado de avaliação para IA (quando aplicável); clareza, organização e pensamento profissional de QA.

### 💡 Dica final

Para obter conceito A, vocês devem:

- Organizar os testes como um time profissional de QA
- Especificar casos de forma clara e detalhada
- Não apenas executar, mas analisar os resultados
- Conectar os testes com problemas reais do LocalEats
- Demonstrar raciocínio — não apenas preencher itens
