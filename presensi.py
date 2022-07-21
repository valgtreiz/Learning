###selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

###selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

###other
import time
from datetime import datetime

class presensiBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Chrome(executable_path='D:\\0. Database\\Webdriver\\chromedriver.exe')

	def login(self):
		bot = self.bot
		bot.get('https://presensi2.jogjaprov.go.id/')
		time.sleep(1)
		username = bot.find_element(By.NAME, 'username')
		password = bot.find_element(By.NAME, 'password')
		username.clear()
		password.clear()
		username.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(1)
		print('Login success')

	def download(self):
		bot = self.bot
		bot.get('https://presensi2.jogjaprov.go.id/lap-pres/rekap/?menu_id=15')
		time.sleep(1)

		find_export_mode = bot.find_element(By.ID, 'fatih')
		select_export_mode = Select(find_export_mode)
		select_export_mode.select_by_value("excel")
		
		input_tanggal_mulai = bot.find_element(By.NAME, 'tanggal_mulai')
		input_tanggal_selesai = bot.find_element(By.NAME, 'tanggal_selesai')

		tanggal_mulai = datetime.today().strftime("%Y-%m-01")
		tanggal_selesai = datetime.today().strftime("%Y-%m-%d")

		input_tanggal_mulai.send_keys(tanggal_mulai)
		input_tanggal_selesai.send_keys(tanggal_selesai)
		
		input_nama = bot.find_element(By.NAME, 'nipnama')
		input_nama.send_keys(Keys.RETURN)

		time.sleep(1)

	def quit(self):
		bot = self.bot
		bot.quit()

admin = presensiBot('197708151998032002', 'Feri2022#')

admin.login()
admin.download()
time.sleep(2)
admin.quit()
