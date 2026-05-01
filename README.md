Word Guess (Wordle Clone): A game where you have 6 guesses to guess a 5-letter word. For each guess, every letter will be analyzed. For each letter, if the letter is not in the answer word at all, then it will appear grey on the guess. If the letter in the guess is in the answer word but not in the corresponding position from guess to answer, it will appear yellow on the guess. If the letter in the guess is in the answer word and in the corresponding position from guess to answer, then it will appear green on the guess. Every letter has to be green in the guess to win. My project will include many classes, like a Board class to store guesses and determine guess correctness, a Tile class to represent individual letters and display the color of the letters.
Python, Pygame, Random, Mixer, Font, Os


Features:

Game Scene: 
Blank Grid
User-controlled Guesses
Letter Checking+Colored In Letters 
Sound Effects
	Win Scene:
Guess Count
Sound Effect
Big Headline
	Lose Scene:
Word Reveal
Sad Sound Effect
P for priority
Game Scene (P1): 
5x6 Grid (P2)
User-controlled Guesses (P1)
Letter Checking+Colored In Letters (P1)
Sound Effects (P3)
	Win Scene (P2):
Guess Count: (P2)
Sound Effect (P3)
Big Headline (P2)
	Lose Scene (P2):
Word Reveal (P2)
Sad Sound Effect (P3)
