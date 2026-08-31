import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
browser.maximize_window()

browser.switch_to.frame("iframeResult")

elem = browser.find_element(By.XPATH, '//*[@id="html"]')

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택하기.")
    elem.click()
else:
    print("선택되어 있으므로 선택하지 않기.")

time.sleep(3)

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택하기.")
    elem.click()
else:
    print("선택되어 있으므로 선택하지 않기.")

time.sleep(3)

browser.quit()
