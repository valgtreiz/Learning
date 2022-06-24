from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class pemdaBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Chrome(executable_path='E:\\Project - Python\\Webdriver\\chromedriver.exe')

	def login(self):
		bot = self.bot
		bot.get('https://twitter.com/login/')
		time.sleep(3)
		email = bot.find_element_by_name('session[username_or_email]')
		password = bot.find_element_by_name('session[password]')
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(3)
		print('aight nice, login')

	def like_tweet(self, hashtag):
		bot = self.bot
		bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
		time.sleep(3)
		print('aight nice, like_tweet')

feri = pemdaBot('odhy.o4@gmail.com', 'pass')
feri.login()
feri.like_tweet('radiohead')
