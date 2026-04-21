# PBL 3 — Estratégia Inicial de Testes · Local Eats

> Entrega da Aula 4 · Disciplina de Qualidade de Software — Senac-RS
> Enunciado original: [../docs/enunciados/pbl-3-estrategia-testes.md](../docs/enunciados/pbl-3-estrategia-testes.md)

## Integrantes

- Felipe Ferreira Ribeiro - Matrícula: 782410083

## 1. Funcionalidades principais

Selecionei as seguintes funcionalidades do sistema Local Eats como foco da estratégia de testes:

1. **Busca de restaurantes** — por culinária, localização e faixa de preço
2. **Cadastro e login de usuário**
3. **Visualização de cardápio, fotos e avaliações**
4. **Favoritar restaurante**
5. **Avaliar restaurante / deixar comentário**
6. **Recomendações personalizadas**

Essas seis funcionalidades foram escolhidas porque representam o *caminho principal* de valor do produto: sem autenticação não há experiência personalizada, sem busca não há descoberta, e os demais pilares (cardápio, avaliação, favoritos e recomendações) sustentam o engajamento contínuo. O escopo cobre os sintomas relatados pelos usuários (lentidão, inconsistência web/mobile, perda de avaliações, resultados incorretos).

## 2. Níveis de teste por funcionalidade

### 2.1 Busca de restaurantes

| Nível             | O que testar                                                                 |
|-------------------|------------------------------------------------------------------------------|
| Unitário          | Funções de filtragem por culinária/preço; normalização de strings de busca   |
| Integração        | API de busca ↔ banco de dados ↔ serviço de geolocalização                    |
| Sistema           | Fluxo completo: usuário digita termo → recebe lista paginada e ordenada      |
| Aceitação         | Usuário consegue encontrar restaurantes próximos que atendem seus filtros    |

### 2.2 Cadastro e login

| Nível             | O que testar                                                                 |
|-------------------|------------------------------------------------------------------------------|
| Unitário          | Validação de e-mail, hash de senha, regras de senha forte                    |
| Integração        | API de autenticação ↔ base de usuários ↔ serviço de e-mail (confirmação)     |
| Sistema           | Fluxo completo: cadastro → confirmação → login → sessão ativa                |
| Aceitação         | Usuário consegue se cadastrar e acessar sua conta com segurança              |

### 2.3 Visualização de cardápio e avaliações

| Nível             | O que testar                                                                 |
|-------------------|------------------------------------------------------------------------------|
| Unitário          | Formatação de preços, ordenação de avaliações                                |
| Integração        | Componente de detalhe ↔ APIs de cardápio, imagens e avaliações               |
| Sistema           | Abrir detalhe de restaurante exibe cardápio, fotos e avaliações consistentes |
| Aceitação         | Usuário consegue decidir onde comer com base nas informações exibidas        |

### 2.4 Favoritar

| Nível             | O que testar                                                                 |
|-------------------|------------------------------------------------------------------------------|
| Unitário          | Toggle de estado favorito na UI                                              |
| Integração        | API de favoritos ↔ perfil do usuário                                         |
| Sistema           | Favoritar em um dispositivo reflete em outro (web ↔ mobile)                  |
| Aceitação         | Usuário consegue manter sua lista de preferidos ao longo do tempo            |

### 2.5 Avaliações

| Nível             | O que testar                                                                 |
|-------------------|------------------------------------------------------------------------------|
| Unitário          | Validação de nota (1-5), limite de caracteres do comentário                  |
| Integração        | API de avaliações ↔ perfil de restaurante ↔ base de usuários                 |
| Sistema           | Avaliação enviada aparece na página do restaurante e não desaparece          |
| Aceitação         | Usuário consegue registrar sua opinião e ela é preservada                    |

### 2.6 Recomendações personalizadas

| Nível             | O que testar                                                                 |
|-------------------|------------------------------------------------------------------------------|
| Unitário          | Cálculo de score por proximidade / histórico                                 |
| Integração        | Motor de recomendação ↔ base de histórico ↔ catálogo                         |
| Sistema           | Lista recomendada varia conforme uso e perfil                                |
| Aceitação         | Usuário percebe sugestões úteis alinhadas a suas preferências                |

## 3. Prioridades e análise de risco

