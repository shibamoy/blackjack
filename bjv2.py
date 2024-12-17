import random
# cards = [
#     1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4,
#     5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
#     9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
# ]
cards = [1,10]
#test
def pick_two(cards):
    return random.sample(cards, 2)

def pick_one(cards):
    return random.sample(cards, 1)

def playerturn():
    player = pick_two(cards)
    playersum = sum(player)
    dealer = pick_two(cards)
    dealersum = sum(dealer)
    print(f"Dealer: {dealer[0]}")
    if 1 and 10 in player:
        print("Congrats you win. Blackjack!")
        if 1 and 10 in dealer:
            print("Dealer too...")
        return
    while True:
        choice = input(f"You have {playersum}, hit or stay? type y for hit, n for stay")
        if choice == "y":
            player += pick_one(cards)
            playersum = sum(player)
            print(player)
            if 1 in player and playersum < 22:
                playersum += 10
                if playersum > 21:
                    playersum -= 10

            if playersum > 21:
                print(f"{playersum} bust! You lose")
                break
            if playersum == 21:
                print("21! Auto stay")
                break
        else:
            break
    if playersum > 21:
        return
    while dealersum < 17:
        dealer += pick_one(cards)
        dealersum = sum(dealer)
        print(dealer)
        if 1 in dealer and dealersum <= 21:
            dealersum += 10
            if dealersum > 21:
                dealersum -= 10
        if dealersum == 21:
            print("Dealer has 21.")
        elif dealersum > 21:
            print(f"dealer has {dealersum}. bust!")
    if dealersum > playersum and dealersum < 22:
        print(f"Dealer wins. Dealer has {dealersum}")
    if dealersum < playersum and playersum < 22:
        print(f"You win! Dealer has {dealersum}")
    if dealersum == playersum:
        print("Push.")

while True:
    start = input("Would you like to play blackjack? y for yes, n for no.").lower()
    if start == "y":
        playerturn()
        print("\n" * 5)
    else:
        break
