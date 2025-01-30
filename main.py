import requests
from bs4 import BeautifulSoup

base_url = 'https://www.kompas.com/'

try:
    response = requests.get(base_url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h3')

    print("Judul dan Link Artikel di Kompas.com:")
    for idx, headline in enumerate(headlines, start=1):
        text = headline.get_text(strip=True)
        link_tag = headline.find('a')
        if text and link_tag and link_tag['href']:
            article_url = link_tag['href']
            print(f"{idx}. {text}")
            print(f"Link: {article_url}")
            print("-" * 50)

except requests.exceptions.RequestException as e:
    print("Terjadi kesalahan saat mengambil data:", e)
