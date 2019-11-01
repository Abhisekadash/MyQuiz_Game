import psycopg2
import logging

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
	print(k)
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

def showquest(i):
	conn,mycursor=get_connection_and_cursor()
	mylist1=display_quest()
	if len(mylist1)!=i:
		logging.error("=============",i,"=================")
		return mylist1[i]
	else:
		return 0