from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bid(bid_record):
  # ex.bid_record = {"John": 120, "Doe": 210}
  highest_bid = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")
      

while not bidding_finished:
  name = input("What's your name?: ")
  price = int(input("What's your bid?: $"))
  bids[name] = price
  should_continue = input("Are there anymore bidders? 'yes' or 'no'.:")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bid(bids)
  elif should_continue == "yes":
    clear()