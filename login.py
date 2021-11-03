#hackerszx tech

#modify path
from bs4.builder import TreeBuilder
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import os
# k=open('f.txt')
def get_mail_id():
	path = "C:\Program Files (X86)\chromedriver.exe"
	driver = webdriver.Chrome(path)
	driver.get('https://www.minuteinbox.com/')
	driver.implicitly_wait(10)
	output = driver.page_source

	soup = BeautifulSoup(output, 'lxml')
	result = soup.findAll("span",{"id": "email"})

	l=[]
	print(result)
	l.append(str(result).split(">")[1])
	global t
	t=''.join(l)

	t=t.split('<')[0]

	return (t,driver)

def main():
	path = 'C:\Program Files (X86)\chromedriver.exe'
	driver = webdriver.Chrome(path)
	driver.get('https://www.instagram.com/accounts/emailsignup/?hl=en')
	driver.implicitly_wait(10)

# import pyperclip
# print(pyperclip.paste())


# 	print(pyautogui.position())

# 	time.sleep(10)

# 	print(pyautogui.position())

	email = driver.find_element_by_css_selector("input[name='emailOrPhone']")
	fullname = driver.find_element_by_css_selector("input[name='fullName']")
	username = driver.find_element_by_css_selector("input[name='username']")
	password = driver.find_element_by_css_selector("input[name='password']")

	login_button = driver.find_element_by_xpath("//button[@type='submit']")
	
	# os.system('python3 mail_signup.py')
	
	(line, mail_driver) = get_mail_id()
	
 	# f = open('temp.txt','r')
	# line = f.readline()
	import random
	k='_abcdefghijklmnopqrstuvwxyz_'

	full_name = line
	email_enter=full_name
	username_enter =''.join(random.choices(k,k=random.randint(10,15)))

	
	i='xxxyyyj'
	email.send_keys(email_enter)
	fullname.send_keys(full_name)
	username.send_keys(username_enter)
	password.send_keys(i)

	login_button.click()
	driver.implicitly_wait(2)
	x=driver.find_element_by_xpath('//*[@title="2004"]').click()
	driver.implicitly_wait(1)
	f=driver.find_element_by_xpath('//button[text()="Next"]').click()
	print('Getting page source')
	driver.implicitly_wait(15)
	time.sleep(2)
	
	mail_driver.implicitly_wait(13)
	time.sleep(12)
	mail_driver.find_element_by_id('odpocet').click()
	time.sleep(3)
	
	out = mail_driver.page_source
	soup = BeautifulSoup(out, 'lxml')
	result = soup.findAll("tbody",{"id": "schranka"})
	print(result)
	for item in result:
		print('In For loop')
		item = str(item)
		x = re.findall("...... is your Instagram code", item)
		# x = x[0]
		# x = x[:6]
		x=''.join(x)
		k=x.split('i')
		print(k[0])
	otp=driver.find_element_by_css_selector('input[name="email_confirmation_code"]')

	otp.send_keys(k[0])
	f=driver.find_element_by_xpath('//button[text()="Next"]').click()

	time.sleep(4)
	os.system(f'bash main.sh {t} {i}')
if __name__=="__main__":
	while True:
    		main()
