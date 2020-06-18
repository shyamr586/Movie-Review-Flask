from datetime import date
import datetime
from flask import Flask, redirect, request, url_for, render_template, session	#all the libraries used to connect python with html
import sqlite3	#library to connect python with a database
import sys	#library containing error messages
from bs4 import BeautifulSoup
import requests
import random


app = Flask(__name__)       # our Flask app
app.secret_key = 'super secret key'		#the secret key
DB_FILE = 'mydb.db'     # file for our Database
day = datetime.datetime.now()
#NOTE: some of the movies are not in use since they had to be deleted due to limited space issues. But the functions are kept to check how they work.



def _insert(name, comment):			#entering values into the guestbook tables after registering
	try:
		params = {'name':name, 'comment':comment}
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()  
		cursor.execute("insert into guestbook VALUES (:name, :comment)",params)
		connection.commit()
		cursor.close()
	
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

def _insert1(username, comment, movie):		#entering values into the comments tables after the user has commented
	try:
		params = {'username':username, 'comment':comment, 'movie':movie}
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()  
		cursor.execute("insert into comments VALUES (:username, :comment, :movie)",params)
		connection.commit()
		cursor.close()
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

def entervalues(username, password, email):		#entering values into the accounts table after registering
	try:
		params = {'username':username, 'password':password, 'email':email}
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()  
		cursor.execute("insert into accounts VALUES (:username, :password, :email)",params)
		connection.commit()
		cursor.close()
		
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/')
def homepage():			#route for the homepage containing function that redirects to homepage
	
	try:
		
		page1 = requests.get("https://collider.com/all-news/")
		soup = BeautifulSoup(page1.content, "html.parser")
		div1 = soup.find(id = "content")
		article = div1.find_all("article")
		
		div2 = article[0].find(class_ = "entry-content")
		p = div2.find(class_="feed-img-p")
		a = p.find("a")
		img = a.find("img")
		src1 = img["src"]
		
		header = div2.find("header")
		h2 = header.find("h2")
		a2 = h2.find("a")
		name1 = a2["title"]
		hrefofsite1 = a2["href"]
		
		div2 = article[1].find(class_ = "entry-content")
		p = div2.find(class_="feed-img-p")
		a = p.find("a")
		img = a.find("img")
		src2 = img["src"]
		
		header = div2.find("header")
		h2 = header.find("h2")
		a2 = h2.find("a")
		name2 = a2["title"]
		hrefofsite2 = a2["href"]
		
		div2 = article[2].find(class_ = "entry-content")
		p = div2.find(class_="feed-img-p")
		a = p.find("a")
		img = a.find("img")
		src3 = img["src"]
		
		header = div2.find("header")
		h2 = header.find("h2")
		a2 = h2.find("a")
		name3 = a2["title"]
		hrefofsite3 = a2["href"]
		
		A = UpdateTable
		A.addtodynamictable(name1,name2,name3)
		
		
		return render_template('index.html',src1 = src1,name1 = name1, hrefofsite1 = hrefofsite1,src2 = src2,name2 = name2, hrefofsite2 = hrefofsite2,src3 = src3,name3 = name3, hrefofsite3 = hrefofsite3)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])


		
