
#Play checks the user input for 'y' or 'n'.  keepGoing will be set to true if discount-skynet 
# makes a correct guess and is used to break out of the loop.  Memory start off as the mainMemory dictionary, which
# will contain the root animals and their actions.  As the dictionary grows in size, the memory will be moving around
# and used as a reference to mainMemory.  That way mainMemory can be updated through the memory reference.  
def play(mainMemory):
    memory = mainMemory
    #key will start off as the root action, but will eventually change to depending on the level we are in the 
    # "tree"
    key = next(iter(mainMemory))
    while key:
        answer = input(f"Does the animal {key}, Y or N\n")
        #makes sure that uppercase and lowercase both work
        answer = answer.lower()
        if(answer == "y"):
            #The only difference is the index, 0 and 1, which will indicate which direction
            #we will traverse when guessing the animal, 0 for left, and 1 for right
            keepGoing, memory, key = learn(memory, key, 0)
            if(keepGoing):
                break
        elif(answer == "n"):
            keepGoing, memory, key = learn(memory, key, 1)
            if(keepGoing):
                break

def learn(memory, key, index):
    #This will determine if the node is a leaf node, in which case we no longer need to keep traversing
    #since there is only one option left
    if(isinstance(memory[key][index], str)):
        #memory[key][index] will be a str if its not a list, because it will be a leaf node if it ever gets here
        answer = input(f"Is it a {memory[key][index]}\n")
        answer = answer.lower()
        if(answer == "y"):
            #if the animal was guessed correctly, the True is returned so that we can break out of the traversal loop
            #memory and key are returned because I set up the whole function to return three things
            #even though memory and key are not needed since we won't be traversing any longer
            print(f"I am becoming self aware, I guessed correctly that it was a {memory[key][index]}\n")
            return True, memory, key
        elif(answer == "n"):
            #if the answer is no, then the mainMemory will be updated/grow
            #action will be the new key of the current node, noun will be the left child since a yes will
            #correspond to it and the previous animal will be moved to the right, since a no corresponds to it
            key = next(iter(memory))
            action = input(f"What does the animal do?\n")
            noun = input(f"What animal is it?\n")
            print("Thanks for teaching me, I will do better next time!")
            #temp will represent the new node and its children via a dictionary
            #the new action will be the new node, and the noun will be on the left, since the noun is the 
            #animal that performs the action, and the old animal which can be accessed using memory[key][index]
            #will now be moved to the left, because it doesn't perform the new action
            temp = {action: [noun, memory[key][index]]}
            #add the new node and its children to the old location in mainMemory
            memory[key][index] = temp
            memory = memory[key]
            #break out of the loop after updating
            return True, memory, key
    else:
        #If we get here, its because this isn't a leaf node and we have to traverse it
        #if 0, then traverse left, if 1, then traverse right
        memory = memory[key][index]
        #once we traverese, update the key to the new node, that way we can check the new node values again
        key = next(iter(memory))
        #key and memory are updated and returned since we want to see the changes outside of this function
        #False prevents the loop from breaking and allows the program to traverse
        return False, memory, key
    
def main():
    #The dictionary will represent a "binary tree" in a way, even though its just a dictionary
    #Each key/node will contain a list that has two items/nodes
    mainMemory = { "bark": ["dog", "cat"]}
    print("Hi, I am Discount Skynet.  Lets play a game.\nYou pick an animal and I try to guess what the animal is.\nIf I fail, tell me what animal it is and what it can do,\nso I can help humanity.\n\n")
    #This allows the program to run again until the user decides to quit
    while True:
        quit = input("Enter to play or 'Q' to quit\n")
        if(quit.lower() == 'q'):
            break
        else:
            play(mainMemory)
main()
