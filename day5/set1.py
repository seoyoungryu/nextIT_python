# pip install selenium
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
# pip install chromedriver_autoinstaller
chromedriver_autoinstaller.install()
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) #대기
url = 'https://search.naver.com/'
driver.get(url)
time.sleep(1)

driver.find_element(By.ID, 'query').send_keys('하와이')
driver.find_element(By.CSS_SELECTOR,'button.btn-search').click()
time.sleep(3) #검색되는동안 시간
driver.quit()#종료