import random

def fill_lottery_data(n):
    all_draws = []
    for _ in range(n):
        single_draw = sorted(random.sample(range(1, 50), 6))
        all_draws.append(single_draw)
    return all_draws

def print_lottery_results(all_draws):
    print("\nZestawy wylosowanych liczb:")
    for i, draw in enumerate(all_draws, 1):
        draw_str = " ".join(str(num) for num in draw)
        print(f"Losowanie {i}: {draw_str}")

def calculate_and_print_statistics(all_draws):
    stats = {i: 0 for i in range(1, 50)}
    
    for draw in all_draws:
        for num in draw:
            stats[num] += 1
            
    for num in range(1, 50):
        print(f"Wystąpienia liczby {num}: {stats[num]}")

def main():
    print("Ile wygenerować losowań?")
    try:
        n = int(input())
        if n <= 0:
            print("Liczba losowań musi być większa od 0.")
            return
    except ValueError:
        print("Niepoprawna wartość. Wprowadź liczbę całkowitą.")
        return

    draws_data = fill_lottery_data(n)
    print_lottery_results(draws_data)
    calculate_and_print_statistics(draws_data)

if __name__ == "__main__":
    main()