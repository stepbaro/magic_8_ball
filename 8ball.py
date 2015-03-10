#Magic 8 Ball - predict the future!
import random
import time
import os

repeat = 'yes'

def game():
	os.system('cls') #clears screen
	print "Welcome to the Magic 8 Ball!"
	print "\nAsk me your question and I will predict the future"
	c = raw_input("What is your question? ")
	print "\n\nso you want to know \"%s\"?" % c
	print "\n\nMagic 8 Ball is thinking..."
	time.sleep(1)
	print '.'
	time.sleep(1)
	print '.'
	time.sleep(1)
	print '.'
	time.sleep(1)
	print '.'
	time.sleep(1)
	print '.'
	random_answer()

def random_answer():
	responses = ('It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',\
	'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',\
	'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful')
	rand_response = responses[random.randrange(len(responses))]
	print "Magic 8 Ball\'s response is...\n\n%s" % rand_response
	time.sleep(2)

while repeat == 'yes':
    game()
    repeat = raw_input('\n\nDo you want to play again yes or no? ')
else:
    print('Magic 8 Ball says goodbye')
	


