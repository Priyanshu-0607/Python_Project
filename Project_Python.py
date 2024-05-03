import random
import time

# User data stored in a dictionary
users = {}

# Function for user registration
def register():
    # Ask user for username
    username = input("Enter username: ")
    # Check if username already exists
    if username in users:
        print("Username already exists. Please choose another username.")
        return None
    else:
        # Ask user for input password and name
        password = input("Enter password: ")
        while True:
            name = input("Enter your name: ")
            # Check if name contains only alphabetic characters
            if name.isalpha():
                # Add user data to the users dictionary with proper nesting
                users[username] = {"password": password, "profile": {"name": name, "score": 0, "games_played": 0, "leaderboard": 0}}
                print("Registration successful. You can now login.")
                return username
            else:
                print("Invalid name. Please enter alphabetic characters only.")
    
# Function for user login
def login():
    # Ask user for input username and password
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Check if username exists and password matches
    if username in users and users[username]["password"] == password:
        print(f"Welcome, {users[username]['profile']['name']}!")
        return username
    else:
        print("Invalid username or password.")
        return None

# Function to view user profile
def view_profile(username):
    print("Profile:")
    print(f"Username: {username}")
    print(f"Name: {users[username]['profile']['name']}")
    print(f"Score: {users[username]['profile']['score']}")
    print(f"Games Played: {users[username]['profile']['games_played']}")

# Function to update user profile
def update_profile(username):
    # Ask user for input new name
    name = input("Enter your name: ")
    # Update user's name in the profile
    users[username]['profile']['name'] = name
    print("Profile updated successfully.")

# Function to generate a secret number based on level and type
def generate_secret_number(level, number_type):
    if level == 'easy':
        max_number = 50
        time_limit = 30
    elif level == 'medium':
        max_number = 100
        time_limit = 45
    elif level == 'hard':
        max_number = 200
        time_limit = 60
    else:
        print("Invalid level. Setting level to easy.")
        max_number = 50
        time_limit = 30

    if number_type == 'basic':
        return random.randint(1, max_number), time_limit
    elif number_type == 'odd':
        return random.choice([num for num in range(1, max_number+1) if num % 2 != 0]), time_limit
    elif number_type == 'even':
        return random.choice([num for num in range(1, max_number+1) if num % 2 == 0]), time_limit
    elif number_type == 'prime':
        primes = [2]
        for num in range(3, max_number+1):
            if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
                primes.append(num)
        return random.choice(primes), time_limit
    else:
        print("Invalid number type. Using normal numbers.")
        return random.randint(1, max_number), time_limit

# Function to play the number guessing game
def play_game(username):
    print("\nSelect Mode:")
    print("1. Single Player")
    print("2. Multiplayer")
    mode_choice = input("Enter your choice: ")

    if mode_choice == "1":
        single_player_game(username)
    elif mode_choice == "2":
        multiplayer_game()
    else:
        print("Invalid choice.")

