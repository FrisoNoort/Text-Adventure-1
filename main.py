# all the rooms!
rooms = {
  "outside" :  {
    "title" : "outside the club",
    "description" : "wanna go inside?",
    "options": ["Club", "no"],
  },

  "club" :  {
    "title" : "In the Club",
    "description" : "your in the club what you wanne do",
     "options": ["dance", "Bar"]
  },

  "bar" :  {
    "title" : "At the Bar",
    "description" : "Alright mate, what can i get you",
     "options": ["Baco", "Tequila"]
  },

  "no" :  {
    "title" : "no no no",
    "description" : "You died poopoohead",
    "options" : ["" , "bar"]
  }
}

#the game "engine"
def game(room):
  currentRoom = rooms[room]
  
  if room == 'outside':
    print('Welcome to the Club!')
    print('Your goal is to survive the night and get home.')
    print('To do this you will have to make crucial choises.')
    print('Good luck adventurer!')
    print("")

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
  nextRoom= nextRoom.lower()

  if nextRoom in options:
    game(nextRoom)
  else:
    print('Thats not an option... Try again genius!')
    game(room)
  
#start the game from the sleepingroom
game("outside")