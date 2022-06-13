from os import system
from os import system
from colorama import Fore
import sys

# all the rooms!
rooms = {
  "start" :  {
    "title" : 'Welcome to the Club! \n Your goal is to survive the night and get home. \n To do this you will have to make crucial choises. \n Good luck adventurer! \n'
    ,
    "description" : "You arrived at the Club.\n In the distance you see a door to the club and a ladder to the roof.",
    "options": ["door", "ladder"],
    "newrooms": ["inside", "ladder"]
  },

  "ladder" :  {
    "title" : "Climbing the ladder...",
    "description" : "You started to climb the ladder but halfway you hear the ladder starting to crack. \n What do you do?",
     "options": ["up", "down"],
     "newrooms": ["death", "start"]
  },
  
  "inside" :  {
    "title" : "In the Club",
    "description" : "your in the club what you wanna do",
     "options": ["dance", "bar"],
        "newrooms": ["room1", "room2"]
  },

  "bar" :  {
    "title" : "At the Bar",
    "description" : "Alright mate, what can i get you",
     "options": ["Baco", "Tequila"],
        "newrooms": ["room1", "room2"]
  },
  
    "death" :  {
    "title" : "Oh no you died...",
    "description" : "You died poopoohead",
    "options" : ["exit" , "retry"],
          "newrooms": ["room1", "start"]
  }
}

#the game "engine"
def game(room):
#  system('clear')
  currentRoom = rooms[room]
  
  title = currentRoom["title"]
  description = currentRoom["description"]  
  options = currentRoom["options"]
  newrooms = currentRoom["newrooms"]

  print(Fore.BLUE,title)
  print(Fore.LIGHTWHITE_EX,description)
  print("Choose one of these options: ")  

  print(", ".join(options))
  
  userinput = input()
  userinput = userinput.lower()
  
  if userinput in options:
   if userinput == ("exit"):
     sys.exit()
   else :
    index = options.index(userinput)
    #index uilezen en opzoeken in newlist
    #print(index)  
    #print(newrooms[index])
    game(newrooms[index])
  else:
    print('Thats not an option... Try again genius!')

    game(room)
  
game("start")