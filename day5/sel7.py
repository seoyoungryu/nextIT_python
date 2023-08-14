from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
chromedriver_autoinstaller.install()
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f'--user-argent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) # 3초 대기
url='https://comic.naver.com/webtoon/detail?titleId=793130&no=1'
driver.get(url)
time.sleep(3)
import util
util.fullpage_screenshot(driver, '방과후.png')
driver.close()