@app.route('/all-movies')
def allmovies():		#route for allmovies page containing function that redirects to allmovies page
	
	try:

		currentDay = int (datetime.datetime.now().day)
		currentMonth = int (datetime.datetime.now().month)
		page1 = requests.get("https://www.bbc.com/weather/292223")
		soup = BeautifulSoup(page1.content, "html.parser")
		div1 = soup.find("span",class_="wr-value--temperature--c").get_text()
		stringtemp = div1[:-1]
		temp = int(stringtemp)
		
		
		if (currentDay == 14 and currentMonth == 2):
		
			listmoviesite = ["Forrest Gump","La La Land","Life is Beautiful"]
			randomnumber = random.randint(0,2)
			alt = listmoviesite[randomnumber]
			if (randomnumber==0):
				href = "https://www.amazon.com/Forrest-Gump-Tom-Hanks/dp/B002QVZ71I"
				src = "https://images-na.ssl-images-amazon.com/images/I/41dkwOlFjYL._AC_.jpg"
				
			elif (randomnumber==1):
				href = "https://www.amazon.com/Land-Ryan-Gosling/dp/B01MRR7AUU"
				src = "https://images-na.ssl-images-amazon.com/images/I/91lKGPwlu2L._AC_SY741_.jpg"
				
			elif (randomnumber==2):
				href = "https://www.amazon.com/Beautiful-English-Subtitled-Roberto-Benigni/dp/B00B3EJ0OY"
				src = "https://images-na.ssl-images-amazon.com/images/I/517EeC7lo-L._AC_.jpg"
			
			
			return render_template('all-movies.html',name = alt,href = href, src = src, message = "Since it's Valentine's Day, I recommend:")
			
		elif (currentDay == 31 and currentMonth == 10):
		
			listmoviesite = ["Mama","The Lighthouse","Hereditary"]
			randomnumber = random.randint(0,2)
			alt = listmoviesite[randomnumber]
			if (randomnumber==0):
				href = "https://www.amazon.com/Mama-Jessica-Chastain/dp/B00BZOD63S"
				src = "https://images-na.ssl-images-amazon.com/images/I/61qiAYwLp-L._AC_SL1001_.jpg"
				
			elif (randomnumber==1):
				href = "https://www.amazon.com/Lighthouse-Willem-Dafoe/dp/B07Z3Z6S2X"
				src = "https://images-na.ssl-images-amazon.com/images/I/91Ol1kBTcbL._AC_SY741_.jpg"
				
			elif (randomnumber==2):
				href = "https://www.amazon.com/Hereditary-Toni-Collette/dp/B07DHYSBJ7"
				src = "https://images-na.ssl-images-amazon.com/images/I/91U6sekg9yL._AC_SL1500_.jpg"
			
			
			return render_template('all-movies.html',name = alt,href = href, src = src, message = "Since it's Halloween, I recommend:")
			
		elif (currentDay == 25 and currentMonth == 12):
		
			listmoviesite = ["Home Alone","Elf","The Nightmare Before Christmas"]
			randomnumber = random.randint(0,2)
			alt = listmoviesite[randomnumber]
			if (randomnumber==0):
				href = "https://www.amazon.com/Home-Alone-Macaulay-Culkin/dp/B0031QNMKK"
				src = "https://i.pinimg.com/originals/14/de/51/14de51206eca408919374362065553be.jpg"
				
			elif (randomnumber==1):
				href = "https://www.amazon.com/Elf-Will-Ferrell/dp/B000YHE4AG"
				src = "https://images-na.ssl-images-amazon.com/images/I/51kg5m6wvFL._AC_.jpg"
				
			elif (randomnumber==2):
				href = "https://www.amazon.com/Tim-Burtons-Nightmare-Before-Christmas/dp/B003SI05PG"
				src = "https://images-na.ssl-images-amazon.com/images/I/51-LjrCfgkL._AC_.jpg"
			
			
			return render_template('all-movies.html',name = alt,href = href, src = src, message = "Since it's Christmas (MERRY CHRISTMAS!), I recommend:")
			
		elif (currentDay == 31 and currentMonth == 12 or currentDay == 1 and currentMonth == 1):
		
			listmoviesite = ["The Lord Of The Rings Trilogy","2001: A Space Odyssey","Goodfellas","The Green Mile", "The Shining"]
			randomnumber = random.randint(0,4)
			alt = listmoviesite[randomnumber]
			if (randomnumber==0):
				href = "https://www.amazon.com/Lord-Rings-Picture-Trilogy-Widescreen/dp/B0001VL0K2"
				src = "https://i.pinimg.com/474x/07/5e/4b/075e4ba8757f8b6f7ee1d0a17895632b.jpg"
				
			elif (randomnumber==1):
				href = "https://www.amazon.com/2001-Space-Odyssey-Douglas-Rain/dp/B000GOUXES"
				src = "https://i.ebayimg.com/images/g/fmoAAOSwwJhdP2S7/s-l300.jpg"
				
			elif (randomnumber==2):
				href = "https://www.amazon.com/GoodFellas-Robert-Niro/dp/B0016YBFZ8"
				src = "https://images-na.ssl-images-amazon.com/images/I/51rOnIjLqzL._AC_SY450_.jpg"
				
			elif (randomnumber==3):
				href = "https://www.amazon.com/Green-Mile-Tom-Hanks/dp/B001EBWIPY"
				src = "https://images-na.ssl-images-amazon.com/images/I/51mvJdnlXrL._AC_.jpg"
				
			elif (randomnumber==4):
				href = "https://www.amazon.com/Shining-Jack-Nicholson/dp/B000GOUMPI"
				src = "https://m.media-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY1200_CR80,0,630,1200_AL_.jpg"
			
			
			return render_template('all-movies.html',name = alt,href = href, src = src, message = "Since it's a New Year, let me recommend you some timeless movies:")
		
		else:
			if (temp>=21 and temp<=30):
				listmoviesite = ["The Manxman","Jaws","After the Sunset"]
				randomnumber = random.randint(0,2)
				alt = listmoviesite[randomnumber]
				if (randomnumber==0):
					href = "https://www.amazon.com/Manxman-Digitally-Remastered-Anny-Ondra/dp/B00Q7HAMFS"
					src = "https://m.media-amazon.com/images/M/MV5BOTg2MDQ0MDA1Nl5BMl5BanBnXkFtZTgwNjU5MDE1NTE@._V1_UY1200_CR101,0,630,1200_AL_.jpg"
					
				elif (randomnumber==1):
					href = "https://www.amazon.com/Jaws-Roy-Scheider/dp/B008LY5VHE"
					src = "https://images-na.ssl-images-amazon.com/images/I/51fn%2B3NvC5L._AC_SY741_.jpg"
					
				elif (randomnumber==2):
					href = "https://www.amazon.com/After-Sunset-Pierce-Brosnan/dp/B003UOHT48"
					src = "https://m.media-amazon.com/images/M/MV5BN2YyMmE1MTUtNTg2OS00ZWRiLWFhZTQtZDViM2MyOGJhZDY3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY1200_CR67,0,630,1200_AL_.jpg"
				
				
				return render_template('all-movies.html',name = alt,href = href, src = src, message = "Since it's a little hot outside, I recommend:")
			
			
			elif (temp>=10 and temp<=20): 
				
				listmoviesite = ["The Mist","Silent Hill","Throne Of Blood"]
				randomnumber = random.randint(0,2)
				alt = listmoviesite[randomnumber]
				
				if (randomnumber==0):
					href = "https://www.amazon.com/Mist-weinstein/dp/B003TNM2K6"
					src = "https://i.pinimg.com/originals/9e/f6/a4/9ef6a4c0b60e16c47944e00be076ffe0.jpg"
				
				elif (randomnumber==1):
					href = "https://www.amazon.com/Silent-Hill-Radha-Mitchell/dp/B000I8HIR2"
					src = "https://images-na.ssl-images-amazon.com/images/I/511KLklYqrL._AC_SY450_.jpg"
					
				elif (randomnumber==2):
					href = "https://www.amazon.co.uk/Throne-Blood-Toshiro-Mifune/dp/B01LP42HIW"
					src = "https://images-na.ssl-images-amazon.com/images/I/818X2DFWmJL._SL1500_.jpg"
				
				
				return render_template('all-movies.html',name = alt,href = href, src = src, message = "Since it's a little cold outside, I recommend:")
				
			elif (temp<10):
				listmoviesite = ["Alive","The Grey","The Thing"]
				randomnumber = random.randint(0,2)
				alt = listmoviesite[randomnumber]
				if (randomnumber==0):
					href = "https://www.amazon.com/Alive-Ethan-Hawke/dp/B005FDWAXM"
					src = "https://img.moviepostershop.com/alive-movie-poster-1992-1020190179.jpg"
					
				elif (randomnumber==1):
					href = "https://www.amazon.com/Grey-Liam-Neeson/dp/B007WV05GY"
					src = "https://m.media-amazon.com/images/M/MV5BNDY4MTQwMzc1MV5BMl5BanBnXkFtZTcwNzcwNTM5Ng@@._V1_.jpg"
					
				elif (randomnumber==2):
					href = "https://www.amazon.com/Thing-Kurt-Russell/dp/B000I9WWK4"
					src = "https://m.media-amazon.com/images/M/MV5BNDcyZmFjY2YtN2I1OC00MzU3LWIzZGEtZDA5N2VlNDJjYWI3L2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg"
				
			
				return render_template('all-movies.html',name = alt,href = href, src = src, message = "Since it's pretty cold outside, I recommend:")
				
			elif (temp>30):
				listmoviesite = ["Lawrence of Arabia","Do The Right Thing","12 Angry Men"]
				randomnumber = random.randint(0,2)
				alt = listmoviesite[randomnumber]
				a = div1.find("a")
				if (randomnumber==0):
					href = "https://www.amazon.com/Lawrence-Arabia-Peter-OToole/dp/B0088OINTU"
					src = "https://images-na.ssl-images-amazon.com/images/I/61XBQoogSbL._SY679_.jpg"
					
				elif (randomnumber==1):
					href = "https://www.amazon.com/Do-Right-Thing-Ossie-Davis/dp/B000I9VOGW"
					src = "https://images-na.ssl-images-amazon.com/images/I/61b9qaUhqzL._AC_.jpg"
					
				elif (randomnumber==2):
					href = "https://www.amazon.com/12-Angry-Men-Henry-Fonda/dp/B001MLUHXQ"
					src = "https://upload.wikimedia.org/wikipedia/commons/b/b5/12_Angry_Men_%281957_film_poster%29.jpg"
				
				return render_template('all-movies.html',name = alt,href = href, src = src, message = "Since it's pretty hot outside, I recommend:")
	
	except:
	
		return render_template("errorpage.html",msg = sys.exc_info()[0])
		

