# Problem 2 – batting average

def comp_bat_avg(hits, at_bats):
    if at_bats > 0:
        return hits / at_bats
    else:
        return 0.0


player_count = 0

response = input("Do you want to enter a player? Enter Yes or No: ")

while response.lower() == "yes":
    last_name = input("Enter player's last name: ")
    hits = float(input("Enter number of hits: "))
    at_bats = float(input("Enter number of at bats: "))

    avg = comp_bat_avg(hits, at_bats)

    print(f"Player: {last_name}, Batting average: {avg:.3f}")

    player_count += 1
    response = input("Do you want to enter another player? Enter Yes or No: ")

print("Number of players entered:", player_count)
