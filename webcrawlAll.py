#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# to set the browser options
from selenium.webdriver.chrome.options import Options
# to set the wait time before moving to the next page
from selenium.webdriver.support import expected_conditions as EC
# to save python objects
import pickle as pk
import json


def search_google(query, driver):
    driver.get(query)
    link_href = []
    while True:
        search_results = []
        # finds all the search boxes in a page
        search_results = driver.find_elements_by_css_selector('h3.r')
        for x in range(0,len(search_results)):
        # TODO: Associate each link with the rank it appeared on google
            link = search_results[x].find_element_by_tag_name('a')
            link_href.append(link.get_attribute('href'))
        # Goes to the next page
        try:
            next_page = driver.find_element_by_css_selector('a#pnnext.pn')
            next_page.click()
        except:
            print("There are no more pages to parse.")
            break
    return link_href

def setDriver():
    options = Options()
    # options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox') # Bypass OS security model
    options.add_argument('--disable-gpu')  # applicable to windows os only
    options.add_argument('start-maximized') #
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome('/home/alex/Documents/GitHubRepositories/PCAT/PCATx CORE/chromedriver', chrome_options=options)
    return driver

def crawlerWrapper(search_query, engine):
    """
        Takes in the query to search for on a portal
        Currently supported portals:
            1. Google
        INPUT:
            search_query: STRING, spaced string as query to be searched
            #TODO: engine: STRING, default: 'google', engine to be used for performing the query
        OUTPUT:
            Returns nothing
            Saves a pickle file with the name: search_query
    """
    driver = setDriver()

    if engine == 'google':
        search_query.replace(" ", "+")
        url = "https://www.google.com/search?q=" + search_query
        links = search_google(url, driver)
    elif engine == 'bloomberg':
        pass
    else:
        print("Engine hasn't been defined yet.")

    with open('data/parsedLinks/{}.pk'.format(search_query), 'wb') as handle:
        pk.dump(links, handle, protocol=pk.HIGHEST_PROTOCOL)
    # search_results = driver.find_element_by_xpath("//html/body/div[@id='main']/div[@id='cnt']/div[@class='mw']/div[@id='rcnt']/div[@class='col']/div[@id='center_col']/div[@id='res']/div[@id='search']//div[@id='ires']/div[@id='rso']/div[@class='bkWMgd']/div[@class='srg']/div[@class='g']")#/div[@class='rc']/div[@class='r']")
    driver.quit()

if __name__ == "__main__":
    crawlerWrapper('Hello I am Himanshu Ahuja what is python we love code wtf', 'google')
    # search_query = "deep learning"
    # search_query.replace(" ", "+")
    # url = "https://www.google.com/search?q=" + search_query
    # # url = "https://chemicalwatch.com/search?q=" + search_query
    # driver = setDriver()
    # links = search_google(url, driver)
    # with open('filename.pickle', 'wb') as handle:
    #     pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # # driver = webdriver.Chrome()
    # # driver.get(url) # opens the URL
    # # search_results = driver.find_element_by_xpath("//html/body/div[@id='main']/div[@id='cnt']/div[@class='mw']/div[@id='rcnt']/div[@class='col']/div[@id='center_col']/div[@id='res']/div[@id='search']//div[@id='ires']/div[@id='rso']/div[@class='bkWMgd']/div[@class='srg']/div[@class='g']")#/div[@class='rc']/div[@class='r']")
    # driver.quit()
# GOING TO ADD THE httrack script here for the terminal.
