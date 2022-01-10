# Markdown syntax guide

## Headers

# This is a Heading h1
## This is a Heading h2 
###### This is a Heading h6

## Emphasis

*This text will be italic*  
_This will also be italic_

**This text will be bold**  
__This will also be bold__

_You **can** combine them_

## Lists

### Unordered

* Item 1
* Item 2
* Item 2a
* Item 2b

### Ordered

1. Item 1
1. Item 2
1. Item 3
  1. Item 3a
  1. Item 3b

## Images

![This is a alt text.](/image/sample.png "This is a sample image.")

## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

## Blockquotes

> Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

## Tables

| Left columns  | Right columns |
| ------------- |:-------------:|
| left foo      | right foo     |
| left bar      | right bar     |
| left baz      | right baz     |

## Blocks of code

```
let message = 'Hello world';
alert(message);
```

## Inline code

This web site is using `markedjs/marked`.


## O que é?

Esta é uma API RESTful que está sendo desenvolvida em parceria ao Grupo de Estudos em Álgebra e Reticulados (GEAR) com o intuito de:

>1 - Estruturar os dados disponiveis em [A Catalogue of Lattices](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/);

>2 - Divulgar e compartilhar os resultados obtidos durante a pesquisa sobre Empacotamento de Regiões, Reticulados e 

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
