# language: pt
Funcionalidade: Exploração de restaurantes
  Como usuário autenticado,
  quero navegar pela lista de restaurantes e abrir detalhes,
  para escolher onde comer.

  Contexto:
    Dado que estou autenticado no Local Eats com "teste@teste.com" / "123"

  Cenário: Lista de restaurantes é exibida na home
    Quando a página inicial termina de carregar
    Então vejo pelo menos 1 restaurante na lista

  Cenário: Abrir detalhe de um restaurante
    Quando clico no primeiro restaurante da lista
    Então sou levado a uma página cujo endereço contém "restaurant.html"
