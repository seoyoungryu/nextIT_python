# pip install selenium
import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
chromedriver_autoinstaller.install()
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) #대기
url = 'http://127.0.0.1:5500/seltest/test2.html'
driver.get(url)

window_handler = driver.window_handles
driver.switch_to.window(window_handler[1]) #[0]번째가 부모(최초 페이지)
time.sleep(1)
driver.find_element(By.ID, 'btn').click()
time.sleep(1)
driver.switch_to.window(window_handler[0])

# 만약 confirm 일 경우 취소는 dismiss()
driver.execute_script('fn_check()') # execute_script : 스크립트 호출
div = driver.find_element(By.ID, 'div_id')
lis = div.find_elements(By.TAG_NAME, 'li')
for li in lis:
    print(li.text)
driver.quit()