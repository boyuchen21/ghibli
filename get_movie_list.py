# get the list of movie to pick from
import requests
from bs4 import BeautifulSoup

def get_movie_list():
    url = "https://www.ghibli.jp/works/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headers = soup.select('h1.post-header')
    # get href attribute of the first <a> element in
    links_list = [headers[i].select('a')[0]['href'] for i in range(len(headers))]

    # Print each link with line breaks
    for link in links_list:
        print(link)
