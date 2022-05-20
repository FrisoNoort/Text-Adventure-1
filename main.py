# all the rooms!
rooms = {
  "outside" :  {
    "title" : "outside the club",
    "description" : "wanna go inside?",
    "options": ["In the Club", "no"],
  },

  "club" :  {
    "title" : "In the Club",
    "description" : "your in the club what you wanne do",
     "options": ["dance", "Bar"]
  },

  "bar" :  {
    "title" : "At the Bar",
    "description" : "aight mate, what can i get you",
     "options": ["Baco", "Tequila"]
  },

  "no" :  {
    "title" : "no no no",
    "description" : "You died poopoohead",
    "options" : ["outside the club" , "bar"]
  }
}

#the game "engine"
def game(room):
  currentRoom = rooms[room]
  
  if room == 'outside the club':
    print('Welcome to the Club')

  # get this room's title and description
  title = currentRoom["title"]
  description = currentRoom["description"]  
  options = currentRoom["options"]

  # show to user
  print(f"{title}")
  print(description)
  print("type the name of the room you would like to go next: ")  

  print(", ".join(options))
  nextRoom = input()

  

  #TODO: check and sanitize input
  
  # go to next room
  game(nextRoom)

#start the game from the sleepingroom
game("outside the club")