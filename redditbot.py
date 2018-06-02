

import praw
import wikipedia
"""
reddit = praw.Reddit(client_id = 'L6dh5QXiOn-94w',
                        client_secret = 'L6dh5QXiOn-94w',
                        username = 'TheZotBot',
                        password = 'password',
                        user_agent = 'web:WikiBot:1.0 (by /u/TheZotBot)')

"""

reddit = praw.Reddit(client_id= "L6dh5QXiOn-94w",
                    client_secret = "_pYdC48G2MprJv7keGumzkeYPcs",
                    username = "throw_away_202514",
                    password = "password",                                     
                    user_agent = 'web:WikiBot:1.0 (by /u/throw_away_202514)')


subreddit = reddit.subreddit('test')
posts = subreddit.new(limit = 5)


for p in posts:
    p.comments.replace_more(limit=None)
    for comment in p.comments.list():
        if "uciWikiBot:" in comment.body:
            keyword = comment.body.split(':')[-1]
            print(keyword)
            comment.reply(wikipedia.summary(keyword, sentences=3))
        print("Comment posted")
