import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
playersum =[]
def pick_two(cards):
    return random.sample(cards, 2)

def pick_one(cards):
    return random.sample(cards, 1)
    


def playerturn(playersum):
    player = pick_two(cards)
    playersum = sum(player)
    while True:
        choice = input(f"You have {playersum}, hit or stay? type y for hit, n for stay")
        if choice == "y":
            player += pick_one(cards)
            playersum = sum(player)
            print(playersum)

        else:
            print(playersum)
            break
    print(playersum)
        
    
    
    
    
playerturn(playersum)


   
    
    


    

    
    

    



        