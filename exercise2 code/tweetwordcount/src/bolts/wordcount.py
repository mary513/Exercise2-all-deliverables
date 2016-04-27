from __future__ import absolute_import, print_function, unicode_literals
import psycopg2
from collections import Counter
from streamparse.bolt import Bolt
from redis import StrictRedis

class WordCounter(Bolt):
    conn = None;
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.redis = StrictRedis()

    def process(self, tup):
	word = tup.values[0]
	self.counts[word] += 1
	cur = self.conn.cursor()
	self.emit([word, self.counts[word]])
	self.log('This is the current word in the queue********:%s: %d' % (word, self.counts[word]))

	try:
#	   self.log('try to insert')
	   cur.execute("INSERT INTO Tweetwordcount(word, count) VALUES(%s, 1)", [word])
	   self.conn.commit()
#	   self.log('committed INSERT')
	except:
#	    self.log('could not INSERT try to UPDATE')
	    self.conn.rollback()
#	    self.log('ROLLED BACK THE INSERT')
	    try:
#		self.log('about to try to UPDATE')
		cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word))
		self.conn.commit()
#		self.log('SUCCESSFUL UPDATE')
	    except:
		self.log('could not update the word: %s:', word)

