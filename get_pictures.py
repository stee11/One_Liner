#Steven Kolln

import os
import urllib2
import re
from subprocess import Popen, PIPE


def get_pictures():
	home_dir = os.getcwd()
	roster_url = ".nhl.com/club/roster.htm" #This is where the pictures are downloaded from
	os.chdir(home_dir+"\pics")
	teams = os.listdir(os.getcwd())
	for element in teams: #for each team folder
		os.chdir(os.getcwd()+"\\"+element)  #go into the folder
		response = urllib2.urlopen("http://%s%s" % (element, roster_url)) #request the teams homepage for the player id
		f = open('Response.txt', 'w')
		f.write(response.read())
		f.close()
		with open("Response.txt") as f:
			count = 0
			player_number = ''
			player_name = ''
			for line in f:
				line = line.strip()
				count-=1
				if count == 0:
					player_name = line[line.index("\">")+2:line.index("</a>")]
					download(player_number, player_name)
					#If our regular expression is matched, that means we have an HTML string containing the NHL player ID we need
				if re.match("<td class=\"left playerPopupTrigger\" rel=\""+element+":\d{7}\" width=\"30%\"", line):
					player_number = line[line.index(":")+1:line.index(":")+8] #Get ID
					count = 1
		os.remove("Response.txt")
		os.chdir("..")
	os.chdir(home_dir)

def download(number, name):
	print number
	print name
	picture_url = "http://1.cdn.nhle.com/photos/mugs/"+number+".jpg"
	command = "../../wget.exe "+picture_url #WGET and download picture
	try:
		p = Popen(command)
		output,errcode = p.communicate()
		os.rename(number+".jpg", name+".jpg") #Rename as players name
	except WindowsError: #If the picture is not found, try a diffent site which mirrors NHL.com
		picture_url = "http://3.cdn.nhle.com/nhl/en/v3/photos/mugs/"+number+".jpg"
		command = "../../wget.exe "+picture_url
		p = Popen(command)
		output,errcode = p.communicate()
		os.rename(number+".jpg", name+".jpg")


if __name__ == "__main__":
	get_pictures()