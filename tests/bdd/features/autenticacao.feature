# language: pt
Funcionalidade: Autenticação no Local Eats
  Como visitante interessado em descobrir restaurantes locais,
  quero acessar minha conta no Local Eats,
  para visualizar restaurantes, favoritos e meus pedidos.

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
