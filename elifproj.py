def iterationApproach(mainMemory):
    memory = mainMemory
    key = next(iter(mainMemory))
    temp = []
    while key:
        answer = input(f"Does the animal {key}, Y or N\n")
        answer = answer.lower()
        if(answer == "y"):
            if(isinstance(memory[key][0], str)):
                answer = input(f"Is it a {memory[key][0]}\n")
                answer = answer.lower()
                if(answer == "y"):
                    print(f"Yay, I guessed that it was a {memory[key][0]}\n\n")
                    break
                elif(answer == "n"):
                    key = next(iter(memory))
                    action = input(f"What does the animal do?\n")
                    noun = input(f"What animal is it?\n")
                    temp = {action: [noun, memory[key][0]]}
                    memory[key][0] = temp
                    memory = memory[key]
                    break; 
            else:
                memory = memory[key][0]
                key = next(iter(memory))
        elif(answer == "n"):
            if(isinstance(memory[key][1], str)):
                answer = input(f"Is it a {memory[key][1]}\n")
                answer = answer.lower()
                if(answer == "y"):
                    print(f"Yay, I guessed that it was a {memory[key][1]}\n\n")
                    break
                elif(answer == "n"):
                    key = next(iter(memory))
                    action = input(f"What does the animal do?\n")
                    action = action.lower()
                    noun = input(f"What animal is it?\n")
                    noun = noun.upper()
                    temp = {action: [noun, memory[key][1]]}
                    memory[key][1] = temp
                    memory = memory[key]
                    break; 
            else:
                memory = memory[key][0]
                key = next(iter(memory))
       
def main():
    mainMemory = { "bark": ["Dog", "Cat"]}
    print("Hi, I am Discount Skynet.  Lets play a game.\nYou pick an animal and I try to guess what the animal is.\nIf I fail, tell me what animal it is and what it does, so I can learn to help humanity.\n\n")
    while True:
        quit = input("Enter to play or 'Q' to quit")
        if(quit.lower() == 'q'):
            break
        else:
            iterationApproach(mainMemory)
main()
