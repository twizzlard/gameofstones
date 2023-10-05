def calculate_optimal_move(n, memo):
    if n <= 0:
        return False  # Bob wins
    if n == 1:
        return True   # Alice wins

    if memo[n] is not None:
        return memo[n]

    for move in range(1, 4):
        if not calculate_optimal_move(n - move, memo):
            memo[n] = True
            return True

    memo[n] = False
    return False

def automatic_mode():
    n = int(input("Enter the number of stones in the pile: "))
    memo = [None] * (n + 1)

    while n > 0:
        alice_move = 1
        while alice_move <= 3 and (n - alice_move < 0 or not calculate_optimal_move(n - alice_move, memo)):
            alice_move += 1

        print(f"Alice removed {alice_move} stones.")
        n -= alice_move

        if n == 0:
            print("Alice wins!")
            break

        bob_move = 1
        while bob_move <= 3 and (n - bob_move < 0 or not calculate_optimal_move(n - bob_move, memo)):
            bob_move += 1

        print(f"Bob removed {bob_move} stones.")
        n -= bob_move

    if n < 0:
        print("Bob wins!")

def human_vs_computer_mode():
    n = int(input("Enter the number of stones in the pile: "))

    while n > 0:
        computer_move = 1
        while computer_move <= 3 and (n - computer_move < 0 or not calculate_optimal_move(n - computer_move, [None] * (n + 1))):
            computer_move += 1

        print(f"Computer removed {computer_move} stones.")
        n -= computer_move

        if n == 0:
            print("Computer wins!")
            break

        human_move = int(input("Enter the number of stones you want to remove (1-3): "))
        if human_move < 1 or human_move > 3 or n - human_move < 0:
            print("Invalid move. Try again.")
            continue

        n -= human_move

    if n < 0:
        print("You win!")

mode = int(input("Choose a mode (1 for automatic, 2 for human vs computer): "))

if mode == 1:
    automatic_mode()
elif mode == 2:
    human_vs_computer_mode()
else:
    print("Invalid mode selection.")
