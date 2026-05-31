import requests
import urllib.request
import re

def download_bing_image(query, filename):
    print(f'Searching Bing for {query}...')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = f'https://www.bing.com/images/search?q={query.replace(" ", "+")}'
    try:
        res = requests.get(url, headers=headers)
        # Find the first image URL in the Bing results
        match = re.search(r'murl&quot;:&quot;(http[^&]+(?:jpg|png|jpeg))&quot;', res.text)
        if match:
            img_url = match.group(1)
            print(f'Downloading {img_url} to {filename}')
            req = urllib.request.Request(img_url, headers=headers)
            with urllib.request.urlopen(req) as r, open(filename, 'wb') as f:
                f.write(r.read())
            return True
        else:
            print('No image found.')
    except Exception as e:
        print(f'Error: {e}')
    return False

download_bing_image('commercial freight transport truck highway high quality', 'img/header.jpg')
download_bing_image('indian heavy transport logistics truck', 'img/about.jpg')
download_bing_image('logistics warehouse truck fleet', 'img/feature.jpg')
download_bing_image('truck driving on modern highway sunset', 'img/blog-1.jpg')
download_bing_image('forklift loading cargo truck', 'img/blog-2.jpg')
