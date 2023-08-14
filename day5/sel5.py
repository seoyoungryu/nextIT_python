from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
chromedriver_autoinstaller.install()
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) #대기
url = 'https://www.msn.com/ko-kr/news/techandscience'
driver.get(url)
time.sleep(1)
try:
    cnt = 5
    pagedown = 1
    body = driver.find_element(By.TAG_NAME, 'body')
    # cnt 횟수로 스크롤 내려가도록
    while pagedown < cnt:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        pagedown += 1
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.prettify()) #html 구조 출력
except Exception as e:
    print(str(e))
