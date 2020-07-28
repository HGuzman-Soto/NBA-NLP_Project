from bs4 import BeautifulSoup

import requests 

import re

import csv

NBA_HTML = requests.get('https://www.nba.com/').text

NBA_Scraper = BeautifulSoup(NBA_HTML, 'lxml')

NBA_File = open('NBA_Scrape_File.csv', 'a')

CSV_Writer = csv.writer(NBA_File)

CSV_Writer.writerow(['Headline', 'Author credits', 'Date and Time', 'Text'])

Latest_HeadLines = NBA_Scraper.find('div', class_= "content_list--item_wrapper")

for Link in Latest_HeadLines.find_all('a', href = True):

    try:
        Article_HTML = requests.get('https://www.nba.com' + Link['href']).text
        Article_Scraper = BeautifulSoup(Article_HTML, 'lxml')
        Headline = Article_Scraper.find('h1', class_= "article__detail--header-text").text
        Author_Credits = Article_Scraper.find('div', class_= "article__detail--writer-profile")
        Credits = []
        for credit_text in Author_Credits.find_all('p'):
            Credits.append(credit_text.text)
    
        Article_text = ""
        for text in Article_Scraper.find_all(['p','h3']):
           Article_text= "\n" + Article_text + "\n" + text.text

        if len(Credits) == 2:
            CSV_Writer.writerow([Headline, Credits[0], Credits[1], Article_text])
    
        if len(Credits) == 1:
            CSV_Writer.writerow([Headline, Credits[0], "null", Article_text])
    except:
        CSV_Writer.writerow(["null","null","null", "null"])
        
   
    
    



   
        