# Function for single player game
def single_player_game(username):
    print("\nSelect Mode:")
    print("1. Normal Mode")
    print("2. Rapid Round")
    mode_choice = input("Enter your choice: ")

    if mode_choice == "1":
        print("\nSelect Level:")
        print("1. Easy (Guess Number Between 1-50)")
        print("2. Medium (Guess Number Between 1-100)")
        print("3. Hard (Guess Number Between 1-200)")
        level_choice = input("Enter your choice: ")

        if level_choice == "1":
            level = 'easy'
        elif level_choice == "2":
            level = 'medium'
        elif level_choice == "3":
            level = 'hard'
        else:
            print("Invalid choice. Setting level to easy.")
            level = 'easy'

        print("\nSelect Number Type:")
        print("1. Basic")
        print("2. Odd")
        print("3. Even")
        print("4. Prime")
        type_choice = input("Enter your choice: ")

        if type_choice == "1":
            number_type = 'basic'
        elif type_choice == "2":
            number_type = 'odd'
        elif type_choice == "3":
            number_type = 'even'
        elif type_choice == "4":
            number_type = 'prime'
        else:
            print("Invalid choice. Using normal numbers.")
            number_type = 'normal'

        # Generate secret number
        secret_number, _ = generate_secret_number(level, number_type)
        attempts = 0
        while True:
            # Ask user to guess the number
            guess = int(input("Guess the number: "))
            attempts += 1
            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                # Print success message and update user's score and games played
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                users[username]['profile']['games_played'] += 1
                # Update user's score based on the number of attempts
                if attempts <= 5:
                    users[username]['profile']['score'] += 2
                else:
                    users[username]['profile']['score'] += 1
                # Update leaderboard score
                users[username]['profile']['leaderboard'] += users[username]['profile']['score']
                break

    elif mode_choice == "2":
        print("\nSelect Level for Rapid Round:")
        print("1. Easy (Guess Number Between 1-50 in 30 seconds)")
        print("2. Medium (Guess Number Between 1-100 in 45 seconds)")
        print("3. Hard (Guess Number Between 1-200 in 60 seconds)")
        level_choice = input("Enter your choice: ")

        if level_choice == "1":
            level = 'easy'
        elif level_choice == "2":
            level = 'medium'
        elif level_choice == "3":
            level = 'hard'
        else:
            print("Invalid choice. Setting level to easy.")
            level = 'easy'

        print("\nSelect Sub-Mode for Rapid Round:")
        print("1. Basic")
        print("2. Odd")
        print("3. Even")
        print("4. Prime")
        type_choice = input("Enter your choice: ")

        if type_choice == "1":
            number_type = 'basic'
        elif type_choice == "2":
            number_type = 'odd'
        elif type_choice == "3":
            number_type = 'even'
        elif type_choice == "4":
            number_type = 'prime'
        else:
            print("Invalid choice. Using normal numbers.")
            number_type = 'normal'

        # Generate secret number with time limit
        secret_number, time_limit = generate_secret_number(level, number_type)
        start_time = time.time()
        print(f"\nYou have {time_limit} seconds to guess.")
        attempts = 0
        while True:
            if time.time() - start_time > time_limit:
                print("Time's up!")
                break
            # Ask user to guess the number
            guess = int(input("Guess the number: "))
            attempts += 1
            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                # Print success message and update user's score and games played
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                users[username]['profile']['games_played'] += 1
                # Update user's score based on the number of attempts
                if attempts <= 5:
                    users[username]['profile']['score'] += 2
                else:
                    users[username]['profile']['score'] += 1
                # Update leaderboard score
                users[username]['profile']['leaderboard'] += users[username]['profile']['score']
                break

    else:
        print("Invalid choice.")

# Function to handle multiplayer game
def multiplayer_game():
    num_players = int(input("Enter number of players: "))
    players = []
    for i in range(num_players):
        print(f"Player {i+1}:")
        username = login()
        if username:
            players.append(username)
    if len(players) < 2:
        print("Insufficient players for multiplayer game. Need at least 2 players.")
        return
    
    num_rounds = int(input("Enter number of rounds: "))
    for round_num in range(1, num_rounds + 1):
        print(f"\nRound {round_num}:")
        for player in players:
            print(f"\n{users[player]['profile']['name']}, it's your turn!")
            single_player_game(player)

# Function to display leaderboard
def display_leaderboard():
    sorted_users = sorted(users.items(), key=lambda x: x[1]['profile']['leaderboard'], reverse=True)
    print("\nLeaderboard:")
    for i, (username, data) in enumerate(sorted_users, start=1):
        print(f"{i}. Username: {username}, Score: {data['profile']['leaderboard']}")

# Main function to run the program
def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Leaderboard")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                logged_in_menu(username)
        elif choice == "3":
            display_leaderboard()
        elif choice == "4":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Logged-in menu function
def logged_in_menu(username):
    while True:
        print("\nMenu:")
        print("1. Play Game")
        print("2. View Profile")
        print("3. Update Profile")
        print("4. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            play_game(username)
        elif choice == "2":
            view_profile(username)
        elif choice == "3":
            update_profile(username)
        elif choice == "4":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

# Check if the script is being run directly
if __name__ == "__main__":
    main()