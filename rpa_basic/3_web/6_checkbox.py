import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

# iframe 전환
browser.switch_to.frame('iframeResult')
elem = browser.find_element(By.ID, "vehicle1")

if elem.is_selected() == False:
    print("선택되어 있지 않아서 체크합니다.")
    elem.click()
else:
    print("선택되어 있기 때문에 체크 하지 않음.")

time.sleep(3)
browser.quit()