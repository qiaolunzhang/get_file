# firefox driver: geckodriver.exe
import requests
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')

def save_pdf(href):
    try:
        root = './/download//'
        kv = {'user-agent': 'Mozilla/5.0'}
        print(href)
        r = requests.get(href, headers=kv)
        path = root + href.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        print("一份pdf")
    except:
        return ""
# firefox_options.binary_location = r'C:\ProgramData\Anaconda3\Scripts\geckodriver.exe'
# chrome_options.binary_location = '/opt/google/chrome/chrome'

driver = webdriver.Firefox(firefox_options=firefox_options, executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver\geckodriver.exe')

time.sleep(3)
driver.get("http://web.mit.edu/15.053/www/AMP.htm")
r = driver.page_source
print(r)
soup = BeautifulSoup(r, 'html.parser')
for link in soup.find_all('a'):
    try:
        print(link.get('href'))
        if ("http" in (link.get('href'))):
            save_pdf(link.get('href'))
        else:
            save_pdf("https://home.deib.polimi.it/fornacia/lib/exe/fetch.php?media=" + link.get('href'))
    except:
        pass
print("Firefox Browser Initialized in Headless Mode")
driver.quit()
print("Driver Exited")