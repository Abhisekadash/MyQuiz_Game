from flask import requests
from bs4 import BeautifulSoup
import argparse
class Html_wrapper:
	def find_text(self,language,limit):
		urls=[]
		site='https://github.com/trending/'+language+'?since=daily'
		response=requests.get(site)
		html_data = response.text
		soup=BeautifulSoup(html_data,'html.parser')
		j=0
		for h in soup.find_all('h1'):
			if j==0:
				j=j+1
				continue
			a1 = h.find('a')
			urls.append(a1.text)
			j=j+1
			if j==limit+1:
				break
		return urls
	def print_proper(self,urls):
		url1=[]
		for x in urls:
			url1.append(x.strip())
		url2=[]
		l=[]
		for x in url1:
			l=x.split("    ")
			url2.append((l[1]).strip())
		ob1={k:v for (k,v) in (enumerate(url2,1))}
		return ob1
