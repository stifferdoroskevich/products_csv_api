# Criar um serviço API para a consulta de datos desde 2 arquivos CSV.


## Estrutura do projeto

Back-end seguir o padrão **clean architecture**

O banco de dados a ser utilizado será o **MongoDB**.

O Back-end deve ser feito com Python.

**Utilizar Docker** para o levantamento do projeto. 


Ambiente Web
Na última página contém o exemplo de listagem e filtros.

- Via API deve permitir a listagem dos dados por paginação.
A API deve retornar:
  - Total de produtos. 
  - Total de produtos em promoções.
  - Total de categorias.

Deve ser possível filtrar o Segmento e carregar as lojas correspondentes.
Na listagem de Produtos deve ser possível filtrar por EAN ou Category.
Quando o (Preço Por) for diferente do (Preço De) trazer o campo desconto, caso contrário trazer como 0.
Aplicar conceitos de User Experience.  (Ponto Extra) ( Opcional )
Aplicar Unit Test (Ponto Extra) ( Opcional )


Cada parte do código será analisada para qualificar a qualidade do projeto, será levado em consideração a utilização de Design Patterns para o desenvolvimento. 


FILTROS:

      - SEGMENT

      - EAN

      - CATEGORY


LAYOUT RESPONSE

    {
        "total_products":50,
        "total_promotions":30,
        "total_categories":20,
        "products":[{
            "typestorename":"Supermercados",
            "name":"Água Mineral Crystal Pet 1,5L",
            "ean":7894900530032,
            "category":"Bebidas",
            "real_price":2.49,
            "price":2.49,
            "discount":0,
            "quantity":1,
            "sales_type":"U",
            "unit_type":"L"
        }]
    }



TABELA: store 

TABELA: products 


PRIMARY KEY (tb: store)

1. id [STORE] ⇔ store_id [PRODUCTS]


FOREIGN KEYS (tb: products)

1. typestore 

2. store_id 