import random
import re
import requests

meaningpedia_resp = requests.get("https://meaningpedia.com/5-letter-words?show=all")
pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
words = pattern.findall(meaningpedia_resp.text)
print("Welcome to the Hangman game.")

computer_choice = random.choice(words)
current = ["_", "_", "_", "_", "_"]
failed_attemps = 0
attempted_letters = []

def check_guess(u_input, c, f_attemps, a_letters):
	if u_input in computer_choice:
		place = computer_choice.find(u_input)
		c[place] = u_input
		print(current)
	else:
		f_attemps += 1
		a_letters.append(u_input)
		print("Not in the word.")
		print("Attemps left: " + str(10 - f_attemps))
		print("Attemped letters: " + str(a_letters))
	return c, f_attemps, a_letters

while failed_attemps < 10:

	user_input = input("Enter a letter: ")

	if len(user_input) > 1:
		print("Please only enter one letter.")
	else:
		current, failed_attemps, attempted_letters = check_guess(user_input, current, failed_attemps, attempted_letters)

		if current == list(computer_choice):
			print("You won! The word was " + computer_choice.upper())
			break