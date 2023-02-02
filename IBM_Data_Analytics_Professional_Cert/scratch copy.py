import twint

c = twint.Config()

c.Search = ['Steven Crowder']       # topic
c.Limit = 20     # number of Tweets to scrape
c.Store_csv = True       # store tweets in a csv file
c.Output = "taylor_swift_tweets.csv"     # path to csv file

twint.run.Search(c)