import mpo
import random
print("\nTERMINAL")
guessing_list = ["good","bad","hallo","elephant","galaxy","butterfly"]
print("""\n
*************** GAME THEME *******************
    The game's premise is that the device 
    guesses one of these words, and you 
      have to figure out what it is using
       the letters and spaces the device 
                provides.
**********************************************
""")
print(f"   {"  |  ".join(guessing_list)}\n")
newo_list = []
mm = []
guessing = random.choice(guessing_list)
for x in guessing:
    newo_list.append("_")
print(" ".join(newo_list))
print(mpo.A[6])
number = 6
while "".join(newo_list) != guessing and number >0:
    guess = input("Please guess a letter: ")
    for v in range(len(guessing)):
        if guess == guessing[v]:
            newo_list[v] = guess
        if guess not in guessing:
            if guess not in mm:
                number -= 1
                mm.append(guess)
                print(mpo.A[number])
                print(" ".join(newo_list))
            else:
                print("You already guessad that. Try again")
            break
    if guess in newo_list:
        print(" ".join(newo_list))
    print(f"You have {number} more tries")
if number == 0:
    print("\n          You lose!       ")
    print("""

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

""")
else:
    print("""
********************
      YOU WIN!
********************
""")
input("")