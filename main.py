from os import system

# all the rooms!
rooms = {
  "start" :  {
    "title" : 'Welcome to the Club! \nYour goal is to survive the night and get home. \nTo do this you will have to make crucial choises. \nGood luck adventurer! \n'
    ,
    "description" : "wanna go inside?",
    "options": ["club", "no"],
  },

  "club" :  {
    "title" : "In the Club",
    "description" : "your in the club what you wanne do",
     "options": ["dance", "bar"]
  },

  "bar" :  {
    "title" : "At the Bar",
    "description" : "Alright mate, what can i get you",
     "options": ["Baco", "Tequila"]
  },

  "no" :  {
    "title" : "no no no",
    "description" : "You died poopoohead",
    "options" : ["start"]
  },
    
  "dance" : {
    "title": "On the dance floor",
    "description" : "You spot a girl dancing alone",
    "options" : ["dance with her", "dance alone", "bar"]
  },

}

#the game "engine"
def game(room):
  system('clear')
  currentRoom = rooms[room]

  # get this room's title and description
  title = currentRoom["title"]
  description = currentRoom["description"]  
  options = currentRoom["options"]

  # show to user
  print(f"{title}")
  print(description)
  print("Choose one of these options: ")  

  print(", ".join(options))
  
  nextRoom = input()
  nextRoom= nextRoom.lower()
  
  if nextRoom in options:
    game(nextRoom)
  else:
    print('Thats not an option... Try again genius!')
    
    game(room)
  
#start the game from the sleepingroom
game("start")