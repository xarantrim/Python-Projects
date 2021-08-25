from replit import clear

from Blind_auction_bidding_art import logo
print(logo)

end_bid = True
bids = {}


def highest_bidder(bidding_records):
    winner = ""
    max_bid = 0
    for bidder in bidding_records:
        if bidding_records[bidder] > max_bid:
            max_bid = bidding_records[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")


while end_bid:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    add_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if add_bidders == "no":
        end_bid = False
        highest_bidder(bids)
    elif add_bidders == "yes":
        clear()
