#PROJECT 2 - THE PERFECT GUESS
'''
We are going to write a program that generates a random number and asks the user to
guess it.

If the player's guess is higher than the actual number, the program displays "Lower
number please". Similarly, if the user's guess is too low, the program prints "higher
number please" When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.

Hint: Use the random module.
'''

import random
import pyttsx3 #text to speech module
import random #random module

#defining function for pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

n = random.randint(1,100)

a = 0
guesses = 0

speak("Guess the Number")
while(a != n):
    a = int(input("Guess the Number: "))

    guesses += 1 
    if(a>n):
        print("Lower Number Please")
        speak("Lower Number Please")

        #guesses += 1#to count the wrong guesses
    elif(a<n):
        print("Higher Number Please")
        speak("Higher Number Please")

        #guesses += 1#to count the wrong guesses

print(f"You have guessed the number {n} correctly in {guesses} attempts")
speak(f"You have guessed the number {n} correctly in {guesses} attempts")



# either keep guesses = 1 and after every wrong guess guesses+=1
# or keep guesses = 0 and after every input add guesses +=1