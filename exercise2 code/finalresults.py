
import sys
import psycopg2

def finalresults(myword):    
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute('SELECT count from Tweetwordcount where word=%s',[myword])
        records = cur.fetchall()
#	print type(records)
	if len(records) == 0:
		print 'Did not find the word:', myword
	else:
        	for rec in records:
                	print "The count for the word", myword, "is:", rec[0], "\n"
      

def final():    
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute('SELECT * from Tweetwordcount')
        records = cur.fetchall()
#	records = list(records)
#	records = map(lambda x:(x[0].lower(), x[1]), records)
        records = sorted(records, key=lambda x: x[0])
        mycounter=0
	for rec in records:
                print "(word:", rec[0], "count:", rec[1], ")"
                #print "count = ", rec[1], "\n"
		mycounter += 1
	print 'total number of records:', mycounter	

if len(sys.argv) > 1: 
    myword = sys.argv[1]
    #print 'myword is', myword
    finalresults(myword)
else:
    final()
