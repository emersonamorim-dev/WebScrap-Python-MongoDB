# WebScraper News - Python MongoDB

Codificação de WebScraper em Python para extrair notícias de um site fictício e para banco de dados implementei para salvar os dados no MongoDB.

## Requisitos

- Python 3.x
- MongoDB rodando localmente na porta padrão (27017)

## Bibliotecas utilizadas

- `requests`: Para fazer requisições HTTP.
- `BeautifulSoup4`: Para parsear e extrair informações do conteúdo HTML.
- `pymongo`: Para interagir com o MongoDB.

## Como usar

1. Instale as bibliotecas necessárias:

```bash
pip install requests beautifulsoup4 pymongo

## Execute o script:

python main.py

## Funcionamento
O script faz uma requisição para a URL especificada, extrai as notícias (assumindo que estão em divs com a classe news-item), e salva os títulos e conteúdos no MongoDB.


## Autor:
Emerson Amorim
