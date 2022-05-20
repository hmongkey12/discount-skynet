def iterationApproach(mainMemory):
    memory = mainMemory
    key = next(iter(mainMemory))
    while key:
        answer = input(f"Does the animal {key}, Y or N\n")
        answer = answer.lower()
        if(answer == "y"):
            keepGoing, memory, key = learn(memory, key, 0)
            if(keepGoing):
                break
        elif(answer == "n"):
            keepGoing, memory, key = learn(memory, key, 1)
            if(keepGoing):
                break

def learn(memory, key, index):
    if(isinstance(memory[key][index], str)):
        answer = input(f"Is it a {memory[key][index]}\n")
        answer = answer.lower()
        if(answer == "y"):
            print(f"I am becoming self aware, I guessed correctly that it was a {memory[key][index]}\n")
            return True, memory, key
        elif(answer == "n"):
            key = next(iter(memory))
            action = input(f"What does the animal do?\n")
            noun = input(f"What animal is it?\n")
            print("Thanks for teaching me, I will do better next time!")
            temp = {action: [noun, memory[key][index]]}
            memory[key][index] = temp
            memory = memory[key]
            return True, memory, key
    else:
        memory = memory[key][index]
        key = next(iter(memory))
        return False, memory, key
    
def main():
    mainMemory = { "bark": ["dog", "cat"]}
    print("Hi, I am Discount Skynet.  Lets play a game.\nYou pick an animal and I try to guess what the animal is.\nIf I fail, tell me what animal it is and what it can do,\nso I can help humanity.\n\n")
    while True:
        quit = input("Enter to play or 'Q' to quit\n")
        if(quit.lower() == 'q'):
            break
        else:
            iterationApproach(mainMemory)
main()
