import tweepy
from textblob import TextBlob 

consumer_key 		= 'nuCCcKoG0CwzTyW39WxWWlSVW'
consumen_secret		= 'IutAmoVEZUkwgrEivasMRnE2KFyFRQux1ZoMtqhIlEiaMYezYd'

access_token		= '1257246690441965568-BMUAt5yO1wqBbkznps9OnFOJp08hd2'
access_token_secret	= '0SDI1NbnxKHdeN6z7cc6aJ8RHgHKBTtReAKPMrXc5gDKp'

auth = tweepy.OAuthHandler(consumer_key, consumen_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
query = input('Masukkan Thread Yang Mau di Cari? ')

public_tweets = api.search(q=[query], count=200)

all_polarity = 0

for tweet in public_tweets:
	print(tweet.text)

	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	all_polarity += analysis.polarity 

	print('')

if all_polarity/100 > 0:
	print(all_polarity/100)
	print('Positive')	
else:
	print(all_polarity/100)
	print('Negative')