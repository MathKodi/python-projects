import art
print(art.logo)

bidders = {}
more_bidders = True
while more_bidders:
    name = input("What is your name?:\n")
    bid = int(input("What is your bid?:\n"))
    bidders[name] = bid
    aux = input("Is there any others bidders? type 'yes' or 'no':\n")
    if aux == "no":
        more_bidders = False
    print("\n" * 50)

highest_bid_name = ""
highest_bid = 0

for key in bidders:
    if bidders[key] > highest_bid:
        highest_bid = bidders[key]
        highest_bid_name = key

print(f"The winner is {highest_bid_name} with a bid of ${highest_bid}")