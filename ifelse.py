#!/usr/bin/env python3

choice =input("Rock, Paper, Scissors: ")

if choice == "rock":
    print("I win")
    print("good game")
elif choice == "paper":
    print("Paper beats rock")
    print("good game")
elif choice == "scissors":
    print("Rock beats scissors")
    print("good game")
else: 
    print("Please select rock, paper, ot scissors")
