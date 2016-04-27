import tweepy

consumer_key = "oGvZ7thstCtTXkMOwzlR3ZIB3";


consumer_secret = "npU9fzTFY1HfeUszQIiSGob7ZcNTlNLdyIYuKrHiKAoJsgV7Fc";

access_token = "713411667934257152-GHSXaz4tGdPi2ep8VKydpsqlGuz3LcD";

access_token_secret = "sUsU42zxZdRHWCfnQ022g5tJoYtkSUsK6MaACc1gMYpsT";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



