import psycopg2
import logging
import random

def get_connection_and_cursor():
    conn = psycopg2.connect(
        database="d2j8ncse346lns",
        user = "yriywxkxtklqar",
        password = "b1903aed1d43f99f0afc8975190147390f805e061e824beb4ba4a106316e78dc",
        host = "ec2-54-197-238-238.compute-1.amazonaws.com",
        port = "5432"
     )
    mycursor=conn.cursor()
    return conn, mycursor

# Insert account informtion.
def insert_acc(First,last,email,password):
	conn,mycursor=get_connection_and_cursor()
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
	conn,mycursor=get_connection_and_cursor()
	sql="insert into question(id,question,option1,option2,option3,\
	option4,answer)values (%s,%s,%s,%s,%s,%s,%s)"
	m=[]
	k=1
	mycursor.execute('select * from question')
	mylist=mycursor.fetchall()
	for x in mylist:
		m.append(x[1])
		k=x[0]
	if question in m:
		logging.error("--------Already have that-----")
	else:
		k=k+1
		val=(k,question,option1,option2,option3,option4,answer)
		mycursor.execute(sql,val)
		logging.error("-------Insert Successfully------")
		conn.commit()
'''
 To display the item and item status.

 It loop through the database.

'''

def display_quest():
	conn,mycursor=get_connection_and_cursor()
	mycursor.execute("select * from question")
	mylist=mycursor.fetchall()
	return mylist

mylist=display_quest()
random.shuffle(mylist)

def showquest(i):
	global mylist
	if len(mylist)!=i:
		return mylist[i]
	else:
		return 0
# To login to the website.
def show(email,password):
	conn,mycursor=get_connection_and_cursor()
	mycursor.execute('select email,password from account')
	mylist=mycursor.fetchall()
	for x in range(len(mylist)):
		if mylist[x][0]==email and mylist[x][1]==password:
			return True
# To check duplicate.
def check_duplicate(email):
	conn,mycursor=get_connection_and_cursor()
	mycursor.execute('select email from account')
	mylist=mycursor.fetchall()
	for x in range(len(mylist)):
		if email == mylist[x][0]:
			return False
	else:
		return  True