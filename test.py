import tweepy

auth = tweepy.OAuthHandler('vuk1YqalorIrvOEDXV6zQHLUN', 'u1R2AqI0EYFO1a25jIjDHt7xxURy1HQhRMfHHMqvw5HgaJCMPp')
auth.set_access_token('929365692377456640-XB5BoxmuVLFSbMXBpm8CMhlkcNlQsHh', 'p2LXdMTgmJa4Yc0Rtu0EGjM7QGAgppQEkKjttqx3fnoH9')

api = tweepy.API(auth)

public_tweets = api.home_timeline()

x = 0
for tweet in public_tweets:
    if x == 10:
        break
    print(tweet.text)
    
    
#https://tweepy.readthedocs.io/en/latest/getting_started.html