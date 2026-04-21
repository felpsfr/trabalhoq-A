# PBL 1 — Atributos de Qualidade da ISO 25000 (Local Eats)

> Entrega da Aula 2 · Disciplina de Qualidade de Software — Senac-RS
> Enunciado original: [../docs/enunciados/pbl-1-iso25000.md](../docs/enunciados/pbl-1-iso25000.md)

## Integrantes

- Felipe Ferreira Ribeiro - Matrícula: 782410083

## 1. Compreensão do cenário

**Propósito do sistema Local Eats.** Conectar moradores e turistas a restaurantes independentes da cidade, fortalecendo o comércio local e oferecendo uma experiência prática, rápida e confiável de busca e descoberta de estabelecimentos gastronômicos. A plataforma disponibiliza versão web e aplicativo mobile com busca por culinária, localização e faixa de preço, visualização de cardápios/fotos/avaliações, favoritos, recomendações personalizadas e compartilhamento de experiências.

**Usuários principais.** (i) *Moradores* que usam a plataforma recorrentemente para descobrir novos restaurantes; (ii) *turistas* que precisam de resultados confiáveis em pouco tempo; (iii) *donos de restaurantes independentes*, cuja visibilidade e reputação dependem do que o sistema exibe; (iv) a *associação de comerciantes*, patrocinadora e principal interessada na reputação da plataforma.

**Resumo dos problemas relatados.** Após um lançamento apressado para atender um grande evento gastronômico, os usuários relatam: lentidão em horários de pico, telas confusas, resultados de busca incorretos, falhas em determinados smartphones, dificuldade para concluir ações simples, avaliações que desaparecem após atualização e inconsistências entre as versões web e mobile. Em conjunto, esses sintomas indicam que múltiplas características de qualidade da ISO/IEC 25010 estão comprometidas.

## 2. Problemas identificados no produto

1. Sistema fica lento em horários de pico.
2. Algumas telas são confusas e pouco intuitivas.
3. Certas buscas retornam resultados incorretos.
4. O aplicativo apresenta falhas em determinados modelos de smartphone.
5. Usuários encontram dificuldade para concluir ações simples (fluxos de UX).
6. Avaliações desaparecem após atualização da página (perda de estado/dados).
7. Há inconsistências entre a versão web e a versão mobile.

## 3. Relação entre problemas e atributos de qualidade (ISO/IEC 25010)

Referencial: modelo de qualidade do produto da ISO/IEC 25010, composto por 8 características — *Functional Suitability*, *Performance Efficiency*, *Compatibility*, *Usability*, *Reliability*, *Security*, *Maintainability* e *Portability*.

| # | Problema identificado                        | Característica afetada      | Sub-característica                     | Justificativa técnica                                                                                                       | Impacto para usuário / negócio                                               |
|---|----------------------------------------------|-----------------------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 1 | Lentidão em horários de pico                 | Performance Efficiency      | Time Behaviour; Resource Utilization   | O sistema não sustenta o tempo de resposta esperado sob carga concorrente, indicando gargalos (consultas custosas, ausência de cache, infra subdimensionada). | Frustração, abandono durante picos (justamente quando mais gera receita); reputação.          |
| 2 | Telas confusas e pouco intuitivas            | Usability                   | Learnability; Operability; UI Aesthetics | Falta de hierarquia visual, rótulos ambíguos e fluxos não alinhados ao modelo mental do usuário dificultam a descoberta do que fazer. | Tempo maior para concluir tarefas, erros de uso, suporte sobrecarregado.      |
| 3 | Buscas retornam resultados incorretos        | Functional Suitability      | Functional Correctness; Appropriateness | A função *busca* é o core do produto; resultados incorretos indicam falhas no algoritmo de filtro, no índice ou nas regras de relevância. | Quebra da proposta de valor (achar restaurantes relevantes); perda de confiança.              |
| 4 | Falhas em determinados smartphones           | Compatibility · Portability | Co-existence; Adaptability; Installability | O app não se adapta corretamente a todas as variações de hardware, SO, densidade de tela e APIs de fabricantes. | Parcela da base fica sem acesso; comerciantes perdem visibilidade junto a esses usuários.     |
| 5 | Dificuldade para concluir ações simples      | Usability                   | Operability; User Error Protection     | Fluxos longos, passos redundantes e validação inadequada impedem o usuário de finalizar tarefas básicas (favoritar, avaliar, filtrar). | Queda de engajamento, abandono de funil.                                      |
| 6 | Avaliações desaparecem após atualização      | Reliability                 | Maturity; Fault Tolerance; Recoverability | Perda de dados após reload sugere que a avaliação não é efetivamente persistida ou que há falha de sincronização entre cache e backend. | Perda de conteúdo gerado pelo usuário (UGC), dano direto à credibilidade da plataforma.       |
| 7 | Inconsistências entre web e mobile           | Reliability · Compatibility | Consistency (ISO 25010 §Usability); Co-existence | Contratos/estados divergentes entre frontends indicam ausência de fonte única de verdade e contratos de API não padronizados. | Usuário desconfia do que vê; comerciantes recebem dados contraditórios.       |

