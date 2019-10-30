import psycopg2
conn = psycopg2.connect(
database="myquiz",
user = "postgres",
password = "b1903aed1d43f99f0afc8975190147390f805e061e824beb4ba4a106316e78dc",
host = "ec2-54-197-238-238.compute-1.amazonaws.com",
URL="postgres://yriywxkxtklqar:b1903aed1d43f99f0afc8975190147390f805e\
061e824beb4ba4a106316e78dc@ec2-54-197-238-238.compute-1.amazonaws.com:5432/d2j8ncse346lns",
port = "5432")
mycursor=conn.cursor()
# Insert account informtion.
def insert_acc(First,last,email,password):
	sql="insert into account(firstname,lastname,email,password)\
	 values (%s,%s,%s,%s)"
	val=(First,last,email,password)
	try:
		mycursor.execute(sql,val)
	except Exception as e:
		raise e
	conn.commit()
# insert_items() for insert elements.
def insert_quest(question,option1,option2,option3,option4,answer):
	sql="insert into question(question,option1,option2,option3,\
	option4,answer)values (%s,%s,%s,%s,%s,%s)"
	val=(question,option1,option2,option3,option4,answer)
	mycursor.execute(sql,val)
	conn.commit()
'''
 To display the item and item status.

 It loop through the database.

'''
def display_quest():
	mycursor.execute("select * from question")
	mylist=mycursor.fetchall()
	return mylist

def showquest(i):
	mylist1=display_quest()
	if len(mylist1)!=i:
		return mylist1[i]
	else:
		return 0