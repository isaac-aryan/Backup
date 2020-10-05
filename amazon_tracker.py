import requests
from bs4 import BeautifulSoup
import smtplib

URL=input("Paste the URL of the product you want to track...")

budget=float(input("Enter your budget in Rupees (No paise)..."))

headers={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

def send_mail():
	server=smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	sever.login('danskerdenstore@gmail.com', '')

	subject='Price fell down!'
	body='Check the amazon link '

def send_term(converted_price):
	if converted_price<=budget:
		print("The Amazon.in price of your product fell down!")
	else:
		print("The Amazon.in price of your product is still out of budget.")

def check_price():
	page=requests.get(URL, headers=headers)

	soup=BeautifulSoup(page.content, 'html.parser')

	title=soup.find(id="productTitle").get_text()
	price=soup.find(id="priceblock_ourprice").get_text()
	#print(price,type(price))

	converted_price=price[2:]
	intprice=converted_price.split(".")[0]
	intprice=intprice.split(",")
	if len(intprice)==1:
		converted_price=int(intprice[0])

	elif len(intprice)==2:
		converted_price=int(intprice[0])*1000+int(intprice[1])

	elif len(intprice)==3:
		converted_price=int(intprice[0])*100000+int(intprice[1])*1000+int(intprice[2])
	#print(converted_price,type(converted_price))
	
	
	send_term(converted_price)

	print(converted_price)
	print(title.strip())


check_price()




