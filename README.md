🧠🚀 PROJETO DE ESTUDO (REST API PARA CATÁLOGO DE FILMES, SEUS ELENCOS E AVALIAÇÕES)

Este projeto de estudo visou construir uma Rest API back-end utilizando Django e Django Rest Framwork. A aplicação mantêm um catálogo de filmes que poderia ser consumido por diversos tipos de clientes que tenham o interesse no assunto. O catálogo oferece informações como os gêneros dos filmes, seus respectivos elencos de atores e atrizes, assim como também todas as avaliações dos mesmos que podem ser feitas por usuários devidamente cadastrados.
A API oferece endpoints para listagem, inserção, atualização e exclusão de filmes, gêneros, atores, avaliações dos filmes e também algumas estatísticas da base de dados. As operações são controladas por perfis de usuários e só podem ser realizadas por usuários devidamente cadastrados e autorizados.

  - A autenticação da API é realizada com o uso de JWT - Json Web Tokens. Verificações de permissões são feitas através de classes de permissões.

  - Os testes dos endpoints da API foram feitos com a ferramenta Postman (https://www.postman.com).

  - Todo response da API é devolvido no formato JSON - JavaScript Object Notation.

  - A API foi disponibilizada na plataforma PythonAnywhere para testes através da URL https://leopareja.pythonanywhere.com.<br>
    A aplicação web encontra-se parada por questões de custo.

Estudos adicionais:

- Serializers dinâmicos e customizados.
- Validadores de dados.
- JWT - Json Web Tokens e Permission Classes.
- Django Custom Commands.
- Versionamento de URL's e recursos.
