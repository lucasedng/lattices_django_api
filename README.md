## O que é?

Esta é uma API RESTful que está sendo desenvolvida em parceria ao Grupo de Estudos em Álgebra e Reticulados (GEAR) com o intuito de:

>1 - Estruturar os dados disponiveis em [A Catalogue of Lattices](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/);

>2 - Divulgar e compartilhar os resultados obtidos durante a pesquisa sobre Empacotamento de Regiões, Reticulados e Códigos Corretores de Erros.

## Como acessar?

Você pode acessar através [deste link](https://api-lattices-postgresq.herokuapp.com/).


## Desenvolvimento:
Framework utilizado em seu desenvolvimento: [django REST framework](https://www.django-rest-framework.org/);

Processo de autenticação: [JSON Web Token Authentication](https://www.django-rest-framework.org/api-guide/authentication/);

Banco de dados: [PostgreSQL](https://www.postgresql.org/);

Hospedagem atual: [Heroku](https://www.heroku.com/).

## O Catálogo de Reticulados:

A partir de um _nome_ ou _id_, você poderá obter as informações mais relevantes sobre um reticulado. Os nomes podem ser obtidos [aqui](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/), ou no catálogo do GEAR.

| Método  | Rota | Descrição|
| ------------- |-------------| ----------------|
| GET     | `/lattices`  | [ROTA PÚBLICA] Consulta informações sobre todos os reticulados disponíveis. |
| GET     | `/publiclattices/:lattice_id`  | [ROTA PÚBLICA] Consulta informações sobre  um determinado reticulado.|
| GET     | `/lattices`  | [ROTA PRIVADA] Consulta informações sobre todos os reticulados disponíveis. |
| POST     | `/lattices`  | [ROTA PRIVADA] Adiciona um novo reticulado ao banco de dados.|
| GET     | `/lattices/:lattice_id`  | [ROTA PRIVADA] Consulta informações sobre  um determinado reticulado. |
| PUT     | `/lattices/:lattice_id`  | [ROTA PRIVADA] Altera informações sobre  um determinado reticulado.|
| DELETE     | `/lattices/:lattice_id`  | [ROTA PRIVADA] Deleta o reticulado do banco de dados.|

## Estrutura da resposta:

`publiclattices/b8df165-9928-404f-8385-7914791efc49`

```json
{
    "id_lattice": "6b8df165-9928-404f-8385-7914791efc49",
    "name": "A2",
    "dimension": 2,
    "determinant": 3,
    "minimal_norm": 2,
    "kissing_number": 6,
    "gram_matrix": [
        [
            2,
            -1
        ],
        [
            -1,
            2
            ]
    ],
    "create_at": "2022-01-07"
}

```

## Executando o projeto

Instale as dependências:

`pip install -r requirements.txt`

Rodando a aplicação localmente:

`python manage.py runserver`

___
Para saber mais sobre reticulados: 


[Lattice-based cryptography](https://en.wikipedia.org/wiki/Lattice-based_cryptography)

[Introdução à Teoria dos Reticulados e suas Propriedades](https://repositorio.unifesp.br/bitstream/handle/11600/60730/Lucas_Eduardo_Trabalho_de_Graduacao_Final.pdf?sequence=7&isAllowed=y)
