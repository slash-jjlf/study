from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://naver.com")

time.sleep(5                                                                                                   )

elem = browser.find_element(By.LINK_TEXT, "카페")

elem.click()




