import requests
from bs4 import BeautifulSoup
import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def get_freeimages(query, filename):
    print(f'Searching freeimages.com for {query}...')
    url = f'https://www.freeimages.com/search/{query}'
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        images = soup.find_all('img', src=True)
        for img in images:
            src = img['src']
            if 'images/large-previews' in src or 'images/previews' in src or 'unsplash' in src:
                if src.startswith('http'):
                    print(f'Downloading {src} to {filename}')
                    req = urllib.request.Request(src, headers=headers)
                    with urllib.request.urlopen(req) as r, open(filename, 'wb') as f:
                        f.write(r.read())
                    return True
    except Exception as e:
        print(f'Error: {e}')
    return False

get_freeimages('truck-highway', 'img/header.jpg')
get_freeimages('indian-truck', 'img/about.jpg')
get_freeimages('warehouse-logistics', 'img/feature.jpg')
get_freeimages('freight-truck', 'img/blog-1.jpg')
get_freeimages('cargo-loading', 'img/blog-2.jpg')
