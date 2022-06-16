from bs4 import BeautifulSoup
import requests

url = "https://coreyms.com/"
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):

	headline = article.header.h2.a.text
	date = article.header.p.time.text
	author = article.header.p.span.a.span.text
	summary = article.find('div', class_='entry-content').p.text

	try:
		vid_source = article.find('iframe', class_='youtube-player')['src']
		vid_id = vid_source.split('/')[4]
		vid_id = vid_id.split('?')[0]
		vid_link = f'https://youtube.com/watch?v={vid_id}'
	except Exception as e:
		vid_link = "This article has no video"
	
	print("-"*70 + "\n")
	print(headline + "\n")
	print(f"Date Created : {date}")
	print(f"Author       : {author}")
	print("\n" + summary + "\n")
	print(f"Video Link   : {vid_link}" + "\n")
