import time
import matplotlib.pyplot as plt
import pandas as pd


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    input_set = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
    execution_times = []

    print("\nRecursive Fibonacci Execution Times:")
    for n in input_set:
        start_time = time.time()
        try:
            fibonacci_recursive(n)
            elapsed_time = time.time() - start_time
        except RecursionError:
            elapsed_time = float('inf')
        execution_times.append(elapsed_time)

    df = pd.DataFrame([execution_times], columns=input_set)
    print(df.to_string(index=False))

    plt.figure(figsize=(8, 5))
    plt.plot(input_set, execution_times, marker='o', linestyle='-')
    plt.title("Recursive Fibonacci Function")
    plt.xlabel("n-th Fibonacci Term")
    plt.ylabel("Time (s)")
    plt.grid()
    plt.show()
