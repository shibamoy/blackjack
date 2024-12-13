import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
playersum =[]

def pick_two(cards):
    return random.sample(cards, 2)

def pick_one(cards):
    return random.sample(cards, 1)
    
def dealerturn():    
    dealer = pick_two(cards)
    dealersum = sum(dealer)
    print(f"Dealer: {dealer[0]}")
    while dealersum < 17:
        dealer += pick_one(cards)
        dealersum = sum(dealer)
        print(dealersum)
        if dealersum == 21:
            print("Dealer has 21.")
        elif dealersum > 21:
            print("dealer bust!")
        else:
            print(f"Dealer has {dealersum}")

def playerturn(playersum):
    player = pick_two(cards)
    playersum = sum(player)
    dealer = pick_two(cards)
    dealersum = sum(dealer)
    print(f"Dealer: {dealer[0]}")

    while True:
        choice = input(f"You have {playersum}, hit or stay? type y for hit, n for stay")
        if choice == "y":
            player += pick_one(cards)
            playersum = sum(player)
            
            if playersum > 21:
                print(f"{playersum} bust! You lose")
                break
            if playersum == 21:
                print("21!Auto stay")
                break
        else:
            break

        
    while dealersum < 17:
        dealer += pick_one(cards)
        dealersum = sum(dealer)
        if dealersum == 21:
            print("Dealer has 21.")
        elif dealersum > 21:
            print("dealer bust!")
    print(dealersum)
    if dealersum > playersum and dealersum < 22:
        print("Dealer wins")
    if dealersum < playersum and dealersum < 22:
        print("You win!")
    print("\n" * 20)

    
    
# dealerturn()
while True:
    playerturn(playersum)


   
    
    


    

    
    

    



        