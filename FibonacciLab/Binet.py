import time
import matplotlib.pyplot as plt
import pandas as pd
import math
from decimal import Decimal, getcontext

getcontext().prec = 500


def fibonacci_binet(n):
    phi = Decimal((1 + math.sqrt(5)) / 2)
    psi = Decimal((1 - math.sqrt(5)) / 2)  # (-1/phi)^n
    sqrt5 = Decimal(math.sqrt(5))

    return round((phi ** n - psi ** n) / sqrt5)


if __name__ == "__main__":
    input_set = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012,
                 6310, 7943, 10000, 12589, 15849]

    execution_times = []

    print("\nBinet Fibonacci Execution Times:")
    for n in input_set:
        start_time = time.time()
        try:
            result = fibonacci_binet(n)
            elapsed_time = time.time() - start_time
        except OverflowError:
            result = "Overflow"
            elapsed_time = float('inf')

        execution_times.append(elapsed_time)
        print(f"Fibonacci({n}) = {result if isinstance(result, int) else 'Overflow'}, Time: {elapsed_time:.6f} sec")

    df = pd.DataFrame([execution_times], columns=input_set)
    print("\nExecution Time Table:")
    print(df.to_string(index=False))

    # Plot the execution times
    plt.figure(figsize=(8, 5))
    plt.plot(input_set, execution_times, marker='o', linestyle='-')
    plt.title("Binet Fibonacci Function")
    plt.xlabel("n-th Fibonacci Term")
    plt.ylabel("Time (s)")
    plt.grid()
    plt.show()
