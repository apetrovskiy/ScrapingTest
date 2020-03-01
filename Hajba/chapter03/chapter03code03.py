from bs4 import BeautifulSoup


with open('example.html') as infile:
    soup = BeautifulSoup(infile, 'html.parser')
