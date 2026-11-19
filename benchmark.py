
import subprocess
import time
import csv
import sys

# Programs we want to compare
programs = {
    "C -O0": ["./c_version/prime_O0"],
    "C -O2": ["./c_version/prime_O2"],
    "Python": ["python3", "python_version/prime_count.py"]
}

# Number of times to run each program
repetitions = 5

# Store benchmark results
results = []

for name, command in programs.items():
    print(f"\nBenchmarking {name}...")

    # Warm-up run (not included in results)
    subprocess.run(command, capture_output=True, text=True, check=True)

    for run in range(1, repetitions + 1):
        start = time.perf_counter()

        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        end = time.perf_counter()

        elapsed = end - start

        # Check that the program produced the expected result
        if "9592" not in process.stdout:
            raise ValueError(f"Unexpected output from {name}")

        results.append([name, run, elapsed])

        print(f"Run {run}: {elapsed:.6f} seconds")

# Save results to CSV
with open("results/benchmark_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Program", "Run", "Execution Time (seconds)"])
    writer.writerows(results)

print("\nBenchmark complete!")
print("Results saved to results/benchmark_results.csv")
