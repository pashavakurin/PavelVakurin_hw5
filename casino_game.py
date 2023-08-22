from game_logic import play_round, calculate_total_money
from decouple import config


def main():
    initial_money = int(config("MY_MONEY"))
    current_money = initial_money

    while current_money > 0:
        print(f"Your current money: ${current_money}")
        bet = int(input("Place your bet: "))

        if bet > current_money:
            print("You can't bet more than your current money.")
            continue

        result, won_amount = play_round(bet)
        current_money += won_amount if result else -bet

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    calculate_total_money(initial_money, current_money)


if __name__ == "__main__":
    main()
