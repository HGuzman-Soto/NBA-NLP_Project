import praw
import pandas as pd
import datetime as dt
import os



def main():
    reddit = praw.Reddit(client_id="CIiRpIvsdkRJ8A",
                        client_secret=os.environ.get('client_secrets'),
                        user_agent="NBA_Scraper",
                        username=os.environ.get('reddit_user'),
                        password=os.environ.get('reddit_pwd'))

    subreddit = reddit.subreddit('nba')
    top_subreddit = subreddit.top(limit=500)
    for submission in subreddit.top(limit=100):
        print(submission.title, submission.id, "\n")

    topics_dict = { "title":[], \
                "score":[], \
                "id":[], \
                "url":[], 
                "comms_num": [], \
                "created": [], \
                "body":[]}

    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)
    
    topics_data = pd.DataFrame(topics_dict)
    _timestamp = topics_data["created"].apply(get_date)
    topics_data = topics_data.assign(timestamp = _timestamp)

    topics_data.to_csv('reddit_comments.csv') 

def get_date(created):
    return dt.datetime.fromtimestamp(created)



if __name__ == "__main__":
    main()