### 3.1 Observações adicionais

- **Segurança** não é citada explicitamente nos relatos, mas avaliações desaparecerem abre flanco para suspeita de **integridade** de dados — vale investigar em uma rodada seguinte.
- **Manutenibilidade** tende a estar comprometida implicitamente, porque o conjunto de sintomas recorrentes sugere código rapidamente escrito sob pressão de prazo do evento.

## 4. Análise consolidada

### 4.1 O sistema possui qualidade adequada para continuar em operação?

**Parcialmente.** O sistema entrega a *proposta funcional básica* (é possível buscar restaurantes, visualizar cardápio, favoritar, avaliar), mas **não atende aos níveis mínimos** de *Functional Suitability*, *Reliability*, *Performance Efficiency* e *Usability* para uma plataforma voltada ao público final — especialmente em um cenário de evento gastronômico, onde picos de uso e primeiras impressões são decisivos. Recomenda-se manter em operação com um **plano de correção priorizado** e canais de monitoramento, evitando remover o produto (o que causaria mais dano reputacional), mas comunicando transparência sobre as melhorias em curso.

### 4.2 Quais aspectos da qualidade estão mais comprometidos?

Em ordem de severidade percebida:

1. **Functional Suitability (Correctness)** — buscas incorretas comprometem a entrega de valor central; todas as demais funcionalidades dependem de a busca funcionar.
2. **Reliability (Maturity / Recoverability)** — perda de avaliações e inconsistência entre plataformas corroem a confiança de forma difícil de reverter.
3. **Performance Efficiency (Time Behaviour)** — lentidão em horários de pico degrada experiência no momento de maior exposição.
4. **Usability (Operability)** — telas confusas e dificuldade de concluir ações elevam a curva de aprendizado e o atrito.
5. **Compatibility/Portability (Adaptability)** — falhas em modelos específicos excluem parte da base.

### 4.3 Quais problemas devem ser priorizados?

Critério utilizado: **impacto no valor entregue + risco à reputação + frequência/alcance do problema**.

| Ordem | Problema                                          | Por que priorizar                                                                                 |
|:-----:|---------------------------------------------------|----------------------------------------------------------------------------------------------------|
| 1     | Buscas retornam resultados incorretos             | Quebra a proposta central do produto; sem busca confiável o app perde sentido.                     |
| 2     | Avaliações desaparecem após atualização           | Perda de UGC é praticamente irreversível reputacionalmente; afeta comerciantes diretamente.        |
| 3     | Lentidão em horários de pico                      | Pico = maior visibilidade = maior dano se falhar; corrige cenário do evento gastronômico.          |
| 4     | Inconsistência web ↔ mobile                       | Afeta confiança sistêmica; endereçá-la simplifica as demais correções (fonte única de verdade).    |
| 5     | Dificuldade para concluir ações simples           | UX de fluxos críticos (favoritar, avaliar) — impacta retenção e engajamento.                       |
| 6     | Telas confusas                                    | Tratamento junto com o item 5 (ambos são Usability).                                               |
| 7     | Falhas em modelos específicos de smartphone       | Importante, mas tipicamente atinge parcela menor; depende da distribuição da base.                 |

## 5. Recomendações preliminares

- **Correctness da busca:** revisar algoritmo, índice e dataset; instrumentar métricas de relevância (CTR dos primeiros resultados) e criar suíte de testes com cenários reais.
- **Persistência de avaliações:** auditar o fluxo *POST avaliação → banco → leitura* e adicionar testes de integração; implementar mecanismo de *retry* no cliente com feedback visual.
- **Performance:** profiling das queries mais lentas, introdução de cache nos endpoints quentes, testes de carga simulando o evento; alertas de latência no monitoramento.
- **Consistência web/mobile:** padronizar contratos (OpenAPI), adotar fonte única para regras de negócio (preferencialmente no backend), testes de contrato automatizados.
- **Usabilidade:** testes de usabilidade com usuários reais, revisão de microcopy e hierarquia visual; adoção de heurísticas de Nielsen como checklist.
- **Portabilidade mobile:** matriz mínima de dispositivos + farm de *devices* para smoke tests pós-release.

## Referências

- ISO/IEC 25010:2011 — *Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*
- ISTQB Foundation Level Syllabus (conceitos de atributos de qualidade)
- Material de aula — Prof. Luciano Zanuz
