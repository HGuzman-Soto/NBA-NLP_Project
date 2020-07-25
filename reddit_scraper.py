import praw
import pandas as pd
import datetime as dt
import os


def main():
    #category = argv[2] #give it a category
    reddit = praw.Reddit(client_id="CIiRpIvsdkRJ8A",
                        client_secret=os.environ.get('client_secrets'),
                        user_agent="NBA_Scraper",
                        username=os.environ.get('reddit_user'),
                        password=os.environ.get('reddit_pwd'))

    subreddit = reddit.subreddit('nba')
    top_subreddit = subreddit.top(limit=100000)
    hot_subreddit = subreddit.hot(limit=100000)
    controversial_subreddit = subreddit.controversial(limit=100000)
    rising_subreddit = subreddit.rising(limit=100000)
    
    category = ['top', 'hot', 'controversial', 'rising']


    topics_dict = { "title":[], \
                "score":[], \
                "id":[], \
                "url":[], 
                "comms_num": [], \
                "created": [], \
                "body":[], \
                "upvote_ratio":[], \
                "category":[]\
                }

    for submission in rising_subreddit:
        if validfy(submission.title, submission.selftext.strip()):
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["url"].append(submission.url)
            topics_dict["comms_num"].append(submission.num_comments)
            topics_dict["created"].append(submission.created)
            topics_dict["body"].append(submission.selftext.strip())
            topics_dict["upvote_ratio"].append(submission.upvote_ratio)
            topics_dict["category"].append("rising")

        topics_data = pd.DataFrame(topics_dict)
        _timestamp = topics_data["created"].apply(get_date)
        topics_data = topics_data.assign(timestamp = _timestamp)

        topics_data.to_csv('reddit_posts_rising.csv') 

def get_date(created):
    return dt.datetime.fromtimestamp(created)


""" Checks to see if following conditions are met
    1) Body content is at least 1500 characters
    2) Does not contain 'streamable' in body 
    3) Also want to get rid of boxscore stuff '[Post Game Thread] in the title
    
"""
def validfy(title, post):
    if len(post) > 500:
        if '[Post Game Thread]' not in title:
            if 'streamable' or '[Post Game Thread]' or '|^[nbaboxscoregenerator.com](http://www.nbaboxscoregenerator.com) ^by ^/u/Obi-Wan_Ginobili|' not in post:
                return True
    return False


if __name__ == "__main__":
    main()