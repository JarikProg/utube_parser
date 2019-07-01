import requests
import bs4
import urllib

utube_playlist_link = "https://www.youtube.com/playlist?list=PL786bPIlqEjRDXpAKYbzpdTaOYsWyjtCX"
if utube_playlist_link.split("?")[0] == "https://www.youtube.com/playlist":
	is_playlist = True
else:
	is_playlist = False

def main():
	request = requests.get( utube_playlist_link )
	beaut_soup = bs4.BeautifulSoup(request.text, "html.parser")

	# page_to_write = beaut_soup.select(".overlay-time-status-renderer")
	# page_text_format = page_to_write[0].getText()

	text = str( beaut_soup )

	def readAllDataReturnText(file):
		text = ""

		my_file = open(file, 'r', encoding='utf-8')		
		for line in my_file:
			text += line
		my_file.close()

		return text

	def writeDataInFile(file, text):
		my_file = open(file, 'w', encoding="utf-8")
		my_file.write(text)
		my_file.close()

	writeDataInFile("utube_file.html", text)
	
	# read_file = readAllDataReturnText("utube_file.html")
	# print(read_file)

	read_file = bs4.BeautifulSoup( open("utube_file.html", "r", encoding='utf-8'), "html.parser" )

	def getElement(soup, add_text = "", start_with = 0):
		# Returned array
		if add_text == "":
			mb_space = ""
		else:
			mb_space = " "

		# =====================
		if is_playlist == True:
			length_text = soup.select("ul.pl-header-details li")[1].getText()
		else:
			length_text = soup.select("#playlist-length")[0]getText()
		# =====================

		length = int( length_text.split()[0] ) - 1

		# =====================
		if is_playlist == True:
			max_border = 100
		else:
			max_border = 200
		# =====================

		if length - start_with > max_border:
			length = start_with + max_border

		# =====================
		if is_playlist == True:
			list = "tbody#pl-load-more-destination"
			element_class = "tr.pl-video.yt-uix-tile"
		else:
			list = "tbody#pl-load-more-destination"
			element_class = "tr.pl-video.yt-uix-tile"
		# =====================

		array = []

		element_link = "{0} {1}".format( list, element_class )

		for i in range(length):
			# element_link = "{0} {1}".format( list, element_class )
			local_el = soup.select( element_link + mb_space + add_text )[i].getText()

			array.append(local_el)

		return array

	# =====================
	if is_playlist == True:
		time_link = ".timestamp span"
	else:
		time_link = ".timestamp span"
	# =====================
	
	# time_array = getElement(read_file, time_link)
	# time_array = ['9:28', '3:43', '5:45', '11:12', '1:28', '16:55', '11:13', '1:57', '9:02', '4:42', '10:07', '6:38', '8:16', '18:29', '11:48', '11:21', '24:48', '18:56', '8:08', '3:59', '12:52', '7:37', '7:54', '15:38', '20:36', '8:23', '15:19', '24:54', '17:10', '2:30', '5:41', '7:15', '3:22', '29:50', '32:10', '4:32', '9:34', '10:32', '6:41', '10:32', '1:50', '46:49', '7:46', '6:47', '14:05', '20:09', '3:55', '13:25', '38:35', '36:33', '13:01', '25:18', '11:42', '33:33', '11:31', '43:03', '15:03', '6:01', '9:28', '24:44', '22:18', '13:59', '14:48', '9:00', '4:12', '5:08', '2:32', '17:27', '19:19', '18:06', '7:03', '10:09', '8:25', '13:37', '11:01', '8:12', '11:24', '5:50', '6:24', '8:50', '6:46', '9:36', '3:08', '5:42', '5:24', '5:46', '4:41', '6:52', '4:05', '2:51', '14:08', '3:39', '16:07', '27:58', '1:51', '8:10', '5:58', '10:58', '22:21', '5:58']
	# print(time_array)

	def timeConcat(arr):
		hours = 0
		minutes = 0
		seconds = 0
		for times in arr:
			splited_arr = times.split(":") #  Change format "00:00:00" to ["00", "00", "00"]
			local_len = len(splited_arr)
			if local_len == 3:
				hours += int( splited_arr[0] )
			elif local_len < 3:
				minutes += int( splited_arr[0] )
				seconds += int( splited_arr[1] )
			else:
				print("To much arguments!")
				break

		print("Before: {0}:{1}:{2}".format(hours, minutes, seconds))

		minutes += seconds // 60
		hours += minutes // 60
		seconds = seconds % 60
		minutes = minutes % 60


		print("After: {0}:{1}:{2}".format(hours, minutes, seconds))

		# return "{0}:{1}:{2}".format(hours, minutes, seconds)

	# timeConcat(time_array)


	'''page_to_write = read_file.select("ol.playlist-videos-list.yt-uix-scroller.yt-viewport")
	page_text_format = page_to_write[0].getText()
	print( page_text_format )'''

if __name__ == '__main__':
	main()