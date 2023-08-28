import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

class NewsScraper:

    def __init__(self, url):
        self.url = url
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['news_database']
        self.collection = self.db['news']

    def fetch_data(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.conteudo

    def parse_data(self, conteudo):
        soup = BeautifulSoup(conteudo, 'html.parser')
        news_list = []

        # Suponhamos que cada notícia esteja em uma div com a classe "news-item"
        for news_item in soup.find_all('div', class_='news-item'):
            titulo = news_item.find('h2').text
            conteudo = news_item.find('p').text
            news_list.append({
                'titulo': titulo,
                'conteudo': conteudo
            })

        return news_list

    def save_to_mongo(self, news_list):
        self.collection.insert_many(news_list)

    def scrape(self):
        conteudo = self.fetch_data()
        news_list = self.parse_data(conteudo)
        self.save_to_mongo(news_list)
        print(f"Savar {len(news_list)} noticias por item no MongoDB.")

if __name__ == "__main__":
    scraper = NewsScraper('https://www.exemplo.com.br/noticias')
    scraper.scrape()
