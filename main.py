
from art import logo
print(logo)

bids={}
biddind_finished = False

def highest_bidder(bidding_record):
    highest_amount = 0
    winner = ""
    for bidder in bidding_record:
       bid_amount =  bidding_record[bidder]
       if bid_amount > highest_amount:
           highest_amount = bid_amount
           winner = bidder
    print(f"the winner is {winner} with amount {highest_amount}")


while not biddind_finished:
    name = input("what is your name??" )
    price = int(input("what is your amount to give??" ))
    bids[name] = price

    should_continue = input("is there any other bidders?? type yes or no")
    if should_continue == "no":
        biddind_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        print("dont see the previous amount.. hahaha")