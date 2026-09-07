import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://shopping.naver.com/ns/home')
browser.maximize_window()

time.sleep(5)

browser.find_element(By.ID, 'input_text').send_keys('무선 마우스')
browser.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div/div[2]/div/span/svg').click()

time.sleep(3)
browser.quit()

# 네이버에서 보안 이슈발생으로 쓸수 없는 코드임..

