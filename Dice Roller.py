import random

def roll_dice(num_dice):
    print("\nRolling the dice...")
    results = [random.randint(1, 6) for _ in range(num_dice)]
    
    print("\nResults:")
    for i, result in enumerate(results, start=1):
        print(f"Die {i}: {result}")
    
    print("\nTotal: ", sum(results))

def main():
    print("Welcome to the Dice Rolling App!")
    
    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? "))
            if num_dice < 1:
                raise ValueError
            roll_dice(num_dice)
        except ValueError:
            print("Please enter a valid number of dice (1 or more).")
        
        play_again = input("Roll the dice again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for rolling the dice! Goodbye.")
            break

if __name__ == "__main__":
    main()
