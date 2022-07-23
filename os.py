### https://youtu.be/ve2pmm5JqmI

import os
from datetime import datetime

class f_manager:

	def __init__(self):
		self.directory = os.chdir('C:\\Users\\samsa\\Downloads')

	def f_list(self):
		f_dir = self.directory
		for f in os.listdir():
			f_name, f_ext = os.path.splitext(f)
			print(f_name)

	def f_rename(self):
		f_dir = self.directory

		for f in os.listdir():
			f_name, f_ext = os.path.splitext(f)

			if f_name == 'Laporan Rekap Presensi Kantor Pelayanan Pajak Daerah Daerah Istimewa Yogyakarta di Kabupaten Bantul':
				f_date = datetime.today().strftime("%Y-%m")
				f_new_name = '{}{}'.format('Presensi ', f_date)
				os.rename(f, f_new_name)

f_manager().f_rename()
