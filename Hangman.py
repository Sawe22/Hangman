"""unique element is on line 86-89. If the user feels confident enough to 'shout out' the entire word, they
may do so to attempt to get it right all in one go"""

import random #allows program to choose random elements from lists

import string
 #Get all english letters


import time#Imports a things which allows for commands which makes the program freeze for x amount of seconds



#Grabs lists which were made from the wordlist.py file
from wordlist import list_Of_Words
from wordlist import HANGMAN_PICS 
from wordlist import list_of_congrats
from wordlist import list_of_rejects




wins = 0

losses = 0


#A function which chooses a random word from the word list and returns that word provided it isnt rai or zimmerman
def is_Acceptable(chosen_Word):
    word = random.choice(list_Of_Words) #Gets a random word from the list of words, random comes from import random
    while word == "Rai" or word == "Zimmerman": #Keeps selecting a random word until it isn't rai or zimmerman
         word = random.choice(list_Of_Words)

    return word.upper() #Returns the word in all caps

def hangman_Game():

    #Get two global variables into the function to be modified, while they remain global variables
    global wins 
    global losses 


    guess = is_Acceptable(list_Of_Words) #Assigns this variable to an acceptable random word
    word_letters = set(guess) #makes the random word into a set
    alphabet = set (string.ascii_uppercase) #Alphabet is a set of uppercase letters, comes from import string
    guessed_letters = set() #Making an empty set, where already guessed word will go into


    mistakes = 6 #counter for mistakes
    attempts = 0 #Counter for number of attempts


    while len(word_letters) >= 0 and attempts != 7: #If this variable is not yet zero, of they have mistakes left, it means the game is not complete, meaning it should loop on until it is finished. Takes the length of the letters remaining to compare them to zero

     #The below prints the full secret word out if the user guessed it correctly, known if there are no letters left in the word_letters set
        if len(word_letters) == 0:
            list_of_current_word = [letter if letter in guessed_letters else '_' for letter in guess]
            print("Congrats, you guessed the word: ", ' '.join(list_of_current_word))
            wins +=1
            break

        hangman = HANGMAN_PICS[attempts] #Prints the hangman image out at the attempted index

        print(hangman) #prints a string which is at the attempt index in the hangman image


        print(f"You have {mistakes} mistakes left") #Tells the user the amount of guesses they have remaining



        print ("You have used these letters: ", ' '.join(guessed_letters)) #Turns this list into a string, which is seperated by whatever is before .join

        list_of_current_word = [letter if letter in guessed_letters else '_' for letter in guess] #This is a for loop which creates a list. It plays out once for each letter in the length of
        #the secret word. From left to right, if a character in the secret word is seen to be in the set of guessed letters, it is added to the list at that 
        #index, otherwise a dash is added at that index
        print("Current word: ", ' '.join(list_of_current_word)) #Adds elements from the list_of_current_word after this string. joined by a space
        




        user_Guess = input ('Give a guess: ').upper() #Prompts user to choose a letter, which is made into uppercase

        time.sleep(1) # Makes the user wait for 2 seconds

        if user_Guess == guess: #if the user can guess the rest of the word, they automatically win.
            print("Congrats, you guessed the word: ", ' '.join(guess))
            wins += 1
            break
        
        if user_Guess in alphabet - guessed_letters: #Sees if the current user guess is in the set of alphabet letters not including the already guessed letters
            guessed_letters.add(user_Guess) #Adds the guessed letters to the guessed letters set


            if user_Guess in word_letters: #If the letter guessed is in the current letters remaining, remove that letter from the list of letters remaining
                word_letters.remove(user_Guess)
                print(random.choice(list_of_congrats))
            else:
                attempts += 1 #Attempts go up
                mistakes -= 1 #mistakes go down
                print("Letter not in word")
                print(random.choice(list_of_rejects)) 


        elif user_Guess in guessed_letters: #If the guessed letter is something which was previously guessed, the user is told so 
            print ("This is an old guess, try something new")


        else:
            attempts +=1
            print("invalid input. Please enter a letter! (Or guess the whole word if you can!)") #If the letter wasn't already guessed or isnt in the alphabet set, it means it is invalid
    if attempts == 7: 
        print ("you ran out of chances, please play again. The word was:", guess)
        losses += 1


option = ""
    
while option.upper() != "N": #Plays the game until user doesn't want to play anymore

    try:
        option = str(input("Would you like to play hangman?(Y/N):"))
    except:
        print("Invalid Input") #if the user doesnt input a string the input is invalid


    if option.upper() == "Y":
        hangman_Game()
    elif option.upper() != "N":
        print("invalid input")
    

print (f"You won {wins} times and you lost {losses} times")
