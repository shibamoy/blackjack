import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
player_sum =[]
def pick_two(cards):
    return random.sample(cards, 2)

def pick_one(cards):
    return random.sample(cards, 1)
    


def playerturn(player_sum):
    player = pick_two(cards)
    player_sum = sum(player)
    while True:
        choice = input(f"You have {player_sum}, hit or stay? type y for hit, n for stay")
        if choice == "y":
            player += pick_one(cards)
            player_sum = sum(player)
            print(player_sum)

        else:
            print(player_sum)
            break
    print(player_sum)
        
    
    
    
    
playerturn(player_sum)


   
    
    


    

    
    

    



        
