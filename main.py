# all the rooms!
rooms = {
  "outside the club" :  {
    "title" : "outside the club",
    "description" : "wanne go inside",
    "options": ["In the Club", "no"],
  },

  "In the Club" :  {
    "title" : "In the Club",
    "description" : "your in the club what you wanne do",
     "options": ["dance", "Bar"]
  },

  "Bar" :  {
    "title" : "bar",
    "description" : "aight mate, what can i get you",
     "options": ["Baco", "Tequila"]
  },

  "no" :  {
    "title" : "no",
    "description" : "You died poopoohead"
  }
}

#the game "engine"
def game(room):
  currentRoom = rooms[room]

  # get this room's title and description
  title = currentRoom["title"]
  description = currentRoom["description"]  
  options = currentRoom["options"]

  # show to user
  print(f"You're in the {title}")
  print(description)
  print("type the name of the room you would like to go next: ")  

  print(", ".join(options))
  nextRoom = input()

  #TODO: check and sanitize input
  
  # go to next room
  game(nextRoom)

#start the game from the sleepingroom
game("outside the club")