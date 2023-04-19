import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd?cena_d_to' \
           '=100000&cena_d_unit=4&kvadratura_d_from=35&kvadratura_d_unit=1'


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.text, features='html.parser')


if __name__ == '__main__':
    get_soup(BASE_URL)
