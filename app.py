#Steven Kolln

import ctypes
import os
import urllib2
import re
from libavg import *

class Application():
	def __init__(self):
		#get screen size
		user32 = ctypes.windll.user32
		self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

		#player and canvas set up
		self.player = avg.Player.get()
		self.canvas = self.player.createMainCanvas(size=(self.screensize[0], self.screensize[1]-75))
		self.rootNode = self.canvas.getRootNode()

		#picture of the ice, teams, and text set up
		self.iceNode = ImageNode(href=os.getcwd()+"\\layout.jpg", pos=(0,0),
		size = (self.screensize[0]/2, self.screensize[1]-75), parent=self.player.getRootNode())
		self.teamsNode = ImageNode(href=os.getcwd()+"\\logos.jpg", pos=(self.screensize[0]/2, self.screensize[1]/10),
		size = (self.screensize[0]/2,self.screensize[1]/3), parent=self.player.getRootNode())
		avg.WordsNode(pos=(self.screensize[0]/1.45,0), font="arial", fontsize = (35),
		text="Select a team", parent=self.rootNode)

		#Event handler for teams
		self.teamsNode.connectEventHandler(avg.CURSORDOWN, avg.MOUSE, self.teamsNode, self.onMouseClick)

		#Dictionary for URL querying (NO LONGER NEEDED)
		self.team_dict = {
			'avalanche' : 'COL',
			'blackhwaks' : 'CHI',
			'bluejackets' : 'CBJ',
			'blues' : 'STL',
			'bruins' : 'BOS',
			'canadiens' : 'MTL',
			'canucks' : 'VAN',
			'capitals' : 'WSH',
			'coyotes' : 'PHX',
			'devils' : 'NJD',
			'ducks' : 'ANA',
			'flames' : 'CGY',
			'flyers' : 'PHI',
			'hurricanes' : 'CAR',
			'islanders' : 'NYI',
			'jets' : 'WPG',
			'kings' : 'LAK',
			'lightning' : 'TBL',
			'mapleleafs' : 'TOR',
			'oilers' : 'EDM',
			'panthers' : 'FLA',
			'penguins' : 'PIT',
			'predators' : 'NSH',
			'rangers' : 'NYR',
			'redwings' : 'DET',
			'sabres' : 'BUF',
			'senators' : 'OTT',
			'sharks' : 'SJS',
			'stars' : 'DAL',
			'wild' : 'MIN',
		}

		#Used for moving text off screen to prevent overlap of text
		self.ran = False
		self.tnode1 = None
		self.tnode2 = None
		self.tnode3 = None
		self.tnode4 = None
		self.tnode5 = None
		self.tnode6 = None
		self.tnode7 = None
		self.tnode8 = None
		self.tnode9 = None
		self.tnode10 = None
		self.tnode11 = None
		self.tnode12 = None

	def onMouseClick(self, event):
		#Get height and width of each team box
		box_width = (self.screensize[0]/2)/6
		box_height = box_width/2.26 #2.26 is the ratio of width to height

		#determine which box was clicked based of x and y location

		#clicks positions are based off what percentage of the screen is clicked.
		#This should keep it consistent accross all monitor sizes


		#collumn 1
		if (event.x >= self.screensize[0]/2 and event.x <= (self.screensize[0]/2) + box_width) and \
		(event.y >= self.screensize[1]/10 and event.y <= (self.screensize[1]/10) + box_height):
			self.showPlayers("canadiens")

		if (event.x >= self.screensize[0]/2 and event.x <= (self.screensize[0]/2) + box_width) and \
		(event.y >= (self.screensize[1]/10 + (box_height*1)) and event.y <= (self.screensize[1]/10 + (box_height*2))):
			self.showPlayers("lightning")

		if (event.x >= self.screensize[0]/2 and event.x <= (self.screensize[0]/2) + box_width) and \
		(event.y >= (self.screensize[1]/10 + (box_height*2)) and event.y <= (self.screensize[1]/10 + (box_height*3))):
			self.showPlayers("panthers")

		if (event.x >= self.screensize[0]/2 and event.x <= (self.screensize[0]/2) + box_width) and \
		(event.y >= (self.screensize[1]/10 + (box_height*3)) and event.y <= (self.screensize[1]/10 + (box_height*4))):
			self.showPlayers("bluejackets")

		if (event.x >= self.screensize[0]/2 and event.x <= (self.screensize[0]/2) + box_width) and \
		(event.y >= (self.screensize[1]/10 + (box_height*4)) and event.y <= (self.screensize[1]/10 + (box_height*5))):
			self.showPlayers("senators")


		#collumn 2
		if (event.x >= (self.screensize[0]/2)+(box_width*1) and event.x <= (self.screensize[0]/2) + (box_width *2)) and \
		(event.y >= self.screensize[1]/10 and event.y <= (self.screensize[1]/10) + box_height):
			self.showPlayers("kings")

		if (event.x >= (self.screensize[0]/2)+(box_width*1) and event.x <= (self.screensize[0]/2) + (box_width *2)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*1)) and event.y <= (self.screensize[1]/10 + (box_height*2))):
			self.showPlayers("flyers")

		if (event.x >= (self.screensize[0]/2)+(box_width*1) and event.x <= (self.screensize[0]/2) + (box_width *2)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*2)) and event.y <= (self.screensize[1]/10 + (box_height*3))):
			self.showPlayers("bruins")

		if (event.x >= (self.screensize[0]/2)+(box_width*1) and event.x <= (self.screensize[0]/2) + (box_width *2)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*3)) and event.y <= (self.screensize[1]/10 + (box_height*4))):
			self.showPlayers("avalanche")

		if (event.x >= (self.screensize[0]/2)+(box_width*1) and event.x <= (self.screensize[0]/2) + (box_width *2)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*4)) and event.y <= (self.screensize[1]/10 + (box_height*5))):
			self.showPlayers("redwings")


		#collumn 3
		if (event.x >= (self.screensize[0]/2)+(box_width*2) and event.x <= (self.screensize[0]/2) + (box_width *3)) and \
		(event.y >= self.screensize[1]/10 and event.y <= (self.screensize[1]/10) + box_height):
			self.showPlayers("predators")

		if (event.x >= (self.screensize[0]/2)+(box_width*2) and event.x <= (self.screensize[0]/2) + (box_width *3)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*1)) and event.y <= (self.screensize[1]/10 + (box_height*2))):
			self.showPlayers("capitals")

		if (event.x >= (self.screensize[0]/2)+(box_width*2) and event.x <= (self.screensize[0]/2) + (box_width *3)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*2)) and event.y <= (self.screensize[1]/10 + (box_height*3))):
			self.showPlayers("wild")

		if (event.x >= (self.screensize[0]/2)+(box_width*2) and event.x <= (self.screensize[0]/2) + (box_width *3)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*3)) and event.y <= (self.screensize[1]/10 + (box_height*4))):
			self.showPlayers("islanders")

		if (event.x >= (self.screensize[0]/2)+(box_width*2) and event.x <= (self.screensize[0]/2) + (box_width *3)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*4)) and event.y <= (self.screensize[1]/10 + (box_height*5))):
			self.showPlayers("hurricanes")


		#collumn 4
		if (event.x >= (self.screensize[0]/2)+(box_width*3) and event.x <= (self.screensize[0]/2) + (box_width *4)) and \
		(event.y >= self.screensize[1]/10 and event.y <= (self.screensize[1]/10) + box_height):
			self.showPlayers("flames")

		if (event.x >= (self.screensize[0]/2)+(box_width*3) and event.x <= (self.screensize[0]/2) + (box_width *4)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*1)) and event.y <= (self.screensize[1]/10 + (box_height*2))):
			self.showPlayers("jets")

		if (event.x >= (self.screensize[0]/2)+(box_width*3) and event.x <= (self.screensize[0]/2) + (box_width *4)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*2)) and event.y <= (self.screensize[1]/10 + (box_height*3))):
			self.showPlayers("blackhawks")

		if (event.x >= (self.screensize[0]/2)+(box_width*3) and event.x <= (self.screensize[0]/2) + (box_width *4)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*3)) and event.y <= (self.screensize[1]/10 + (box_height*4))):
			self.showPlayers("ducks")

		if (event.x >= (self.screensize[0]/2)+(box_width*3) and event.x <= (self.screensize[0]/2) + (box_width *4)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*4)) and event.y <= (self.screensize[1]/10 + (box_height*5))):
			self.showPlayers("stars")	


		#collumn 5 penguins rangers oilers devils sabres
		if (event.x >= (self.screensize[0]/2)+(box_width*4) and event.x <= (self.screensize[0]/2) + (box_width *5)) and \
		(event.y >= self.screensize[1]/10 and event.y <= (self.screensize[1]/10) + box_height):
			self.showPlayers("penguins")

		if (event.x >= (self.screensize[0]/2)+(box_width*4) and event.x <= (self.screensize[0]/2) + (box_width *5)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*1)) and event.y <= (self.screensize[1]/10 + (box_height*2))):
			self.showPlayers("rangers")

		if (event.x >= (self.screensize[0]/2)+(box_width*4) and event.x <= (self.screensize[0]/2) + (box_width *5)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*2)) and event.y <= (self.screensize[1]/10 + (box_height*3))):
			self.showPlayers("oilers")

		if (event.x >= (self.screensize[0]/2)+(box_width*4) and event.x <= (self.screensize[0]/2) + (box_width *5)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*3)) and event.y <= (self.screensize[1]/10 + (box_height*4))):
			self.showPlayers("devils")

		if (event.x >= (self.screensize[0]/2)+(box_width*4) and event.x <= (self.screensize[0]/2) + (box_width *5)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*4)) and event.y <= (self.screensize[1]/10 + (box_height*5))):
			self.showPlayers("sabres")


		#collumn 6
		if (event.x >= (self.screensize[0]/2)+(box_width*5) and event.x <= (self.screensize[0]/2) + (box_width *6)) and \
		(event.y >= self.screensize[1]/10 and event.y <= (self.screensize[1]/10) + box_height):
			self.showPlayers("canucks")

		if (event.x >= (self.screensize[0]/2)+(box_width*5) and event.x <= (self.screensize[0]/2) + (box_width *6)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*1)) and event.y <= (self.screensize[1]/10 + (box_height*2))):
			self.showPlayers("mapleleafs")

		if (event.x >= (self.screensize[0]/2)+(box_width*5) and event.x <= (self.screensize[0]/2) + (box_width *6)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*2)) and event.y <= (self.screensize[1]/10 + (box_height*3))):
			self.showPlayers("coyotes")

		if (event.x >= (self.screensize[0]/2)+(box_width*5) and event.x <= (self.screensize[0]/2) + (box_width *6)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*3)) and event.y <= (self.screensize[1]/10 + (box_height*4))):
			self.showPlayers("sharks")

		if (event.x >= (self.screensize[0]/2)+(box_width*5) and event.x <= (self.screensize[0]/2) + (box_width *6)) and \
		(event.y >= (self.screensize[1]/10 + (box_height*4)) and event.y <= (self.screensize[1]/10 + (box_height*5))):
			self.showPlayers("blues")


	def showPlayers(self, team_name):
		os.chdir("pics\\"+team_name+"\\")
		files_in_dir = os.listdir(os.getcwd())
		url = "http://"+team_name+".nhl.com/club/stats.htm" #We need each player on the teams stats
		response = urllib2.urlopen(url)
		f = open('Response.txt', 'w')
		f.write(response.read())
		f.close()
		if self.ran: #If the program was ran before, move previous text off the screen
			self.tnode1.x = -400
			self.tnode2.x = -400
			self.tnode3.x = -400
			self.tnode4.x = -400
			self.tnode5.x = -400
			self.tnode6.x = -400
			self.tnode7.x = -400
			self.tnode8.x = -400
			self.tnode9.x = -400
			self.tnode10.x = -400
			self.tnode11.x = -400
			self.tnode12.x = -400
		with open("Response.txt") as f:
			players_to_go = 12  #Number of players left to display on screen
			player_name = ""
			player_goals = 0
			player_points = 0
			player_assists = 0
			capture_data = 0 #Used for iterating file made to get specific data x lines away. Example: to get data 3
			#lines away we get wait untill our counter is 3.
			for line in f:
				line = line.strip()
				if capture_data == 4:
					player_points = line[line.rindex("\">")+2:line.rindex("</td>")]
					capture_data = 0
					for picture in files_in_dir:
						if picture == player_name+".jpg": #Find our players picture
						
						#The way the data was collected, the best players are received first so
						#our order will always be Center, Right Wing, Left Wing: -> Repeat. This process
						#is done for all four lines. The players stats are added under their picture

							#fourth line
							if  players_to_go < 4 and players_to_go > 0: #Add our player to the page.
								if players_to_go == 3:
									player3 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/4.8, self.screensize[1]/1.5), parent=self.player.getRootNode())
									
									self.tnode3 = avg.WordsNode(pos=(self.screensize[0]/5.5, self.screensize[1]/1.2), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)

								if players_to_go == 2:
									player2 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/2.9, self.screensize[1]/1.5), parent=self.player.getRootNode())
									
									self.tnode2 = avg.WordsNode(pos=(self.screensize[0]/3.2, self.screensize[1]/1.2), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)

								if players_to_go == 1:
									player1 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/13, self.screensize[1]/1.5), parent=self.player.getRootNode())
									
									self.tnode1 = avg.WordsNode(pos=(self.screensize[0]/25, self.screensize[1]/1.2), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)
								players_to_go-=1

							#third line
							if players_to_go < 7 and players_to_go > 3:
								if players_to_go == 6:
									player6 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/4.8, self.screensize[1]/2.2), parent=self.player.getRootNode())
									
									self.tnode6 = avg.WordsNode(pos=(self.screensize[0]/5.5, self.screensize[1]/1.65), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)

								if players_to_go == 5:
									player5 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/2.9, self.screensize[1]/2.2), parent=self.player.getRootNode())
									
									self.tnode5 = avg.WordsNode(pos=(self.screensize[0]/3.2, self.screensize[1]/1.65), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)

								if players_to_go == 4:
									player4 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/13, self.screensize[1]/2.2), parent=self.player.getRootNode())
									
									self.tnode4 = avg.WordsNode(pos=(self.screensize[0]/25, self.screensize[1]/1.65), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)
								players_to_go-=1

							#second line
							if players_to_go < 10 and players_to_go > 6:
								if players_to_go == 9:
									player9 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/4.8, self.screensize[1]/4.4), parent=self.player.getRootNode())

									self.tnode9 = avg.WordsNode(pos=(self.screensize[0]/5.5, self.screensize[1]/2.65), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)

								if players_to_go == 8:
									player8 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/2.9, self.screensize[1]/4.4), parent=self.player.getRootNode())

									self.tnode8 = avg.WordsNode(pos=(self.screensize[0]/3.2, self.screensize[1]/2.65), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)

								if players_to_go == 7:
									player7 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/13, self.screensize[1]/4.4), parent=self.player.getRootNode())
									
									self.tnode7 = avg.WordsNode(pos=(self.screensize[0]/25, self.screensize[1]/2.65), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)
								players_to_go-=1

							#first line
							if players_to_go <= 12 and players_to_go >= 10:
								if players_to_go == 12:
									player12 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/4.8, self.screensize[1]/100), parent=self.player.getRootNode())

									self.tnode12 = avg.WordsNode(pos=(self.screensize[0]/5.5, self.screensize[1]/6), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)
								if players_to_go == 11:
									player11 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/2.9, self.screensize[1]/100), parent=self.player.getRootNode())

									self.tnode11 = avg.WordsNode(pos=(self.screensize[0]/3.2, self.screensize[1]/6), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)

								if players_to_go == 10:
									player10 = ImageNode(href=os.getcwd()+"\\"+picture, size = (self.screensize[1]/8.5, self.screensize[0]/12),
									pos=(self.screensize[0]/13, self.screensize[1]/100), parent=self.player.getRootNode())

									self.tnode10 = avg.WordsNode(pos=(self.screensize[0]/25, self.screensize[1]/6), font="arial", fontsize = (15), color = "000000",
									text=player_name+": "+player_goals+"G "+player_assists+"A "+player_points+"P", parent=self.rootNode)
								players_to_go-=1

				#This part parses for the goal, points, and assists data.
				if capture_data == 3:
					player_assists = line[line.rindex("\">")+2:line.rindex("</td>")]
					capture_data = 4

				if capture_data == 2:
					player_goals = line[line.rindex("\">")+2:line.rindex("</td>")]
					capture_data = 3

				if capture_data == 1:
					capture_data = 2

				if line.find("td class=\"left\"><nobr><a href=\"/club/player.htm?id=") != -1:
					player_name = line[line.rindex("\">")+2:line.rindex("</a>")]
					capture_data = 1
				if players_to_go == 0:
					break

		os.remove("Response.txt")
		os.chdir("../..")
		self.ran = True

	def go(self):
		self.player.play()


def main():
	app = Application()
	app.go()
	

if __name__ == "__main__":
	main()