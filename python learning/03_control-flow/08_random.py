#Random Number Guess(Easy)
import random
number = random.randint(1, 10)
guess = int(input("Enter number: "))
if guess == number:
    print("Correct")
else:
    print("Wrong, the number was {number}")

print(" ")

#Coin Toss Simulator
import random

user_choice = input("Heads or Tails? ").lower()
toss = random.choice(["heads", "tails"])

if user_choice == toss:
    print("You guessed right!")
else:
    print(f"Wrong! It was {toss}")


print(" ")

#Rock, Paper, Scissors
import random

choices = ["rock", "paper", "scissors"]
user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print(f"Computer chose: {computer}")

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("You win!")
else:
    print("You lose!")

print(" ")

#Dice Roll - Even or Odd Game
import random

guess = input("Guess 'even' or 'odd': ").lower()
roll = random.randint(1, 6)

print(f"You rolled: {roll}")
if (roll % 2 == 0 and guess == "even") or (roll % 2 != 0 and guess == "odd"):
    print("Correct!")
else:
    print("Wrong!")


print(" ")

#Random Compliment Generator
import random

compliments = ["You're awesome!", "You're smart!", "You're kind!", "You're creative!"]
print(random.choice(compliments))

print(" ")

#Lucky Draw Game
import random

number = random.randint(1, 100)
print(f"Your lucky number is: {number}")

if number == 7:
    print("Jackpot!")
elif number % 5 == 0:
    print("Small prize!")
else:
    print("Try again!")

print(" ")

#Random Password Strength Checker
import random

length = random.randint(5, 15)
print(f"Generated password length: {length}")

if length < 8:
    print("Weak password")
elif length <= 12:
    print("Moderate password")
else:
    print("Strong password")

print(" ")

#Magic 8-Ball Simulator
import random

input("Ask me any question: ")
responses = ["Yes", "No", "Maybe", "Ask again later"]
print(random.choice(responses))

print(" ")

#Roll Two Dice
import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

print(f"You rolled: {die1} and {die2} (Total: {total})")

if total in [7, 11]:
    print("You win!")
elif total in [2, 3, 12]:
    print("You lose!")
else:
    print("Roll again!")

print(" ")

#Random Mood Generator
import random

mood = random.choice(["happy", "sad", "excited", "tired"])
print(f"Today you're feeling: {mood}")

if mood == "happy":
    print("Keep smiling 😄")
elif mood == "sad":
    print("It's okay to feel down. Better days are coming 💙")
elif mood == "excited":
    print("Awesome! Make the most of it 🚀")
else:
    print("Take some rest and recharge 💤")
