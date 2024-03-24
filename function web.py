from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def web_scrape(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Supongamos que los títulos son etiquetas <h1> y <h2> y los párrafos son <p>
        titles = [title.text.strip() for title in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        paragraphs = [p.text.strip() for p in soup.find_all('p')]
        # Unimos los títulos y párrafos en un solo texto
        extracted_text = '\n'.join(titles + paragraphs)
        return extracted_text
    else:
        return "No se pudo acceder al sitio web"

@app.route('/scrape', methods=['GET'])
def scrape_and_respond():
    default_url = 'https://unipaz.edu.co/index.html'  # URL predeterminada
    url = request.args.get('url', default_url)
    extracted_text = web_scrape(url)
    return extracted_text

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
