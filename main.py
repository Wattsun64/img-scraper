from selenium import webdriver
import urllib.request as req
import os

pages = ["https://www.umclubgreaterdetroit.org/gallery/May-2018-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/November-2017-Monthly-Meeting","https://www.umclubgreaterdetroit.org/gallery/November-2017---Vegan-Holiday-Cooking-Class","https://www.umclubgreaterdetroit.org/gallery/October-2017-Networking-Event","https://www.umclubgreaterdetroit.org/gallery/October-2017-Game-Watching-Party-vs-Penn-State","https://www.umclubgreaterdetroit.org/gallery/July-2017-Mirepoix-Summer-Lobster-Bake","https://www.umclubgreaterdetroit.org/gallery/June-2017-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/April-2017-Focus-Hope-Volunteer-Food-Packing","https://www.umclubgreaterdetroit.org/gallery/June-2015-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/June-2016-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/May-2015-U-of-M-Club-of-Greater-Detroit-at-Focus-Hope-Detroit","https://www.umclubgreaterdetroit.org/gallery/March-2015-Alternative-Spring-Break-Student-Visit","https://www.umclubgreaterdetroit.org/gallery/February-2015-Monthly-Meeting","https://www.umclubgreaterdetroit.org/gallery/December-2014---94th-Annual-UMCGD-Football-Bust","https://www.umclubgreaterdetroit.org/gallery/December-2014---Holiday-Networking-Event-at-the-Detroit-Golf-Club","https://www.umclubgreaterdetroit.org/gallery/August-2014-Kickoff-Tipoff-Faceoff-Tailgate-Dinner","https://www.umclubgreaterdetroit.org/gallery/June-2014-Cooking-Class-at-Mirepoix-Cooking-School","https://www.umclubgreaterdetroit.org/gallery/June-2014-Board-of-Governors-Lunch","https://www.umclubgreaterdetroit.org/gallery/June-2014-Golf-Outing","https://www.umclubgreaterdetroit.org/gallery/June-2014-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/May-2014-Detroit-Tigers-vs-Texas-Rangers-Annual-Picnic-Event","https://www.umclubgreaterdetroit.org/gallery/March-2014-Curling-Event-at-the-Detroit-Curling-Club","https://www.umclubgreaterdetroit.org/gallery/March-2014-Alternative-Spring-Break-Student-Visit","https://www.umclubgreaterdetroit.org/gallery/March-2014-Hockey-Outing","https://www.umclubgreaterdetroit.org/gallery/July-2013-U-M-Alumni-Night-at-Bakers-Keyboard-Lounge","https://www.umclubgreaterdetroit.org/gallery/June-2013-Cooking-Class-at-Mirepoix-Cooking-School","https://www.umclubgreaterdetroit.org/gallery/June-2013-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/June-2012-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/May-2012-David-Brandon-U-of-M-Athletic-Director-Addresses-the-U-of-M-Club","https://www.umclubgreaterdetroit.org/gallery/2011-Football-Kickoff-Dinner","https://www.umclubgreaterdetroit.org/gallery/2011-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/2010-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/2009-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/2008-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/2007-Scholarship-Dinner","https://www.umclubgreaterdetroit.org/gallery/2005-Football-Bust"]

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
