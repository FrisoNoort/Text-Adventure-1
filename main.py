# all the rooms!
rooms = {
  "sleepingRoom" :  {
    "title" : "Sleepingroom",
    "description" : "There's a bed in the room. This must be a room for sleeping",
    "options": ["kitchen", "slaapkamer"],
  },

  "kitchen" :  {
    "title" : "Kitchen",
    "description" : "Hmmm... what's for dinner?",
     "options": ["a", "b"]
  },

  "forrest" :  {
    "title" : "Forrest",
    "description" : "There's a bunch of trees. I am Groot! Says a tree",
     "options": ["aap", "noot"]
  },

  "slaapkamer" :  {
    "title" : "Slaapkamer",
    "description" : "Zzzzzz"
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
game("sleepingRoom")