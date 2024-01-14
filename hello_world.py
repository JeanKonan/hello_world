name = input("Hey! What is your name? ")

if name != "":
    print(f"Hello {name}! ")
    feeling = input("How are you doing today? ")
    
    me = "Leo"
    
    if feeling.lower() == "bad":
        print(f"Oh sorry! My name is {me}")
        help = input("Is there anything I can do help you feel better? ")
    else:
        print(f"Oh great! My name is {me} and I am pleased to meet you!")