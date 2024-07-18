import time
import random

class GettingBoredException(Exception):
    pass

def code():
    print("Coding...")
    # Simulate random chance of getting bored
    if random.randint(1, 5) == 1:  # 20% chance of getting bored
        raise GettingBoredException("Getting bored of coding...")
    time.sleep(1)  # Simulate time spent coding

def take_break():
    print("Taking a break... Grabbing a coffee.")
    time.sleep(2)  # Simulate break time

def internship():
    print("Starting internship at Codesoft!")
    deadline = 10  # Example deadline (in seconds)
    start_time = time.time()
    
    while (time.time() - start_time) < deadline:
        try:
            code()
        except GettingBoredException as e:
            print(e)
            take_break()
    
    print("Deadline reached! Internship coding session ended.")
    
    # Ask the user if they can be the best intern
    while True:
        answer = input("Can I be the best intern? ").strip().lower()
        if answer == "yes":
            print("Thank you, Codsoft.")
            break
        else:
            print("You must answer 'yes' to proceed!")

# Run the internship simulation
internship()
