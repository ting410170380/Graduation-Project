from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
import os

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://udn.com/news/story/7326/7860139")

import time

time.sleep(2)
aa = driver.find_element(By.XPATH, "/html/body/main/div/section/section")
time.sleep(5)
b = aa.find_element(By.TAG_NAME, "h1")
c = b.text
print(c)

time.sleep(5)
d = aa.find_element(By.TAG_NAME, "figure")
time.sleep(5)
e = d.find_element(By.TAG_NAME, "figcaption")
f = e.text
print(f)

time.sleep(2)
g = driver.find_element(By.XPATH, "/html/body/main/div/section/section/figure/picture/img")
img_url = g.get_attribute("src")    #取出標籤裡面的src屬性值
print(img_url)
local_path = "C:\\Users\\USER\\OneDrive\\桌面\\Project"
urlretrieve(img_url, os.path.join(local_path , "x.jpg"))    #下載圖片

time.sleep(10)
driver.close()
