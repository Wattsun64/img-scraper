from selenium import webdriver
import urllib.request as req
import os

pages = []

chrome = webdriver.Chrome("/Users/ecochra/img_scraper/webdrivers/chromedriver")
club_dir = "/Users/ecochra/Downloads/Detroit-Club"

os.mkdir(club_dir)

for page in pages:
    dir_name = page.split("/")[4]
    path = club_dir + "/" + dir_name

    os.mkdir(path)

    chrome.get(page)

    images = chrome.find_elements_by_css_selector("img[id*='imgThumb']")

    for img in images:
        img_src = img.get_attribute("src")

        if img_src.find("_small") != -1:
            img_src = img_src.split("_small")
            img_src = img_src[0] + "_large" + img_src[1]

        file_name = path + "/" + img_src.split("/pg/")[1]

        req.urlretrieve(img_src, file_name)

chrome.close()
