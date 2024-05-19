import random

chance = int(input("Enter number of rounds you want to play: "))

while (chance):
    # List of Bolldwood movies
    movies = ['Dilwale Dulhania Le Jayenge', 'Dhoom', 
            'Kabhi Khushi Kabhie Gham','Lagaan']

    # Choose a random movie from the list
    movie_to_guess = random.choice(movies)
    movie_to_guess = movie_to_guess.replace(" ","")
    word_length = len(movie_to_guess)
    display = ['_'] * word_length
    guessed_letters = []
    remaining_lives = 6

    print("Welcome to Hangman Game! Let's play with Bollywood movies.")
    print(f"The movie title has {word_length} letters or numbers and it doesn't contain any spaces name is written using camel casing.")

    while True:
        print(f"\nLives remaining: {remaining_lives}")
        print(' '.join(display))

        if '_' not in display:
            print(f"Congratulations! You guessed the movie '{movie_to_guess}'.")
            print(f"You scored {remaining_lives*10} points.")
            chance -= 1
            break

        if remaining_lives == 0:
            print(f"Game Over! The movie was '{movie_to_guess}'.")
            print("You scored 0 points.")
            chance -= 1
            break

        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalnum():
            print("Invalid input. Please enter a single letter or number.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in movie_to_guess.upper():
            indices = [i for i, letter in enumerate(movie_to_guess.upper()) if letter == guess]
            for index in indices:
                display[index] = movie_to_guess[index]
        else:
            remaining_lives -= 1
            print(f"'{guess}' is not in the movie title.")
