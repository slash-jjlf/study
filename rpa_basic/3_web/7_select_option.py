import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')
browser.maximize_window()

browser.switch_to.frame('iframeResult')

time.sleep(3)
# cars에 있는 element를 찾고, 드롭다운 내부에 있는 3번째 옵션을 선택
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[3]')
# elem.click()

# 텍스트 값을 통해서 선택하는 방법
# 옵션 중에서 텍스트가 Audi인 항목을 선택
elem = browser.find_element(By.XPATH,('//*[@id="cars"]/option[text()="Audi"]'))
elem.click()
                                    
time.sleep(3)
browser.quit()
