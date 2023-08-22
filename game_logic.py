import random


def play_round(bet):
    winning_slot = random.randint(1, 30)
    chosen_slot = int(input("Choose a slot (1-30): "))

    if chosen_slot == winning_slot:
        print("Congratulations! You won!")
        return True, bet * 2
    else:
        print("Sorry, you lost.")
        return False, 0


def calculate_total_money(initial_money, current_money):
    if current_money > initial_money:
        print(f"Congratulations! You won ${current_money - initial_money}.")
    elif current_money < initial_money:
        print(f"Sorry, you lost ${initial_money - current_money}.")
    else:
        print("You broke even.")
