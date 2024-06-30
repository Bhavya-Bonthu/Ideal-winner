def guess_number(low, high):
    print(f"Think of a number between {low} and {high} and I'll try to guess it.")
    
    guesses = 0
    while low <= high:
        mid = (low + high) // 2
        guesses += 1
        print(f"Is your number {mid}?")
        user_input = input("Enter 'h' if your number is higher, 'l' if your number is lower, or 'c' if the guess is correct: ").lower()
        
        if user_input == 'h':
            low = mid + 1
        elif user_input == 'l':
            high = mid - 1
        elif user_input == 'c':
            print(f"Yay! I guessed your number {mid} correctly in {guesses} guesses.")
            return
        else:
            print("Invalid input, please enter 'h', 'l', or 'c'.")
    
    print("It seems there was a mistake. Let's try again.")

# Example usage:
guess_number(1, 100)
