from __future__ import absolute_import, print_function, unicode_literals

import re
from streamparse.bolt import Bolt

################################################################################
# Function to check if the string contains only ascii chars
################################################################################
def ascii_string(s):
  return all(ord(c) < 128 for c in s)

class ParseTweet(Bolt):

    def process(self, tup):
        tweet = tup.values[0]  # extract the tweet

        # Split the tweet into words
        words = tweet.split()

        # Filter out the hash tags, RT, @ and urls
        valid_words = []
        for word in words:
            if word.startswith("#"): continue
            if word.startswith("@"): continue
            if word.startswith("RT"): continue
            if word.startswith("http"): continue
	    if word.isdigit(): continue
            if any(d in word for d in'0123456789'): continue
            if any(a in word for a in'@+={[}]^~*$&/%#'): continue
            aword = word.strip('\?><,.:!(;)')
	    aword = word.strip('\"')
	    aword = word.strip('\\')
            aword = aword.lower()

            # now check if the word contains only ascii
            if len(aword) > 0 and ascii_string(word):
                valid_words.append([aword])

        if not valid_words: return

        # Emit all the words
        self.emit_many(valid_words)

        # tuple acknowledgement is handled automatically
