import requests
import bs4
import urllib

utube_playlist_link = "https://www.youtube.com/watch?v=uXMTq81jG7Y&list=PL786bPIlqEjRDXpAKYbzpdTaOYsWyjtCX"

def main():
	request = requests.get( utube_playlist_link )
	beaut_soup = bs4.BeautifulSoup(request.text, "html.parser")

	# page_to_write = beaut_soup.select(".overlay-time-status-renderer")
	# page_text_format = page_to_write[0].getText()

	text = str( beaut_soup )

	def writeDataInFile(file, text):
		my_file = open(file, 'w', encoding="utf-8")
		my_file.write(text)
		my_file.close()

	writeDataInFile("utube_file.html", text)

if __name__ == '__main__':
	main()