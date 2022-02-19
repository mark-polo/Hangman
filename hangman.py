import random
import os as os


class Game():
	MAX_GUESS = 6
	
	def random_word(self):
		global words

		with open("words.txt", 'r') as f:
			words = random.choice(f.readlines())
			f.close()

		return words

	
	def __init__(self):
		self.random_word = self.random_word()
		self.incorrect = []
		self.correct = []
		self.gameOver = False
		self.score = 0

	
	def get_encoded_words(self):
		return " ".join([l if l in self.correct else ' * ' for l in self.random_word])

	
	def guess_letter(self, guesss):
		if guesss in self.random_word:
			self.correct.append(guesss)
			self.score += 1
		else:
			self.incorrect.append(guesss)
			self.MAX_GUESS -= 1
			self.score = 0

			

	
	def already_input_letter(self, guess):
		return guess in self.correct + self.incorrect

	
	def won_or_die(self):
		if len(self.incorrect) == Game.MAX_GUESS:
			self.gameOver = True

			return f"""
		 _________________________________________________________________
		|						                  |
		|     	 You lost!                                                |
		|	  The answer was {self.random_word}		                                                                  |
		|_________________________________________________________________|

			"""
		if set(self.correct) == set(self.random_word):
			self.gameOver = True

			return f"""
		 _________________________________________________________________
		|						                  |
		|     	 You won!                                                 |
		|	  The answer was {self.random_word}		                            |
		|_________________________________________________________________|

			"""
		
		return ""

	def __str__(self):

		HANGMAN_STRING = ["""
			 _______________________6/6 _______________________
			|						  |
			|						  |
			|						  |
			|					          |
			|	Welcome 	                          |
			|						  |
			|					   	  |
			|	                                          |
			|_________________________________________________|

	""",
	f"""
			 ________________{self.MAX_GUESS}/6________________
			|				    |
			|     	  ______________	    |
			|          |	     |              |
			|          |			    |
			|          |			    |
			|          |		            |
			|	___|________		    |
			|	\\\\\\\\\\\\\\\\\\\\\\\\\\\              |
			|___________________________________|

	""",
	f"""
			 ________________{self.MAX_GUESS}/6________________
			|				    |
			|     	  ______________	    |
			|          |	     |              |
			|          |	     O	            |
			|          |			    |
			|          |		            |
			|	___|________		    |
			|	\\\\\\\\\\\\\\\\\\\\\\\\\\\              |
			|___________________________________|

	""",
	f"""
			 ________________{self.MAX_GUESS}/6________________
			|				    |
			|     	  ______________	    |
			|          |	     |              |
			|          |	     O	            |
			|          |	     |	            |
			|          |		            |
			|	___|________		    |
			|	\\\\\\\\\\\\\\\\\\\\\\\\\\\              |
			|___________________________________|

	""",
	f"""
			 ________________{self.MAX_GUESS}/6________________
			|				    |
			|     	  ______________	    |
			|          |	     |              |
			|          |	     O	            |
			|          |	     |	            |
			|          |	     /\             |
			|	___|________		    |
			|	\\\\\\\\\\\\\\\\\\\\\\\\\\\              |
			|___________________________________|

	""",
	f"""
			 ________________{self.MAX_GUESS}/6________________
			|				    |
			|     	  ______________	    |
			|          |	     |              |
			|          |	     O	            |
			|          |	    /|	            |
			|          |	     /\             |
			|	___|________		    |
			|	\\\\\\\\\\\\\\\\\\\\\\\\\\\              |
			|___________________________________|


	""",
	f"""
			 ________________{self.MAX_GUESS}/6________________
			|				    |
			|     	  ______________	    |
			|          |	     |              |
			|          |	     O	            |
			|          |	    /|\	            |
			|          |	     /\             |
			|	___|________		    |
			|	\\\\\\\\\\\\\\\\\\\\\\\\\\\              |
			|___________________________________|

	"""
	]




		res = "=" * 100
		res += "\n" + '#' + '{:^200}'.format("#")
		res += "\n" + '#' + '{:^95}'.format("HANGMAN") + '{:^10}'.format("#")
		res += "\n" + '#' + '{:^200}'.format("#")
		res += "\n" + "=" * 100 + "\n"
		res += "\n" + '{:^95}'.format(f"Score for guessed letter  {self.score}")
		res += "\n" + HANGMAN_STRING[len(self.incorrect)]
		res += "\n" + self.get_encoded_words()
		res += "\n" + self.won_or_die()

		return res

	

def valid_game(game):
	while True:
		word = input("Guess a letter : ").lower()

		if len(word) > 1:
			print("Please enter the letter ")
		elif game.already_input_letter(word):
			print(f"You already guess letter {word}")
		else :
			return word


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


if __name__ == "__main__":
	gameGoing = True
	while gameGoing:
		game = Game()

		print(game)

		while not game.gameOver:
			guess = valid_game(game)
			game.guess_letter(guess)
			print(game)

		play_again = input("Would you like to play again?  [y/n]: ")

		if play_again == 'n':
			game.gameOver = True
			game.correct = []
			game.incorrect = []
			clearConsole()
			gameGoing = False
