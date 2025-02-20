import time
import matplotlib.pyplot as plt
import pandas as pd


def fibonacci_tabulation(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


if __name__ == "__main__":
    input_set = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012,
                 6310, 7943, 10000, 12589, 15849]

    execution_times = []

    print("\nTabulation Fibonacci Execution Times:")
    for n in input_set:
        start_time = time.time()
        result = fibonacci_tabulation(n)
        elapsed_time = time.time() - start_time
        execution_times.append(elapsed_time)
        print(f"Fibonacci({n}) = {result}, Time: {elapsed_time:.6f} sec")

    df = pd.DataFrame([execution_times], columns=input_set)
    print("\nExecution Time Table:")
    print(df.to_string(index=False))

    plt.figure(figsize=(8, 5))
    plt.plot(input_set, execution_times, marker='o', linestyle='-')
    plt.title("Tabulation Fibonacci Function")
    plt.xlabel("n-th Fibonacci Term")
    plt.ylabel("Time (s)")
    plt.grid()
    plt.show()
