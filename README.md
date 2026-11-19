 C vs Python: Performance Benchmarking

Project Overview

This project compares the execution performance of C and Python by measuring how long each language takes to count prime numbers up to 100,000.

The project also compares two C compiler optimization levels:
- C with `-O0` (no compiler optimization)
- C with `-O2` (compiler optimization)

Python is included as the third implementation.

Project Structure

text
c-vs-python-benchmark/
├── c_version/
│   └── prime_count.c
├── python_version/
│   └── prime_count.py
├── results/
│   └── benchmark_results.csv
├── benchmark.py
└── README.md


 How to Run
 1. Compile the C programs

bash
gcc -O0 c_version/prime_count.c -o c_version/prime_O0
gcc -O2 c_version/prime_count.c -o c_version/prime_O2


 2. Run the benchmark

bash
python3 benchmark.py


The benchmark runs each implementation five times and saves the execution times in `results/benchmark_results.csv`.

 3. Run individual programs

bash
./c_version/prime_O0
./c_version/prime_O2
python3 python_version/prime_count.py


Methodology

- All three implementations perform the same prime-counting task.
- Each program counts prime numbers from 2 through 100,000.
- Each implementation is run five times for measurement.
- A warm-up run is performed before collecting measurements.
- Execution time is measured using Python's `time.perf_counter()`.
- C compilation happens before timing begins.

The benchmark measures total program execution time, including process startup.

Results

The measured execution times are saved in `results/benchmark_results.csv`.

All implementations should produce the same result: **9,592 prime numbers**.

Each implementation was measured five times.

| Implementation | Average Time (seconds) | Median Time (seconds) |
|---|---:|---:|
| C -O0 | 0.016353 | 0.015598 |
| C -O2 | 0.014353 | 0.013812 |
| Python | 0.172517 | 0.175819 |

Key Findings

- C -O0 was approximately 10.55 times faster than Python.
- C -O2 was approximately 12.02 times faster than Python.
- Compiler optimization reduced C's average execution time by approximately 12.2%.

These results suggest that C executed this particular prime-counting task faster than Python on the tested environment.

Tools and Technologies

- C
- Python
- GCC
- Git and GitHub
- CSV
