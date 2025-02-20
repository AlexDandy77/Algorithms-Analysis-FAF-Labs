import time
import matplotlib.pyplot as plt
import pandas as pd

def fibonacci_matrix(n):
    def multiply_matrix(A, B):
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

    def power_matrix(M, n):
        if n == 1:
            return M
        if n % 2 == 0:
            half_power = power_matrix(M, n // 2)
            return multiply_matrix(half_power, half_power)
        else:
            return multiply_matrix(M, power_matrix(M, n - 1))

    if n == 0:
        return 0
    F = [[1, 1], [1, 0]]
    result = power_matrix(F, n - 1)
    return result[0][0]

if __name__ == "__main__":
    input_set = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
    execution_times = []

    print("\nMatrix Fibonacci Execution Times:")
    for n in input_set:
        start_time = time.time()
        fibonacci_matrix(n)
        elapsed_time = time.time() - start_time
        execution_times.append(elapsed_time)

    df = pd.DataFrame([execution_times], columns=input_set)
    print(df.to_string(index=False))

    plt.figure(figsize=(8, 5))
    plt.plot(input_set, execution_times, marker='o', linestyle='-')
    plt.title("Matrix Fibonacci Function")
    plt.xlabel("n-th Fibonacci Term")
    plt.ylabel("Time (s)")
    plt.grid()
    plt.show()
