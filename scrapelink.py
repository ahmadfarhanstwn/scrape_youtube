import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = 'https://www.channelcrawler.com/eng/results2/507057/page:'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

output = []

for i in range(1, 14):
    nLink = link + str(i)
    driver.get(nLink)
    element = driver.find_elements(By.XPATH ,"//*[@class='channel col-xs-12 col-sm-4 col-lg-3']/h4/a")
    for elem in element:
        output.append([elem.get_attribute("href")])

with open('output1.csv', 'a', newline='') as w:
    writer = csv.writer(w)
    writer.writerows(output)