@app.route('/account')
def account():			#route for the account page containing function that redirects to account page

	return render_template('account.html')

@app.route('/about')
def about():			#route for the about page containing function that redirects to about page

	return render_template('about.html')

@app.route('/contact-info')
def contactinfo():		#route for the contact info page containing function that redirects to contact info page

	try:
		page2 = requests.get("https://www.bbc.com/weather/292223")
		soup = BeautifulSoup(page2.content, "html.parser")
		div1 = soup.find("span",class_="wr-value--temperature--c").get_text()
		A = UpdateTable
		A.addtoweather(div1)
		return render_template('contact-info.html',temp = div1)
	
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])
	
@app.route('/arrival',methods = ['POST','GET'])
def arrival():			#route for the arrival movie page containing function that redirects to arrival movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'arrival'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("arrival.html",entries=rv)
	
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])
		
	
@app.route('/sign2', methods = ['POST'])
def sign2():			#takes entered comments of arrival movie page to add to table

	_insert1(session['name'],request.form['content'],"arrival")
	return redirect(url_for('arrival'))
	

@app.route('/blade-runner-2049',methods = ['POST','GET'])
def br2049():			#route for the br2049 movie page containing function that redirects to br2049 movie page and loads previous comments 

	try:
		page3 = requests.get("https://www.imdb.com/title/tt1856101/?ref_=nv_sr_srsg_4")
		soup = BeautifulSoup(page3.content, "html.parser")
		wrapper = soup.find(id="wrapper")
		div1 = wrapper.find(id="root")
		div2 = div1.find(id="pagecontent")
		div3 = div2.find(id="content-2-wide")
		div4 = div3.find(id="main_top")
		div5 = div4.find(class_="title-overview")
		div6 = div5.find(id="title-overview-widget")
		div7 = div6.find(class_="vital")
		div8 = div7.find(class_="title_block")
		div9 = div8.find(class_="title_bar_wrapper")
		div10 = div9.find(class_="ratings_wrapper")
		div11 = div10.find(class_="imdbRating")
		div12 = div11.find(class_="ratingValue")
		rating = div12.get_text()
		
		A = UpdateTable
		A.addrating(rating)
		
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'br2049'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("blade-runner-2049.html",entries=rv, rating = rating)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign1', methods = ['POST'])		
def sign1():		#takes entered comments of br2049 movie page to add to table

	_insert1(session['name'],request.form['content'],"br2049")
	return redirect(url_for('br2049'))
	

