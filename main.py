'''

This is the main python server application.

This is to store the user account and quiz_game's quiz.

'''
from flask import Flask,request,url_for,render_template,redirect
#import database to use the database.
import Database1
import setting
import time
import pdb
import os

#This is to start the main aplication
app=Flask(__name__)

# Main UI of application.
@app.route('/')
def main():
	return render_template('main.html')

# Head part of UI.
@app.route('/heading')
def heading():
	return render_template('heading.html')
	# Main_page to show html page to show question to users.
@app.route('/main_page')
def main_page():
	return render_template('main_page.html')
# It will show a main_page2 html page 
# Which will show the question page.
@app.route('/main_page2')
def main_page2():
	return render_template('main_page2.html')
# Starting of score and question increment value
def increquest():
	i=0
	score=0
	return i,score

# To import the question direct by .csv files.
@app.route('/fileupload',methods=['POST'])
def fileupload():
	questfile=request.files['files']
	# Save the file in server.
	questfile.save(os.path.join(app.config["image_upload"],questfile.filename))
	# Open and read the file.
	dfile=open(questfile.filename,"r").read().strip()
	data=dfile.split('\n')
	print(data)
	m=[]
	#Try exxcept block to handle exception.
	if dfile[0] is not None:
		for x in range(len(data)):
			print(x)
			m.append(data[x].split(' , '))
	else:
		return "<p style='font-size:30px'>You inserted a  blank file.</p>"
	print(m)
	for x in range(len(m)):
		if len(m[x])==6:
			Database1.insert_quest(m[x][0],m[x][1],m[x][2],m[x][3],m[x][4],m[x][5])
		else:
			return f"<p style='font-size:30px'>Missing parameter in line {x}</p>"
	return redirect('/main_page2')
	
#It is the starting page of the application.
@app.route('/starting')
def starting():
	i,score=increquest()
	return render_template('starting_page.html',i=i,score=score)
'''
This part is to show question and record the response.
	process the response and show the score.
	'''

#It will loop the question again and again.
@app.route('/main_page1',defaults={'i':0,'score':0})
@app.route('/main_page1/<int:i>/<int:score>')
def main_page1(i,score):
	# It call the database's question list from databases.
	question2=Database1.showquest(i)
	#To end the loop.
	if question2 !=0:
		z=question2[0]
		a=question2[1]
		b=question2[2]
		c=question2[3]
		d=question2[4]
		e=question2[5]
		f=question2[6]
		# It will show and pass the values to html page.
		return render_template('main_page1.html',\
			a=a,b=b,c=c,d=d,e=e,f=f,i=i,score=score)
	else:
		# If the loop ends then it will shows the end page. 
		return render_template('test.html',score=score,i=i)
# It will loop the question.
@app.route('/showquest/<int:i>/<int:score>')
def showquest(i,score):
	i+=1
	return redirect(url_for('main_page1',i=i,score=score))

# End of game and count score.
@app.route('/end/<int:i>/<int:score>')
def end(i,score):
	return render_template('test.html',score=score,i=i)

# Count the score of User.
@app.route('/score1/<z>/<m>/<int:i>/<int:score>')
def score1(z,m,i,score):
	if z==m:
		score=score+1
	return redirect(url_for('showquest',i=i,score=score))

# This function receive the question from user.  
@app.route('/question1',methods=['POST'])
def question():
	# Receive the question and option through request form/
	question=request.form['question']
	option1=request.form['option1']
	option2=request.form['option2']
	option3=request.form['option3']
	option4=request.form['option4']
	answer=request.form['answer']
	# Insert the question in database.
	Database1.insert_quest(question,\
	option1,option2,option3,option4,answer)
	return redirect('/main_page2')
#	except:
#		return "<p style='font-size:40px'>Insert a full content</p>"
	'''
To create a sign up UI for user.

This will store the user info for short time.
'''
# Shows to create a sign up page
@app.route('/creation')
def creation():
	return render_template('Acc_creation.html')

# It's insert the information of user.
@app.route('/create',methods=['POST'])
def create():
	first=request.form['firstname']
	last=request.form['lastname']
	email=request.form['email']
	password=request.form['password']
	# It insert into database.
	Database1.insert_acc(first,last,email,password)
	return redirect('/login')

#To login
@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/auth',methods=['POST'])
def auth():
	email=request.form['email']
	password=request.form['password']
	return redirect('/starting')
currentdirec=os.getcwd()
fileloc=os.getcwd()
app.config["image_upload"]=fileloc

# To start the Application.
if __name__=='__main__':
	app.run(debug="true")