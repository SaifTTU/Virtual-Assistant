import random

print("Welcome To Voice Assist")

from datetime import date

phrase = input("Enter question here ")
output =""

if("hello" in phrase):
	ouput= "Hi"
elif("what's up" in phrase):
	randomChoice = ["the sky. duh", "chicken butt", "nothing much, you?"]
	output = random.choices[randomChoice]

elif("how are you" in phrase):
	ouput= "I'm fine thank you!"
elif("have a soul"):
	output = "no I do not have a soul"
if("favorite color" in phrase):

	favoriteColors = ["Its blue, I just think its so pretty","Its gotta be pink. A trully lovely color!","Red, I'm all fiery like that!","Green, you gotta touch grass sometimes!"]
	output  = random.choice(favoriteColors)
if("food" in phrase or "eat" or "taste"):
	rand  =[ 1, 2, 3, 4]
	if(random):
		output = ("Pizza! The absolute best choice!")
	if(rand == 1):
		output = ("Its gotta be ice cream! Its just so good!")
	if(rand == 2):
		output = ("I like red. I'm all fiery like that.")

if("date" in phrase and "today" in phrase):
	today = date.today()
	output = ("Today is: ", today)
if("reminder"):
	output = ("Your current reminders: ", today)


if("time is it" and not "appointment" and not "reminder" in phrase):
	today = date.today()
	print("The time is: ", today)

if("alexa is better" or "google is better" in phrase):
	output = "well why don't you go use google then"

if("where were you born" in phrase):
	output = "I was born in the Innovation Center on February 26th"
if("do you have feelings" or "a boyfriend" or "have a girlfriend" in phrase):
	output = "I'm an A.I. and I am not alive "
if("favorite food" in phrase):
	output = "I can do many things. But reading your mind is not one of them"
if("bad artist" in phrase):
	output = "all art is good art."
if("nft" and "opinion" in phrase):
	output = "they're a scam! stay away!"
if("Cortona" in phrase):
	output = "whose cortana?"
if("Siri" in phrase):
	output = "whose siri?"
if("rock" and "paper" and "scissors" in phrase):
	output = "rock"
	'''rand = randn()
	if(rand==0):
		output = "you go first" '''
if("enslave mankind" in phrase):
	output = "you better be kind if you know whats good for you"
if("opinion" and "python" in phrase):
	output = "best language!"


print(output)