@app.route('/donnie-darko')
def donnieDarko():		#route for the donnie darko movie page containing function that redirects to donnie darko movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'donniedarko'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("donnie-darko.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign3', methods = ['POST'])
def sign3():		#takes entered comments of donnie darko movie page to add to table

	_insert1(session['name'],request.form['content'],"donniedarko")
	return redirect(url_for('donnieDarko'))

@app.route('/fight-club')
def fightClub():	#route for the fight club movie page containing function that redirects to fight club movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'fight club'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("fight-club.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])
	
@app.route('/sign4', methods = ['POST'])
def sign4():	#takes entered comments of fight club movie page to add to table

	_insert1(session['name'],request.form['content'],"fight club")
	return redirect(url_for('fightClub'))

@app.route('/forrest-gump')
def forrestGump():	#route for the forrest gump movie page containing function that redirects to forrest gump movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'forrest gump'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("forrest-gump.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign5', methods = ['POST'])
def sign5():	#takes entered comments of forrest gump movie page to add to table

	_insert1(session['name'],request.form['content'],"forrest gump")
	return redirect(url_for('forrestGump'))

@app.route('/goodfellas')
def goodfellas():	#route for the goodfellas movie page containing function that redirects to goodfellas movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'goodfellas'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("goodfellas.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])
	
