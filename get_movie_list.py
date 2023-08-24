# get the list of movie to pick from
import requests
from bs4 import BeautifulSoup
import re

def get_movie_list():
    url = "https://www.ghibli.jp/works/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headers = soup.select('h1.post-header')
    # get href attribute of the first <a> element in
    links_list = [headers[i].select('a')[0]['href'] for i in range(len(headers))]
    eng_idex_list = [links_list[i].split('/')[-2] for i in range(len(links_list))]
    titles_list = [headers[i].select('a')[0]['title'].encode('ISO-8859-1').decode('utf-8') for i in range(len(headers))]
    pattern = re.compile(r"をもっと見る$")
    titles_list = [pattern.sub('', s) for s in titles_list]

    print("Here are the list of movies you can choose from:")
    # Print each link with line breaks
    for link, title in zip(eng_idex_list, titles_list):
        print(f"{title} / {link}")        