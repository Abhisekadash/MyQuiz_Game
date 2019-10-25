'''
This is the mysql connection with python.

It store the quiz questions like questions options

'''
#import mysql connector for use to connect
import mysql.connector
'''
Using mysql.connector To connect python to database 
by using username password

'''
import time
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="chiku123",
	database="quiz_game"
	)
mycursor=mydb.cursor()
# Insert account informtion.
def insert_acc(First,last,email,password):
	sql="insert into account(First,last,email,password) values (%s,%s,%s,%s)"
	val=(First,last,email,password)
	try:
		mycursor.execute(sql,val)
	except Exception as e:
		raise e
	mydb.commit()
# insert_items() for insert elements.
def insert_quest(question,option1,option2,option3,option4,answer):
	sql="insert into question(question,option1,option2,option3,option4,answer) values (%s,%s,%s,%s,%s,%s)"
	val=(question,option1,option2,option3,option4,answer)
	try:
		mycursor.execute(sql,val)
	except Error as err:
  		print("Something went wrong: {}".format(err))
	mydb.commit()
'''
 To display the item and item status.

 It loop through the database.

'''
def display_quest():
	try:
		mycursor.execute("select * from question")
		mylist=mycursor.fetchall()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
	return mylist

def showquest(i):
	mylist1=display_quest()
	if len(mylist1)!=i:
		return mylist1[i]
	else:
		return 0