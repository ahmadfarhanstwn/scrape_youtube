import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

links = []
titles = []

with open('channel videos.csv', 'r') as f:
    csvreader = csv.reader(f)
    for l in csvreader:
        links.append(l[0])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for link in links:
    driver.get(link)
    videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
    res = ""

    for video in videos:
        title = video.find_element_by_xpath('.//*[@id="video-title"]').text
        res += title + " "

    titles.append([res])

with open('output.csv', 'w') as w:
    writer = csv.writer(w)
    writer.writerows(titles)