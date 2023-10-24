from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://mmehrabi.blogsky.com/"
PATH = r'C:\Driver\Chromedriver.exe'
downloadable = []
binaee = []
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url=URL)

pTags = driver.find_elements(By.XPATH, "//div[@class='content-wrapper']//p//a")
for p in pTags:
    downloadable.append(p.get_attribute('href'))

for get in downloadable:
    driver.get(get)
    driver.find_element(By.XPATH, "//button//span[@class='btn-text']").click()
    download = driver.find_element(By.XPATH, "//div[@id='downloadLinkBox']//a")
    download.click()
    # download.click()
    print(f"------------------Downloading---------------- {download.get_attribute('href')}")
    
    
