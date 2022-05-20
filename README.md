# discount-skynet

Hi, I am Discount Skynet.  Lets play a game. 
You pick an animal and I try to guess what the animal is.
If I fail, tell me what animal it is and what it does, so I can learn to help humanity.

The elifproj.py and refactored.py do the same thing.  The refactored.py is just a refactored version of elifproj.py

To run the project:

```
python3 refactored.py
```

or

```
python3 elifproj.py
```


Discount Skynet demonstrates the use of if/else/elif statements, while loops, and dictionaries.  The dictionary functions like a decision tree and grows as the user enters information.  If the animal is not already in the dictionary, the animal is added to it so that the program can "learn".

If the animal barks, it can be a dog, otherwise it may be a cat.

<img width="1094" alt="Screen Shot 2022-05-20 at 12 22 21 PM" src="https://user-images.githubusercontent.com/9085803/169597772-78bb4e92-6872-4a89-8212-20aec9f5bda0.png">

If the animal does bark, but its not a dog, it gets added to the dictionary.  If the animal barks and swims, it may be a barking fish.  If the animal barks, but doesn't swim, it may be a dog.

<img width="583" alt="Screen Shot 2022-05-20 at 12 22 28 PM" src="https://user-images.githubusercontent.com/9085803/169597781-a71919ea-de6b-46b2-8f8d-b38280006d0d.png">

If the animal barks, doesn't swim, but flies, it may be a barking bird.  If the animal barks, doesn't swim and fly, then it may be a dog.

<img width="547" alt="Screen Shot 2022-05-20 at 12 22 33 PM" src="https://user-images.githubusercontent.com/9085803/169597789-eb4cd082-6c6c-4f97-8451-854e3f0adee2.png">
