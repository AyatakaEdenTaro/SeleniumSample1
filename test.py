from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

url = "https://www.youtube.com/"
driver = webdriver.Chrome("chromedriver.exe")
wait = WebDriverWait(driver,10)
driver.get(url)

# 検索先のページのHTMLを取得
html = driver.page_source.encode('utf-8')
print(html)

driver.close()
driver.quit()