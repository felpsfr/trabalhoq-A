# PBL 4 — Testes Funcionais vs Estruturais · Local Eats

> Entrega da Aula 5 · Disciplina de Qualidade de Software — Senac-RS
> Enunciado original: [../docs/enunciados/pbl-4-funcionais-estruturais.md](../docs/enunciados/pbl-4-funcionais-estruturais.md)

## Integrantes

- Felipe Ferreira Ribeiro - Matrícula: 782410083

## 1. Funcionalidade escolhida

**Funcionalidade:** **Busca de restaurantes**

Escolhi a busca porque ela é o coração do Local Eats: todas as jornadas relevantes (descobrir um restaurante, favoritar, avaliar, receber recomendação) começam ou dependem dela. Também é a funcionalidade com o sintoma mais grave relatado pelos usuários (“resultados incorretos”), o que a torna o ponto de maior retorno para análise conjunta de caixa-preta e caixa-branca.

### 1.1 O que a funcionalidade faz

A busca recebe um termo digitado pelo usuário e/ou filtros (tipo de culinária, faixa de preço, localização) e retorna uma lista paginada de restaurantes que combinam com esses critérios. O resultado é normalmente ordenado por uma regra de relevância que leva em conta distância até o usuário, avaliação média e popularidade recente. Se nada for encontrado, a interface deve sinalizar o resultado vazio e sugerir relaxar filtros.

### 1.2 O que o usuário espera dela

- Que o termo digitado encontre **restaurantes equivalentes**, incluindo variações (acentos, maiúsculas/minúsculas, sinônimos como “pizzaria” para cozinha italiana).
- Que os **filtros sejam respeitados** (se pediu “faixa $$” não aparecer $$$$).
- Que a busca seja **rápida**, mesmo em horários de pico.
- Que a **ordenação faça sentido**: resultados próximos e bem avaliados aparecem primeiro.
- Que, em caso de zero resultados, a aplicação **comunique claramente** e proponha alternativas.
- Que o comportamento seja **consistente entre web e mobile**.

## 2. Testes Caixa-Preta (Visão do Usuário)

> Perspectiva: sem conhecer o código. Valido entradas, saídas e comportamento visível.

### 2.1 Entradas possíveis

- Termo válido corriqueiro (“pizza”, “japonês”)
- Termo com acentuação e variações de caixa (“Japonês”, “JAPONES”, “japónes”)
- Termo com erro de digitação (“sushii”)
- Termo parcial (prefixo: “piz”) e termo muito curto (1 caractere)
- Termo vazio (busca apenas com filtros)
- Caracteres especiais (`@`, `#`, emojis) e tentativas de injeção (`' OR 1=1`)
- Combinações de filtros: culinária + preço; culinária + preço + localização; apenas preço; apenas localização
- Faixa de preço invertida (mínimo > máximo)
- Localização impossível (coordenada em outro país) ou permissão de localização negada
- Busca executada sem rede / com rede intermitente

### 2.2 Cenários de teste funcionais

| #  | Cenário                                                        | Entrada                                             | Comportamento esperado                                                                 |
|----|----------------------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------------------------------------|
| 1  | Busca simples por culinária                                    | “pizza”                                             | Lista paginada de restaurantes que servem pizza, ordenada por relevância/proximidade.   |
| 2  | Busca ignorando acentuação e caixa                             | “JAPONÊS”, “japones”, “JaPonês”                     | Todos retornam o mesmo conjunto de resultados.                                         |
| 3  | Busca com termo parcial                                        | “piz”                                               | Retorna pizzarias via *prefix-match* ou *auto-complete*.                               |
| 4  | Busca com filtro de preço combinado                            | culinária=“italiana” + preço=“$$”                   | Somente restaurantes italianos com faixa de preço $$ aparecem.                         |
| 5  | Busca com zero resultados                                      | “xyzabc123”                                         | Mensagem clara “Nenhum restaurante encontrado”; sugestão de relaxar filtros.           |
| 6  | Busca com termo muito curto                                    | “a”                                                 | Sistema pede termo com mais caracteres **ou** usa filtros em vez do termo.              |
| 7  | Busca com caracteres especiais / tentativa de injeção          | `' OR 1=1--`                                        | Não quebra; trata como texto; retorna vazio ou erro amigável.                           |
| 8  | Faixa de preço invertida                                       | preço_min=100, preço_max=20                          | Validação sinaliza o problema ou inverte automaticamente.                              |
| 9  | Busca sem permissão de localização                             | permissão negada                                    | Continua funcionando, porém sem ordenar por proximidade; informa o usuário.            |
| 10 | Busca com rede instável                                         | latência alta / pacote perdido                      | UI mostra estado de carregamento e mensagem de erro recuperável (tentar novamente).    |
| 11 | Consistência entre plataformas                                 | mesmo termo/filtro na web e mobile                  | Mesmos resultados, mesma ordem.                                                         |
| 12 | Paginação                                                      | avançar para a última página                        | Última página exibe corretamente o número restante de itens; não trava em páginas vazias. |

