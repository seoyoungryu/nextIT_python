# pip install selenium
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
# pip install chromedriver_autoinstaller
chromedriver_autoinstaller.install()
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) #대기
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
time.sleep(1)
soup = BeautifulSoup(driver.page_source,'html.parser')
div = soup.select_one('#tb_list')
trs = div.find_all('tr')
for i,tr in enumerate(trs):
    if i > 0:
        print(i,'등',tr.find_all('td')[5].select_one('a').getText())
        print('='*100)
    #print(tr.getText())

# 화면 접근
# div = driver.find_element(By.ID, 'tb_list')
# trs = div.find_elements(By.TAG_NAME,'tr')
# for tr in trs:
#     print(tr)
# driver.quit()