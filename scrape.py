from twitterscraper import query_tweets
import csv
import datetime as dt

dataFields = {
    "text": 0,
    "hashtags": 0,
    "likes" : 0,
    "has_media" : 0,
    "retweets" : 0,
    "img_urls" : 0,
    "screen_name": 0,
    "timestamp" : 0,
    "is_replied" : 0,
    "is_reply_to" : 0,
    "parent_tweet_id" : 0,
    "replies" : 0,
    "tweet_id" : 0,
    "tweet_url" : 0,
    "user_id" : 0,
    "username" : 0
    #"video_url" : 0
}

if __name__ == '__main__':
    # Takes tweets from date
    date = dt.date.today()
    limit = 1000
    lang = 'english'

    with open('data_' + str(date) + '.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        fields = []
        count = 0
        #write first row
        for x in dataFields:
            fields.append(x)
        writer.writerow(fields)
        
        tomorrow = date + dt.timedelta(days=1)
        for tweet in query_tweets("#NBA",
                              limit = limit,
                              begindate=date,
                              enddate=tomorrow,
                              lang = lang
                                  ):
            #Store Tweets without videos
            if(tweet.video_url == ''):
                #Gather info for row
                fields = []
                
                fields.append(tweet.text)           # string
                
                #array type hashTags
                hashtags = ''
                for hashtag in (tweet.hashtags):
                    if (hashtags == ''):
                        hashtags = hashtag
                    else:
                        hashtags = hashtags + '|' + hashtag
                fields.append(hashtags)
                
                fields.append(tweet.likes)          # int
                fields.append(tweet.has_media)      # bool
                fields.append(tweet.retweets)       # int

                #array type URL
                urls = ''
                for url in (tweet.img_urls):
                    if (urls == ''):
                        urls = url
                    else:    
                        urls = url + '|' + urls
                fields.append(urls)
                
                fields.append(tweet.screen_name)    # string
                fields.append(tweet.timestamp)      # string
                fields.append(tweet.is_replied)     # bool
                fields.append(tweet.is_reply_to)    # bool
                fields.append(tweet.parent_tweet_id)# string
                fields.append(tweet.replies)        # int
                fields.append(tweet.tweet_id)       # string
                fields.append(tweet.tweet_url)      # string
                fields.append(tweet.user_id)        # int
                fields.append(tweet.username)       # string

                #write row
                writer.writerow(fields)
                count = count + 1

    print("Num Found: " + str(count))

                
        

