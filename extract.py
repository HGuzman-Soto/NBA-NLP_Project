import requests
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from pandas import *
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import *


def main():
    browser = launchBrowser()
    db = getStats(browser)
    visualization(db)


def launchBrowser():
    #Adapted from
    #http://kevincsong.com/Scraping-stats.nba.com-with-python/

    driver = webdriver.ChromeOptions()

    driver.binary_location = "/Users/soto26938/Applications/Google Chrome"
    driver.add_argument("start-maximized")
    path_to_chromedriver = '/Users/soto26938/Desktop/nba_project/chromedriver' # Path to access a chrome driver

    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    return browser

   

def getStats(browser):
    url = "https://stats.nba.com/leaders"
    browser.get(url)
    browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/label/select/option[2]').click()

    browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/select/option[1]').click()
    table = browser.find_element_by_class_name('nba-stat-table__overflow')
    player_ids = []
    player_names = []
    player_stats = []

    for line_id, lines in enumerate(table.text.split('\n')):
        if line_id == 0:
            column_names = lines.split(' ')
        else:
            if line_id % 3 == 1:
                player_ids.append(lines)
            if line_id % 3 == 2:
                player_names.append(lines)
            if line_id % 3 == 0:
                player_stats.append( [float(i) for i in lines.split(' ')] )

    db = pandas.DataFrame({'player': player_names,
                       'gp': [i[0] for i in player_stats],
                       'min': [i[1] for i in player_stats],
                       'pts': [i[2] for i in player_stats],
                       'fgm': [i[3] for i in player_stats], 
                       'fga': [i[4] for i in player_stats],
                       'fg%': [i[5] for i in player_stats],
                       '3pm': [i[6] for i in player_stats],
                       '3pa': [i[7] for i in player_stats],
                       '3p%': [i[8] for i in player_stats],
                       'ftm': [i[9] for i in player_stats],
                       'fta': [i[10] for i in player_stats],
                       'ft%': [i[11] for i in player_stats],
                       'oreb': [i[12] for i in player_stats],
                       'dreb': [i[13] for i in player_stats],
                       'reb': [i[14] for i in player_stats],
                       'ast': [i[15] for i in player_stats],
                       'stl': [i[16] for i in player_stats],
                       'blk': [i[17] for i in player_stats],
                       'tov': [i[18] for i in player_stats],
                       'eff': [i[19] for i in player_stats]
                       }
                     )
    db = db[['player', 
         'gp', 
         'min', 
         'pts', 
         'fgm', 
         'fga', 
         'fg%', 
         '3pm', 
         '3pa', 
         '3p%', 
         'ftm',
         'fta', 
         'ft%', 
         'oreb', 
         'dreb',
         'reb',
         'ast',
         'stl',
         'blk',
         'tov',
         'eff']
      ]

    db.to_html('output.html')
    return db

def visualization(db):
    plt.scatter(db['fga'], db['fg%'])
    plt.xlabel('Field Goals Attempted (per game)', fontsize=14, fontweight='bold')
    plt.ylabel('Field Goal % (per game)', fontsize=14, fontweight='bold')
    plt.xticks(fontsize=12, fontweight='bold')
    plt.yticks(fontsize=12, fontweight='bold')
    plt.xlim([0,30])
    plt.ylim([0,75])
    plt.show()

    

if __name__ == "__main__":
    main()