### 2.3 Tipos de erro detectáveis por caixa-preta

- Resultados incorretos ou incompletos para termos válidos (sintoma principal relatado).
- Mensagens ausentes ou confusas em situações de erro (lista vazia, sem conexão).
- Filtros que não filtram (restaurantes fora da faixa escolhida aparecem).
- Inconsistência entre web e mobile (mesma busca, respostas diferentes).
- Performance perceptível: busca que demora muito em horários de pico.
- Tela que quebra com entrada inesperada (caractere especial → erro 500 visível ao usuário).

## 3. Testes Caixa-Branca (Visão do Sistema)

> Perspectiva: com acesso ao código. Examino estruturas internas, ramos e condições.

### 3.1 Possível estrutura de implementação (pseudocódigo)

```pseudo
função buscar(termo, filtros, usuario):
    se termo.vazio() e filtros.todosVazios():
        retornar lista_padrao(popularidade, usuario.localizacao)

    termoNormalizado = remover_acentos(trim(lower(termo)))
    se len(termoNormalizado) < 2 e filtros.todosVazios():
        lançar ValidationError("termo muito curto")

    filtros = sanitizar(filtros)
    se filtros.precoMin > filtros.precoMax:
        trocar(filtros.precoMin, filtros.precoMax)

    tentar:
        resultados = indice.buscar(termoNormalizado, filtros)
    capturar(TimeoutError):
        retornar fallback_cache(termoNormalizado, filtros)

    se usuario.tem_localizacao():
        resultados = ordenar_por(distancia, avaliacao_media, popularidade)
    senão:
        resultados = ordenar_por(avaliacao_media, popularidade)

    retornar paginar(resultados, filtros.pagina, filtros.tamanhoPagina)
```

### 3.2 Regras internas / decisões que geram ramos

- `if termo vazio e filtros vazios` → retorna lista padrão.
- `if len(termoNormalizado) < 2 e filtros vazios` → erro de validação.
- `if precoMin > precoMax` → inverte ou rejeita?
- `try/except` em `indice.buscar` → *fallback* para cache em caso de *timeout*.
- `if usuario tem localização` → ordenação distinta.
- Paginação: cálculo de `offset = (pagina - 1) * tamanhoPagina` e tratamento de última página (tamanho parcial).
- Normalização de string: remoção de acentos, *lowercase*, *trim*.
- Sanitização de filtros: coerção de tipos, validação do `enum` de culinária.

### 3.3 Situações que precisam ser cobertas no código

| #  | Situação de código                                          | Por que testar                                                             |
|----|-------------------------------------------------------------|-----------------------------------------------------------------------------|
| 1  | Termo vazio + nenhum filtro                                 | Verifica ramo “lista padrão”; evita chamar índice sem necessidade.          |
| 2  | Termo < 2 caracteres + nenhum filtro                        | Verifica branch de validação e mensagem de erro correta.                    |
| 3  | Termo < 2 caracteres **com** filtros                        | Garante que, com filtros, a busca ainda ocorre (*não* cai no ramo de erro). |
| 4  | `precoMin > precoMax`                                       | Verifica sanitização (troca dos valores) — previne *off-by-one* silencioso. |
| 5  | *Timeout* do índice                                          | Verifica `try/except` e o *fallback* para cache.                            |
| 6  | Usuário sem localização                                     | Cobre ramo alternativo de ordenação; evita *null pointer*.                  |
| 7  | Lista de resultados vazia vinda do índice                   | Garante retorno de lista vazia, não `null`, e manutenção do contrato de API. |
| 8  | Última página com menos itens que o tamanho da página        | Testa aritmética de paginação.                                               |
| 9  | Caracteres especiais após normalização                      | Garante que a normalização não quebre com entradas inesperadas.             |
| 10 | Tentativa de injeção (`' OR 1=1`)                           | Garante uso de *query parameters*/prepared statements no acesso ao banco.   |

### 3.4 Tipos de cobertura visados

