from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
bidder_dict = {}

def bidders(bidder_name, bid_amt):
    bidder_dict[bidder_name] = bid_amt
    
def bid_winner():
    winner = ""
    max_bid = 0

    for bidder in bidder_dict:
        if bidder_dict[bidder] > max_bid:
            max_bid = bidder_dict[bidder]
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${max_bid}")

isBidding = True

while isBidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders(bidder_name=name, bid_amt=bid)
    
    user_add = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if user_add == "no":
        isBidding = False
    elif user_add == "yes":
        clear()
    
bid_winner()
