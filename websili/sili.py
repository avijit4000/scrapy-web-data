from selenium import webdriver
import pandas as pd
from selenium.webdriver.edge.options import Options
import time
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)

driver.get("https://www.forbes.com/forbes-400/")
driver.maximize_window()
button = driver.find_elements("xpath",'//div[@class="Table_tableBody__1pLud"]/div[1]/div')
name=[]
for i in button:
    name.append(i.find_element("xpath",'//div[@class="Table_tableBody__1pLud"]/div[1]/div'))