- **Cobertura de comandos (statement coverage):** toda linha executada pelo menos uma vez.
- **Cobertura de decisão (branch coverage):** cada `if/else`, cada ramo de `try/except`.
- **Cobertura de condição / MC-DC:** avaliar combinações lógicas em condicionais compostas (ex.: `termo.vazio() e filtros.todosVazios()`).
- **Cobertura de caminhos críticos:** caminho completo desde a entrada até o *fallback* de cache em caso de *timeout*.

### 3.5 Tipos de erro detectáveis apenas por caixa-branca

- Ramos não alcançados (ex.: *fallback* do cache nunca é executado porque a condição está escrita invertida).
- Código morto que nunca é chamado.
- Exceções engolidas silenciosamente (*swallowed exceptions*).
- Cálculos de paginação incorretos em condições de borda.
- *Off-by-one* e problemas de *short-circuit* em expressões booleanas compostas.

## 4. Comparação entre as abordagens

| Critério                         | Caixa-preta (funcional)                                         | Caixa-branca (estrutural)                                             |
|----------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------|
| Conhecimento necessário          | Requisitos, comportamento esperado, contrato externo              | Código-fonte, fluxo interno, estruturas de dados                       |
| Quem normalmente aplica          | QA, analistas, usuários de UAT                                  | Desenvolvedores (e QA com viés técnico)                                |
| O que valida                     | **O quê** o sistema faz                                          | **Como** o sistema faz                                                 |
| Tipos de erro detectáveis        | Divergência de requisito, UX ruim, validações ausentes, falhas de contrato | Caminhos não cobertos, ramos mortos, exceções engolidas, *off-by-one* |
| Momento de uso                   | Validação funcional antes de cada entrega                        | Construção do código (TDD) e rede de segurança em refatorações         |
| Custo                            | Geralmente mais barato (testes manuais ou E2E automatizados)     | Exige tempo de implementação de testes unitários/integração            |
| Limitação principal              | Não enxerga ramos não acionáveis pelo usuário                    | Pode passar em testes e ainda assim não atender ao que o usuário precisa |
| Resposta ao cenário Local Eats   | Detecta “busca retornou resultados incorretos”                  | Mostra *por que* o ramo de sanitização dos filtros não foi executado   |

**Diferença central:** a caixa-preta garante que o produto **entrega valor** para quem usa; a caixa-branca garante que o código está **robusto**, coberto e livre de armadilhas estruturais. Uma abordagem responde “está funcionando?”; a outra responde “está bem feito?”.

## 5. Reflexão no contexto do Local Eats

### 5.1 Qual abordagem parece mais útil para os problemas atuais?

**Nenhuma sozinha é suficiente — as duas são necessárias**, mas a caixa-preta tem prioridade imediata para atacar os sintomas visíveis aos usuários. Os problemas mais visíveis do Local Eats (telas confusas, buscas com resultado incorreto, dificuldade para concluir ações, inconsistência web/mobile) são **sintomas de comportamento externo**, e portanto se revelam mais rapidamente com cenários caixa-preta, inclusive com testes exploratórios. Já os sintomas “avaliações desaparecem” e “falhas em dispositivos específicos” têm raízes internas (persistência, condições de contorno, manipulação de estado) e respondem melhor a **testes estruturais + integração**, garantindo que os ramos de tratamento de erro e a persistência estejam cobertos.

### 5.2 Apenas uma abordagem seria suficiente?

**Não.** Como o ISTQB ressalta, as duas abordagens são complementares:

- Somente caixa-preta deixa passar bugs estruturais silenciosos: um *swallowed exception* que faz o sistema “parecer ok” até o dado se perder.
- Somente caixa-branca deixa passar bugs de negócio: o código está coberto, mas não faz o que o usuário esperava.

**Recomendação para o Local Eats.** Adotar uma estratégia dupla:

1. **Caixa-branca** na base da pirâmide — testes unitários para funções de normalização, ordenação, sanitização de filtros e persistência de avaliações; testes de integração cobrindo índice de busca, banco e cache.
2. **Caixa-preta** no meio e no topo — testes E2E para fluxos críticos (login → busca → avaliação) executados em web e mobile, testes de aceitação com critérios claros, e rodadas de testes exploratórios focadas nos sintomas relatados.
3. **Monitoramento em produção** fecha o ciclo, detectando problemas que nem uma nem outra abordagem antecipou.

Essa combinação conecta a qualidade percebida pelo usuário à qualidade interna do código, atacando simultaneamente as duas frentes em que o Local Eats hoje tem dívida.

## Referências

- ISTQB Foundation Level Syllabus — Capítulos 2 e 4
- ISO/IEC 25010:2011
- Pressman, R. — *Engenharia de Software: Uma Abordagem Profissional*
- Material de aula — Prof. Luciano Zanuz