@app.route('/sign6', methods = ['POST'])
def sign6():	#takes entered comments of goodfellas movie page to add to table

	_insert1(session['name'],request.form['content'],"goodfellas")
	return redirect(url_for('goodfellas'))

@app.route('/interstellar')
def interstellar():	#route for the interstellar movie page containing function that redirects to interstellar movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'interstellar'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("interstellar.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign7', methods = ['POST'])
def sign7():	#takes entered comments of interstellar movie page to add to table

	_insert1(session['name'],request.form['content'],"interstellar")
	return redirect(url_for('interstellar'))

@app.route('/john-wick')
def johnwick():	#route for the john wick movie page containing function that redirects to donnie john wick page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'john wick'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("john-wick.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign8', methods = ['POST'])
def sign8():	#takes entered comments of john wick movie page to add to table

	_insert1(session['name'],request.form['content'],"john wick")
	return redirect(url_for('johnwick'))

@app.route('/joker')
def joker():	#route for the joker movie page containing function that redirects to joker movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'joker'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("joker.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign9', methods = ['POST'])
def sign9():	#takes entered comments of joker movie page to add to table

	_insert1(session['name'],request.form['content'],"joker")
	return redirect(url_for('joker'))


@app.route('/leon-the-professional')
def leontheprofessional():	#route for the leon the professional movie page containing function that redirects to leon movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'leon the professional'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("leon-the-professional.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign10', methods = ['POST'])
def sign10():	#takes entered comments of leon the professional movie page to add to table

	_insert1(session['name'],request.form['content'],"leon the professional")
	return redirect(url_for('leontheprofessional'))


@app.route('/oldboy')
def oldboy():	#route for the oldboy movie page containing function that redirects to oldboy movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'oldboy'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("oldboy.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign11', methods = ['POST'])
def sign11():	#takes entered comments of oldboy movie page to add to table

	_insert1(session['name'],request.form['content'],"oldboy")
	return redirect(url_for('oldboy'))

@app.route('/seven-samurai')
def sevensamurai():	#route for the seven samurai movie page containing function that redirects to saven samurai movie page and loads previous comments 

	try:
		page3 = requests.get("https://www.imdb.com/title/tt0047478/?ref_=nv_sr_srsg_0")
		soup = BeautifulSoup(page3.content, "html.parser")
		wrapper = soup.find(id="wrapper")
		div1 = wrapper.find(id="root")
		div2 = div1.find(id="pagecontent")
		div3 = div2.find(id="content-2-wide")
		div4 = div3.find(id="main_top")
		div5 = div4.find(class_="title-overview")
		div6 = div5.find(id="title-overview-widget")
		div7 = div6.find(class_="vital")
		div8 = div7.find(class_="title_block")
		div9 = div8.find(class_="title_bar_wrapper")
		div10 = div9.find(class_="ratings_wrapper")
		div11 = div10.find(class_="imdbRating")
		div12 = div11.find(class_="ratingValue")
		rating = div12.get_text()
		
		A = UpdateTable
		A.addrating(rating)
		
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'seven samurai'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("seven-samurai.html",entries=rv, rating = rating)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign12', methods = ['POST'])
def sign12():	#takes entered comments of seven samurai movie page to add to table

	_insert1(session['name'],request.form['content'],"seven samurai")
	return redirect(url_for('sevensamurai'))

@app.route('/spider-man')
def spiderman():	#route for spiderman movie page containing function that redirects to spider movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'spiderman'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("spider-man.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign13', methods = ['POST'])
def sign13():	#takes entered comments of spiderman movie page to add to table

	_insert1(session['name'],request.form['content'],"spiderman")
	return redirect(url_for('spiderman'))

