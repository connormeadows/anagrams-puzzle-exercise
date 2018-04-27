#Anagrams game
from random import choice, sample

class Anagram:
    def __init__(self, difficulty):
        e = ['Corn','Dog','Cat','Mouse','Home','Room','Palace','Flop','Sit','Allow','Amaze','Shop','School','Back','Goodbye','Heart','Break','Time','Ugly','Wait','Only','Small','Snail','Ram','Sense','Come']
        m = ['Runner','Laughter','Ponder','Voluminous','Fantastic','Extreme','Quickly','Absurd','Wordy','Supreme','Elephant','Agony','Elaborate','Consequence','Decadent','Awesome','Relevant','Omen']
        h = ['Cogitate','Inconspicuous','Convoluted','Extraneous','Remarkable','Paleontologist','Prognosticate','Fabricate','Serendipitous','Magnificent','Stupendous','Incomprehensible','Enmeshed','Mesmerizing','Sumptuous','Bonafide','Bantam','Phantasm','Penultimate']
        if difficulty == 'e':
            self.word = choice(e)
        elif difficulty == 'm':
            self.word = choice(m)
        elif difficulty == 'h':
            self.word = choice(h)
        self.mixer()
        self.run()

    def mixer(self):
        self.mixList = list(self.word)
        self.ezMixString = ' '.join(sample(self.mixList, len(self.mixList)))
        self.mixString = self.ezMixString.lower()

    def hints(self, h):
        if h == 'capital':
            print("  The first letter is now capitalized\n  " + self.ezMixString)
        elif h == 'give up':
            print("  The word is " + self.word)

    def run(self):
        print("\n  Your anagram is\n  " + self.mixString)
        quest = True
        while quest:
            ans = input("  ").lower()
            if ans == 'cap':
                self.hints('capital')
            elif ans == 'give up':
                self.hints(ans)
                break
            elif ans != self.word.lower():
                print("  Sorry, wrong word. Try again\n")
            else:
                print("  That's right! The word is " + self.word)
                quest = False


print("\n  Time for an anagram! There are three difficulties: easy, medium, and hard.")
print("  There are hints! Type \"cap\" to capitalize the letter that starts the word.")
print("  If you are ready to give up, type \"give up\".")
yn = "y"
while yn != "n":
    ans = input("\n  Type \"e\" for easy, \"m\" for medium, and \"h\" for hard.")
    while ans != 'e' and ans != 'm' and ans != 'h':
        ans = input("  That is not a valid choice. Please put \"e\",\"m\", or \"h\".")
    abc = Anagram(ans)
    yn = input("\n  Play again? Type \"y\" if yes or \"n\" if you're done.")