| Funcionalidade              | Criticidade | Impacto de falha                                         | Prioridade |
|-----------------------------|:-----------:|----------------------------------------------------------|:----------:|
| Cadastro e login            | Alta        | Usuário não entra → bloqueia uso inteiro do sistema      | 🔴 Alta    |
| Busca de restaurantes       | Alta        | Core do produto: se falha, não há valor entregue         | 🔴 Alta    |
| Avaliações                  | Média-alta  | Perda de conteúdo afeta confiança e reputação            | 🟠 Média   |
| Visualização de cardápio    | Média       | Informação incorreta pode frustrar, mas não bloqueia     | 🟠 Média   |
| Favoritar                   | Média       | Recurso útil, mas contornável                            | 🟡 Baixa   |
| Recomendações               | Baixa       | Sem recomendações, sistema ainda funciona                | 🟡 Baixa   |

**Justificativa:** as funcionalidades classificadas como “Alta” compõem o *caminho crítico* do produto — sem login e sem busca, não há Local Eats. As demais influenciam engajamento e retenção, mas o sistema ainda entrega valor mínimo.

## 4. Pirâmide de Testes

```
                 /\
                /  \   E2E / Aceitação   (poucos, caros, lentos)
               /----\
              /      \  Integração        (quantidade moderada)
             /--------\
            /          \ Unitários        (muitos, rápidos, baratos)
           /____________\
```

- **Base — testes unitários (maior quantidade):** rápidos, isolados, baratos de manter; cobrem regras de negócio (validações, cálculos, formatação).
- **Meio — testes de integração:** cobrem pontos de ligação que geram os erros mais frequentes do Local Eats (busca ↔ BD, login ↔ serviço de e-mail, avaliações ↔ perfil).
- **Topo — testes E2E / aceitação (menor quantidade):** poucos, porém estratégicos, cobrindo *happy paths* críticos (login → busca → avaliação).

**Justificativa:** concentrar esforço nos unitários maximiza feedback rápido a cada commit; integrar no meio reduz os problemas de “funciona sozinho, falha junto” observados no Local Eats; E2E fica reservado para o fluxo crítico, onde o custo alto se justifica.

## 5. Testes em Produção

**O sistema deveria usar testes em produção? Sim — de forma controlada e complementar.** Os testes em ambiente de homologação não cobrem condições reais de carga, diversidade de dispositivos, latência de rede nem dados autênticos. Vários dos sintomas já relatados (lentidão em horários de pico, falhas em smartphones específicos, inconsistências web/mobile) só emergem com tráfego real. Portanto, testar em produção *não substitui* as demais camadas da pirâmide, mas **complementa** o que os ambientes anteriores não conseguem replicar.

**Em quais situações aplicar:**

- **Smoke tests pós-deploy** — validam que endpoints críticos sobem após cada release.
- **Canary releases / feature flags** — expor nova versão a uma fração de usuários antes da liberação total.
- **Testes A/B de recomendações** — comparar algoritmos sem comprometer a base.
- **Monitoramento sintético** — transações automatizadas simulando login/busca de hora em hora para detectar degradação.
- **Observabilidade / alertas** — medir latência, taxa de erro, *Apdex* (conecta com os relatos de lentidão em horários de pico).

**Cuidados:** dados de teste devem ser claramente marcados; evitar gerar avaliações ou pedidos reais; LGPD exige cuidado ao manipular dados de usuários reais.

## 6. Conexão com os problemas reais do sistema

| Problema relatado                           | Onde a estratégia ataca                                                   |
|---------------------------------------------|---------------------------------------------------------------------------|
| Lentidão em horários de pico                | Monitoramento sintético + testes de performance na integração             |
| Buscas com resultados incorretos            | Testes unitários de filtros + integração com serviço de busca             |
| Falhas em smartphones específicos           | Camada de aceitação em dispositivos reais / farm de devices               |
| Avaliações desaparecem                      | Teste de integração avaliações ↔ perfil + monitoramento de consistência    |
| Inconsistências web/mobile                  | Contratos compartilhados testados na integração entre front e API         |

## Referências

- ISTQB Foundation Level Syllabus
- Mike Cohn — *Succeeding with Agile* (pirâmide de testes)
- Material de aula — Prof. Luciano Zanuz
