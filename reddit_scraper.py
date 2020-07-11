import requests
import time
import pickle

from urllib.request import urlopen
from selenium import webdriver
from pandas import *
import numpy as np
from sys import argv

def main():

    if argv[1] == "visual":
        test = pickle.load( open( "19-20-nba_player_stats.pkl", "rb" ) )
        print(test)
    if argv[1] == "get":
        browser = launchBrowser()
        getStats(browser)
        


def launchBrowser():
    driver = webdriver.ChromeOptions()

    driver.binary_location = "/Users/soto26938/Applications/Google Chrome"
    driver.add_argument("start-maximized")
    path_to_chromedriver = '/Users/soto26938/Desktop/nba_project/chromedriver' # Path to access a chrome driver

    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    return browser

   

def getStats(browser):
   
    url = "https://stats.nba.com/leaders"
    browser.get(url)
   
    

if __name__ == "__main__":
    main()