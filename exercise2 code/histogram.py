





import sys
import psycopg2

def finalresults(lower, upper):
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("SELECT * from Tweetwordcount where count>%s and count<%s;",[lower, upper])
        records = cur.fetchall()
	#print records
	if len(records) == 0:
		print 'No words meet this criteria'
	else:
        	for rec in records:
                	print "The count for the word", rec[0], "is:", rec[1], "\n"
      


if len(sys.argv) > 2: 
    lower = sys.argv[1]
    upper = sys.argv[2]
    #print 'myword is', myword
    finalresults(lower, upper)
else:
    print "Need to numbers as input"

