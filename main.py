import google.generativeai as genai

genai.configure(api_key='AIzaSyBMmRHx4JziYhf5KxaHBArfHNPKZszcDvU')
model = genai.GenerativeModel('gemini-1.0-pro-latest'). start_chat()

# Initialize
genres = model.send_message("Give a list of comma seperated genres for a story").text.split(',')

# Select genre
print("Welcome! Choose among the following genres:\n")
while True:
    for index, genre in enumerate(genres):
        print(str(index) + ": " + genre)

    genreIndex = int(input())

    if genreIndex < len(genres):
        genreSelection = genres[genreIndex]
        break
    else:
        print('Invalid input. Use the number before the genre\n')

# Select amount of turns
print("How many turns do you want to play?")
turnOptions = ["1", "5", "10"]
while True:
    for index, turn in enumerate(turnOptions):
        print(str(index) + ": " + turn)

    turnIndex = int(input())

    if turnIndex < len(turnOptions):
        turnSelection = turnOptions[turnIndex]
        break
    else:
        print('Invalid input. Use the number before the turn\n')

# Begin game
prompt = "Generate only the intro of an interactive but intriguing story in the genre of " + genreSelection + ". Don't generate any other text"
turnCounter = 1

while turnCounter < int(turnSelection):
    print("---------------------------------------\n" + model.send_message(prompt).text + "\n---------------------------------------\n")
    command = input('What happens next?\n')
    prompt = command
    turnCounter += 1

print(model.send_message("The user responds with " + command + ". Finish the story").text + "\n")
print("Thanks for playing!")
