import csv
import statistics

results = {
    "C -O0": [],
    "C -O2": [],
    "Python": []
}

# Read the benchmark results
with open("results/benchmark_results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        program = row["Program"]
        execution_time = float(row["Execution Time (seconds)"])
        results[program].append(execution_time)

# Calculate averages and medians
averages = {}

print("BENCHMARK RESULTS")
print("-----------------")

for program, times in results.items():
    average = statistics.mean(times)
    median = statistics.median(times)

    averages[program] = average

    print(f"\n{program}")
    print(f"Average: {average:.6f} seconds")
    print(f"Median:  {median:.6f} seconds")

# Calculate speedup
print("\nSPEEDUP COMPARISONS")
print("-------------------")

for program in ["C -O0", "C -O2"]:
    speedup = averages["Python"] / averages[program]
    print(f"{program} was {speedup:.2f}x faster than Python.")