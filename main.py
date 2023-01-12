from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to thesecret auction progamme.")

more_bidders = True
bid_dictionary = {}


def highest_bidder(cumulative_bidding):
    highest_bid = 0
    winner = ""
    for bidder in cumulative_bidding:
        bid_amount = int(cumulative_bidding[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of €{highest_bid}.")


while more_bidders:
    name = input("What is your name?\n")
    bid = input("What is your highest bid?\n€")

    bid_dictionary[name] = bid

    more_bids = input("Are there any more bidders? Enter 'Yes' or 'No'\n")
    if more_bids == "No":
        more_bidders = False
        clear()
        highest_bidder(bid_dictionary)
    if more_bidders:
        clear()