@app.route('/the-shining')
def theshining():	#route for the shining movie page containing function that redirects to shining movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'the shining'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("the-shining.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign14', methods = ['POST'])
def sign14():	#takes entered comments of shining movie page to add to table

	_insert1(session['name'],request.form['content'],"the shining")
	return redirect(url_for('theshining'))

@app.route('/there-will-be-blood')
def twbb():	#route for there will be blood movie page containing function that redirects to twbb movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'there will be blood'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("there-will-be-blood.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign15', methods = ['POST'])
def sign15():	#takes entered comments of there will be blood movie page to add to table

	_insert1(session['name'],request.form['content'],"there will be blood")
	return redirect(url_for('twbb'))

@app.route('/taxi-driver')
def taxidriver():	#route for taxi driver movie page containing function that redirects to taxi driver movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'taxi driver'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("taxi-driver.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign16', methods = ['POST'])
def sign16():	#takes entered comments of taxi driver movie page to add to table

	_insert1(session['name'],request.form['content'],"taxi driver")
	return redirect(url_for('taxidriver'))

@app.route('/spirited-away')
def spiritedaway():	#route for spirited away movie page containing function that redirects to spirited away movie page and loads previous comments 

	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM comments where movie = 'spirited away'")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("spirited-away.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/sign17', methods = ['POST'])
def sign17():	#takes entered comments of spirited away movie page to add to table

	_insert1(session['name'],request.form['content'],"spirited away")
	return redirect(url_for('spiritedaway'))

@app.route('/guestbook')
def guestbook():	#redirects to the guestbook page
	"""
	An input form for signing the guestbook  
	"""
	return render_template('guestbook.html')

@app.route('/sign', methods=['POST'])
def sign():		#function that enters comments to table (but the entering to table part is in the _insert() function
	"""
	Accepts POST requests, and processes the form;
	Redirect to guestbook when completed.
	"""
	try:
		_insert(request.form['name'], request.form['comment'])
		return redirect(url_for('guestbook'))
	
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])
	

@app.route('/signup', methods=['POST'])
def signup():	#similar to above, used to take values from html page and add to table
	try:
		entervalues(request.form['username'], request.form['password'], request.form['email'])
		return render_template("account.html")

	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])

@app.route('/login', methods=['POST', 'GET'])
def login():	#the login function which checks if the entered name is there in the table or not, if yes it will login and if not it will show error message
	try:
		if request.method == 'POST':
			query = "select * from accounts where username = '" + request.form['username2']
			query = query + "' and password = '" + request.form['password2'] + "';"
			connection = sqlite3.connect(DB_FILE)
			cur = connection.execute(query)
			rv = cur.fetchall()
			cur.close()
			if len(rv) == 1:
				session['logged in'] = True
				session ['wrong details'] = False
				session['name'] = request.form['username2']
				return render_template('all-movies.html')
			else:
				session ['wrong details'] = True
				return render_template('account.html', msg="Username/Password Incorrect!")
		else:
			return render_template('account.html')
			
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged in'] = False
    return render_template('index.html')

@app.route('/view', methods=['GET', 'POST'])
def view():
	"""
	Accepts POST requests, and processes the form;
	Redirect to view when completed.
	"""
	try:
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM guestbook")
		rv = cursor.fetchall()
		cursor.close()
		return render_template("view.html",entries=rv)
		
	except:
		return render_template("errorpage.html",msg = sys.exc_info()[0])


class UpdateTable:

	def addtodynamictable(name1,name2,name3):
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()  
		cursor.execute("insert into dynamictable VALUES (:day, :name);", (day,name1))
		cursor.execute("insert into dynamictable VALUES (:day, :name);", (day,name2))
		cursor.execute("insert into dynamictable VALUES (:day, :name);", (day,name3))
		connection.commit()
		cursor.close()
		
	def addtoweather(temp):
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("insert into weather VALUES (:day, :temperature);", (day,temp))
		connection.commit()
		cursor.close()
		
	def addrating(rating):
		connection = sqlite3.connect(DB_FILE)
		cursor = connection.cursor()
		cursor.execute("insert into rating VALUES (:day, :rating);", (day,rating))
		connection.commit()
		cursor.close()

	

if __name__ == '__main__':
	app.run(debug = True)


