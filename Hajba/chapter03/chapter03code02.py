from bs4 import BeautifulSoup
from requests import get


# soup = BeautifulSoup('http://hajba.hu', 'html.parser')
soup = BeautifulSoup(get('http://hajba.hu').text, 'html.parser')
