import os
import csv
import sys
from sys import argv

"""
File used to concatenate documents togethers

The folders bbc and bbc_sports must be in the same directory for this script to work
"""

def main():
    if argv[1] == 'bbc':
        directory = './bbc 2'
        headings = ['business', 'entertainment', 'politics', 'sport', 'tech']
        csv_name = argv[1] + '.csv'
    elif argv[1] == "bbc_sports":
        directory = './bbcsport'
        headings = ['athletics', 'cricket', 'football', 'rugby', 'tennis']
        csv_name = argv[1] + '.csv'
    elif argv[1] == "Sports":
        directory = "./SportsArticles"
        headings = ['Raw Data']
        csv_name = argv[1] + '.csv'
    else:
        print("error: specify a correct file")
        return -1


    with open(csv_name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Index", "Content", "Category"])   

    i = 0
    for heading in headings:
        for folder in os.listdir(directory+'/'+heading):
            with open(directory +"/" + heading + "/" +folder, "r", errors="ignore") as fp:
                line = " ".join(fp.read().split())
                with open(csv_name, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    writer.writerow([i, line, heading])
                i+=1

if __name__ == "__main__":
    main()