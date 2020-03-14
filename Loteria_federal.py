from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/federal'
url = "http://www.pythonscraping.com/pages/page1.html"
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs)