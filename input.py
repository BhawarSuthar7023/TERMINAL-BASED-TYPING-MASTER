import random
import time
from termcolor import colored

def wpm_measure_and_display_Results(random_words):


    start_time = time.time()

    typed_words_by_user = [] #storing correct words typed by user

    for word in random_words:
        print(word,end=" ")
        user_typing = input()
        if user_typing == word:
            typed_words_by_user.append("True")
    
    end_time = time.time()
    time_taken_by_user = end_time - start_time

    WPM = ( len(typed_words_by_user) / time_taken_by_user )
    WPM = WPM * 60  #to convert
    correct_words_count = len(typed_words_by_user)

    return WPM
def input_taken():
    print()
    print("*★*――――*★**★*――――*★**★*――――*★**★*――――*★*")
    print(colored(" Welcome to Terminal Typing Master 🎮 :-","magenta",attrs=["bold"]))
    print("*★*――――*★**★*――――*★**★*――――*★**★*――――*★*")
    print()
    Username = input("Enter Your Username :- ")
    
    while (username_exists_or_not(Username)) == True:
        print("Username is already exists.")
        Username = input("Enter Your Username :- ")
    while True:
        print()
        print("Features :- ")
        print("-----*------")
        print("1. Start Typing Test ")
        print("2. Show the LeaderBoard")
        print("3. Exit the Game")
        choice = input("Select Your Choice :-")
        if choice == "1":
            user_choice = input("How many Words you want to type(1-9) :- ")
            while int(user_choice) < 1 or int(user_choice) > 9:
                print(" Invalid Input 🥺")
                user_choice = input("How many Words you want to type(1-9) :- ")
            
            Words = load_words_from_json_function()
            count_of_Words = len(list(Words))
            random_words = random.sample(list(Words),int(user_choice))
            # collect_data
            data = wpm_measure(random_words) #data = [wpm,correct_words,time_taken]
            # displaying_the_result
            print("---------------")
            print("Results 📈 :-")
            print("--------------")
            print()
            print(f" Username ==> {Username}")
            print()
            print(f" Correct Words ==> {data[1]}/{len(random_words)}.")
            print(f" Time Taken. ==> {data[2]:.2f} seconds")
            print(f" Words Per Minute (WPM) ==> {data[0]:.2f}")
            # update in leaderboard
            update_leaderboard(Username,data[0])
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print("*★*――――*★**★*――――*★**★*――――*★**★*――――*★*")
            print(colored("Thanks For Playing Game.","magenta"))
            print()
            print(colored(" ❤️  From (BHNAWAR LAL SUTHAR)","grey"))
            break
        else:
            print("Invalid Input 🥺")
            continue