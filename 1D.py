import time, random

# create class
class Pokemon:
    def __init__(self, name, types, move, tries, health="====="):
        self.name = name
        self.types = types
        self.move = move
        self.health = health
        self.tries = 5  # Amount of tries
        pass


def start_game():
    print("---Gotta Solve Em' All---")
    player_name = input("What is your name? ")
    print(
        f"""
        Welcome player {player_name}!
        Choose your starter Pokemon!
        [1] Pythagoras
        [2] Franklin
        [3] Euler
        """
    )
    starter_pokemon = ["Pythagoras", "Franklin", "Euler"]
    while True:
        try:
            choose_pokemon = int(input("Your starter pokemon is: "))
            if choose_pokemon == 1 or choose_pokemon == 2 or choose_pokemon == 3:
                chosen_pokemon = starter_pokemon[choose_pokemon - 1]
                print(f"Hooray. {chosen_pokemon} is now your Pokemon!")
                break
            else:
                print("Choose amongst the 3 pokemons provided")
        except:
            continue
    time.sleep(1)
    print("------------------------------------------")
    print(  # https://www.asciiart.eu/people/faces
        r"""
    #############       
    ##         ##      
    #  ~~   ~~  #    
    #  ()   ()  #      
    (     ^     )       
     |         |        
     |  {===}  |      
      \       /       
     /  -----  \      
  ---  |%\ /%|  ---     
 /     |%%%%%|     \    
       |%/ \%|                                    
        """
    )
    print(
        """
            Prof : Welcome to Mathematica Island! 
            I am professor Chewbaka, a researcher on this island.
            There are 2 Pokemons on the loose:
            Addition and Subtraction.
            Will you help me catch them?
            """
    )
    time.sleep(1)
    N = 0
    while True:
        try:
            choice = input("Help the Professor?(Y/N): ")
            if choice == "Y" or choice == "N":
                if choice == "Y":
                    print("Prof: Thank you so much!")
                    break
                elif choice == "N":
                    N += 1
                    if N == 1:
                        print("Come on... Don't you want to help me? :(")
                    elif N == 2:
                        print("I'll give you bonus marks for M&A assessment later...")
                    elif N == 3:
                        print("Sigh...No adventures for you then...")
                        break
            else:
                print("I don't understand your input")
        except:
            continue
    print(
        """
        Pokemons on the loose:
        [1]: Addition
        [2]: Subtraction
        """
    )
    pokemon_fights = ["Addition", "Subtraction"]
    while True:
        try:
            catch = int(input("Which pokemon do you want to catch first? "))
            if catch == 1 or catch == 2:
                pokemon_fight = pokemon_fights[catch - 1]
                print(f"you have choosen {pokemon_fight}")
                break
            else:
                print("I don't understand the input")
        except:
            continue


P = Pokemon("no name", "no type", "no moves", 5)
start_game()
# print(P.name)


def random_generator():
    first_number = random.randint(0, 1000)
    second_number = random.randint(0, 1000)
    return first_number, second_number


# Eugene's stuff
def checkdead():
    if P.tries == 0:
        print("Your pokemon has fainted... ")
        print("Game Over")
        P.start_game()
    else:
        print("You are alive")


#
# def victory():
#     print("Congratulations")
#     # gainexp()
# gainmoney()


# Get 2 numbers to add or subtract
numbers = random_generator()
subtraction_ans = abs(numbers[0] - numbers[1])
addition_ans = numbers[0] + numbers[1]


print("Now you have to solve this")

# Loops of subtraction
loop = 1
while loop == 1:
    option = input(
        """Would you like to solve addition or subtraction problems?
    Type 1 for addition, 2 for subtraction"""
    )

    if option == "1":
        correct_ans = addition_ans
        ans = input(f"Solve sum of {numbers[0]} and {numbers[1]}!")
        loop = 0
    elif option == "2":
        correct_ans = subtraction_ans
        ans = input(f"Solve difference of {numbers[0]} and {numbers[1]}!")
        loop = 0

    else:
        print("What the fuck are you typing")

# Check the answer
try:
    if int(ans) == correct_ans:
        print(P.tries)
        print("Correct!")
    else:
        print(P.tries)
        print("Wrong!")
        P.tries -= 1
        print(P.tries)
except ValueError:
    print(P.tries)
    print("Wrong!")
    P.health -= 1
    print(P.tries)

checkdead()

