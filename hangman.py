import random

fruits = ["apple", "banana", "grape", "orange", "mango", "peach", "cherry", "lemon", "melon", "berry"]

cs = [
    "python", "programming", "algorithm", "computer", "science", "development", "software", "keyboard", "mouse",
    "internet", "database", "variable", "function",
    "compiler", "hardware"
]

animals = ["tiger", "lion", "zebra", "panda", "whale", "shark", "eagle", "camel", "koala", "rabbit"]

hangman_stages = [
    """
     _______
     |     |
     |
     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    /
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    / \\
     |
    _|_
    """
]

def display_word(secret_word_as_char, correct_answer):
    for char in secret_word_as_char:
        if char in correct_answer:
            print(f'{char}', end=" ")  
        else:
            print("_", end=" ")
    print()

def topic():
    while True:
        topic = input("what topic do you want the game to be aroud? (animals/fruits/cs): \n\n")
        if topic.lower() in ["animals", "fruits", "cs"]:
            print(f'you chose {topic} as the topic!!\n\n')
            return topic
        elif topic.lower() == "quit":
            exit()
        else:
            print(f'{topic} is an invalid topic')
            print("type 'quit' if you want to stop playing")

def secret_word(topic):
    match topic:
        case "animals":
            secret_word = random.choice(animals)
        case "fruits":
            secret_word = random.choice(fruits)
        case "cs":
            secret_word = random.choice(cs)
    return secret_word

def guess(secret_word):
    secret_word_as_char = list(secret_word)
    correct_answer = []
    lives = 6

    print(f'Guess The Secret Word!       lives:{lives}\n')
    print(hangman_stages[0])
    display_word(secret_word_as_char, correct_answer)

    while lives > -1 and not all(item in correct_answer for item in secret_word_as_char):
        guess = input("\n\nGuess a letter From The Word: ")

        if len(guess) == 1:
            if guess in secret_word_as_char:
                correct_answer.append(guess)
                print("Correct!")
            else:
                lives -= 1
                print(f'{guess} is incorrect.\n attempts left: {lives}')

          
            match lives:
                case 6:
                    print(hangman_stages[0])
                case 5:
                    print(hangman_stages[1])
                case 4:
                    print(hangman_stages[2])
                case 3:
                    print(hangman_stages[3])
                case 2:
                    print(hangman_stages[4])
                case 1:
                    print(hangman_stages[5])
                case 0:
                    print("___GAME OVER___")
                    print(hangman_stages[6])

            display_word(secret_word_as_char, correct_answer)

        elif len(guess) > 1 or len(guess) < 1:
            print("Guesses can only be 1 letter.")

    if all(item in correct_answer for item in secret_word_as_char):
        print("\nCongratulations! You guessed the word correctly!")
    else:
        print("\nBetter luck next time!")

def hangman():
    chosen_topic = topic()  
    word = secret_word(chosen_topic) 
    
    guess(word)

hangman()
