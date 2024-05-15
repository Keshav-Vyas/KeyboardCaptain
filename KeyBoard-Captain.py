import time
from essential_generators import DocumentGenerator

def typing_speed():
    # Generate a random sentence using DocumentGenerator
    gen = DocumentGenerator()
    random_sentence = gen.sentence()
    wordcount = len(random_sentence.split())  # Count words in the generated sentence

    # Typing Speed Calculation
    print(random_sentence)  # Display the generated sentence
    print("----------------------------------------")
    start_time = time.time()  # Record the start time of typing
    user_input = str(input("Type the sentence: "))
    end_time = time.time()  # Record the end time of typing
    accuracy = len(set(user_input.split()) & set(random_sentence.split()))  # Calculate accuracy
    accuracy = accuracy / wordcount * 100  # Convert accuracy to percentage
    time_taken = round(end_time - start_time, 2)  # Calculate time taken
    wpm = round((wordcount / time_taken) * 60)  # Calculate words per minute (wpm)
    print("----------------------------------------")

    # Show the results
    print("Your accuracy is:", accuracy)
    print("Time taken:", time_taken, "seconds")
    print("Your typing speed is:", wpm, "words per minute")

    # Provide feedback based on performance
    if accuracy < 50 or wpm < 30:
        print("You need to practice typing more!")
    elif accuracy < 80 or wpm < 60:
        print("You are doing great!")
    elif accuracy <= 100 or wpm <= 100:
        print("You are a pro in typing!")
    else:
        print("You are a typing machine!")

if __name__ == "__main__":
    print("Starting Keyboard-Captain...")
    typing_speed()

    # Allow user to try again
    while True:
        if input("Do you want to try again? (y/n): ") == "y":
            print("\n")
            typing_speed() 
        else:
            print("Thank you for using Keyboard-Captain, Have a Good Day...")
            break  

