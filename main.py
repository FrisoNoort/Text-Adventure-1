from os import system
from colorama import Fore
import sys

# all the rooms!
rooms = {
  "start" :  {
    "title" : 'Welcome to the Club! \n Your goal is to survive the night and get home. \n To do this you will have to make crucial choises. \n Good luck adventurer! \n'
    ,
    "description" : "You arrived at the Club.\n In the distance you see the front door to the club and a ladder to the roof.",
    "options": ["door", "ladder"],
    "newrooms": ["inside", "ladder"]
  },

  "ladder" :  {
  "title" : "Climbing the ladder...",
  "description" : "You started to climb the ladder but halfway you hear the ladder starting to crack. \n What do you do?",
  "options": ["up", "down"],
  "newrooms": ["roof", "start"]
  },
 
  "roof" :  {
  "title" : "On the roof!",
  "description" : "You barely made it to the roof, you are so frightened you are debating to go back with the ladder but you also see a cabin up ahead ",
  "options": ["cabin", "go back"],
  "newrooms": ["cabin", "start"]
  },

  "cabin" :  {
  "title" : "In the roofcabin",
  "description" : "You secretly entered the roofcabin and see a note... \n do you read it or go back to the roof?",
  "options": ["read note" , "roof"],
  "newrooms": ["note","roof"]
  },
  
  "note" :  {
  "title" : "The note sais: 'code : 42069'",
  "description" : "",
  "options": ["okay",],
  "newrooms": ["cabin"]
  },
  
  "inside" :  {
  "title" : "In the Club",
  "description" : "You entered the club and can choose to do two things:\n go to the dancefloor or go to the bar",
  "options": ["dance", "bar"],
  "newrooms": ["dance", "bar"]
  },

  "dance" :  {
    "title" : 'dance floor' ,
    "description" : 'The music is blasting in your ears. \n Everybody around you is dancing and having fun. \n You see this girl dancing alone. \n Do you go up to her? \n' ,
    "options": ['yes', 'no', 'bar' ],
       "newrooms": ['girl','death2','bar' ]
  },

  "bar" :  {
    "title" : 'At the bar' ,
    "description" : 'you take a seat at the bar and the bartender greets you: "aight mate, what can i get you? \n' ,
     "options": ['vodka', 'tequila', 'the girl'],
        "newrooms": ['shot', 'shot']
  },

  "shot" :  {
    "title" : "Your'e shot is ready" ,
    "description" : "You took the shot like a man, wanne take another" ,
     "options": ['another', 'no' ],
        "newrooms": ['shot','bar' ]
  },

  
  "girl" :  {
    "title" : "You walk up to her and start dancing",
    "description" : "You think she's beautiful so you use your best pickup-line. Better choose wisely... \n 1:Are you wifi cause i am totaly feeling a conection. \n 2: Treat me like a pirate and give me your booty \n 3: I may not go down in history, but i will go down on you. \n 4:Aside from being sexy what do you do for a living ",
     "options": ['1','2','3','4' ],
        "newrooms": ["","","",""]
  },
  
  "death1" :  {
  "title" : "Oh no you died...",
  "description" : "You died poopoohead",
  "options" : ["exit" , "retry"],
  "newrooms": ["", "start"]
  },
  
  "death2" :  {
  "title" : "No Bitches?",
  "description" : "Unfortunately you failed to get bitches...\n i guess you really are a disappointment,\n would you like to try again? ",
  "options" : ["exit" , "retry"],
  "newrooms": ["", "start"]
  }
}

#the game "engine"
def game(room):
  system('clear')
  currentRoom = rooms[room]
  
  title = currentRoom["title"]
  description = currentRoom["description"]  
  options = currentRoom["options"]
  newrooms = currentRoom["newrooms"]

  print(Fore.BLUE,title)
  print(Fore.LIGHTWHITE_EX,description)
  print(" Choose one of these options: ")  

  print("", ", ".join(options))
  
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