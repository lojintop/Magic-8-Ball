def get_user_guess():
    while True:
        try:
            guess=int(input("enter your guess(1-100):"))
            if 1<=guess<=100:
                return guess 
            else:
                print("please enter a number between 1and 100.")
        except ValueError:
            print("invalid input")
            
import random
responses=["yes,definitely","NO,not now.","ASK agine later.","it is certain.","very doubtful","outlook is good","Beter not tell you now","concenttarate and ask agin."]
def get_random_respones():
 return random.choice(responses)
