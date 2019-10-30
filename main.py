'''

This is the main python server application.

This is to store the user account and quiz_game's quiz.

'''
from flask import Flask,request,url_for,render_template,redirect
#import database to use the database.
import Database1
import time
import pdb
import os
def quizgame():
	#This is to start the main aplication
	app=Flask(__name__)
	j=0
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

# To import the question direct by .csv files.
	@app.route('/fileupload',methods=['POST'])
	def fileupload():
		questfile=request.files['files']
		questfile.save(os.path.join(app.config["image_upload"],questfile.filename))
		dfile=open(questfile.filename,"r").read().split('\n')
		m=[]
		for x in range(len(dfile)):
			m.append(dfile[x].split(' , '))
		print(m)
		for x in range(len(m)):
			print(m[x][0],m[x][1],m[x][2],m[x][3],m[x][4],m[x][5])
			Database1.insert_quest(m[x][0],m[x][1],m[x][2],m[x][3],m[x][4],m[x][5])
		return redirect('/main_page2')
	#It is the starting page of the application.
	@app.route('/starting')
	def starting():
		global score,i
		i=0
		score=0
		return render_template('starting_page.html')
	'''
	This part is to show question and record the response.

	process the response and show the score.

	'''
	#It will loop the question again and again.
	@app.route('/main_page1')
	def main_page1():
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
					a=a,b=b,c=c,d=d,e=e,f=f)
			else:
				# If the loop ends then it will shows the end page. 
				return render_template('test.html',score=score) 
		
	global score
	score=1
	# It will loop the question.
	@app.route('/showquest')
	def showquest():
		global i
		i+=1
		return redirect('/main_page1')

	# Count the score of User.
	@app.route('/score1/<z>/<m>')
	def score1(z,m):
			if z==m:
				global score
				score=score+1
			return redirect('/showquest')
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
	app.config["image_upload"]="F:\Python\MyQuiz Game"
	# To start the Application.
	if __name__=='__main__':
		app.run(debug="true")
quizgame()