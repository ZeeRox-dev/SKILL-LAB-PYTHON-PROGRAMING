import random
import os
from collections import Counter

# Generate 100 random memory addresses in range 0x0000 to 0x0FFF
addresses = [random.randint(0x0000, 0x0FFF) for _ in range(100)]

# Identify duplicate addresses and display frequency
address_counts = Counter(addresses)
duplicates = {addr: count for addr, count in address_counts.items() if count > 1}

print("Duplicate Addresses:")
for addr, count in duplicates.items():
    print(f"  0x{addr:04X}: appears {count} times")

# Randomly select 10 addresses for additional testing
selected_addresses = random.sample(addresses, 10)
print("\nSelected addresses for additional testing:")
for addr in selected_addresses:
    print(f"  0x{addr:04X}")

# Create directory and save addresses
os.makedirs("test_data", exist_ok=True)
with open("test_data/addresses.txt", "w") as f:
    for addr in addresses:
        f.write(f"0x{addr:04X}\n")

print("\nAddresses saved to test_data/addresses.txt")


import numpy as np

# Read values from file (assuming file exists with one value per line)
try:
    with open("signal_values.txt", "r") as f:
        signal_values = [float(line.strip()) for line in f]
except FileNotFoundError:
    # Create sample data for demonstration
    signal_values = list(np.random.uniform(-0.5, 1.5, 1000))
    with open("signal_values.txt", "w") as f:
        for val in signal_values:
            f.write(f"{val}\n")

# Convert to numpy array
signal_array = np.array(signal_values)

# Calculate statistics
min_val = np.min(signal_array)
max_val = np.max(signal_array)
mean_val = np.mean(signal_array)
std_val = np.std(signal_array)
rms_val = np.sqrt(np.mean(np.square(signal_array)))

print(f"Minimum: {min_val:.4f} V")
print(f"Maximum: {max_val:.4f} V")
print(f"Mean: {mean_val:.4f} V")
print(f"Standard Deviation: {std_val:.4f} V")
print(f"RMS Value: {rms_val:.4f} V")

# Identify values outside 0V to 1.2V range
invalid_mask = (signal_array < 0) | (signal_array > 1.2)
invalid_samples = signal_array[invalid_mask]
invalid_indices = np.where(invalid_mask)[0]

print(f"\nInvalid samples found: {len(invalid_samples)}")

# Store invalid samples in separate file
with open("invalid_samples.txt", "w") as f:
    f.write("Index,Value\n")
    for idx, val in zip(invalid_indices, invalid_samples):
        f.write(f"{idx},{val:.4f}\n")

print("Invalid samples saved to invalid_samples.txt")


import re
from collections import Counter
from datetime import datetime

# Sample log data (in practice, read from file)
log_content = """
[2026-08-12 10:15:21] INFO: Test started
[2026-08-12 10:15:25] ERROR: Address mismatch at 0x1A2F
[2026-08-12 10:15:28] WARNING: Timeout
[2026-08-12 10:15:30] ERROR: Data mismatch at 0x2B10
"""

# Extract timestamps
timestamps = re.findall(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]', log_content)
print("Timestamps:", timestamps)

# Extract hexadecimal addresses
hex_addresses = re.findall(r'0x[0-9A-Fa-f]+', log_content)
print("Hex Addresses:", hex_addresses)

# Extract ERROR messages
error_messages = re.findall(r'ERROR: (.+)', log_content)
print("Error Messages:", error_messages)

# Count message types
message_types = re.findall(r'\] (INFO|WARNING|ERROR):', log_content)
type_counts = Counter(message_types)
print("\nMessage Type Counts:")
for msg_type, count in type_counts.items():
    print(f"  {msg_type}: {count}")

# Determine earliest and latest timestamps
datetime_objects = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S") for ts in timestamps]
earliest = min(datetime_objects)
latest = max(datetime_objects)
print(f"\nEarliest timestamp: {earliest}")
print(f"Latest timestamp: {latest}")

# Display summary
print("\n=== Verification Run Summary ===")
print(f"Total messages: {len(timestamps)}")
print(f"INFO messages: {type_counts.get('INFO', 0)}")
print(f"WARNING messages: {type_counts.get('WARNING', 0)}")
print(f"ERROR messages: {type_counts.get('ERROR', 0)}")
print(f"Total errors found: {len(error_messages)}")
print(f"Hex addresses referenced: {len(hex_addresses)}")


import itertools
import random
import copy

# Test parameters
clock_frequencies = ['100MHz', '200MHz', '400MHz']
voltage_levels = [0.9, 1.0, 1.1, 1.2]
operating_modes = ['normal', 'low_power']
temperature_conditions = ['25C', '85C', '125C']

# Generate all possible configurations using Cartesian product
all_configurations = list(itertools.product(
    clock_frequencies,
    voltage_levels,
    operating_modes,
    temperature_conditions
))

print(f"Total possible configurations: {len(all_configurations)}")

# Randomly select 10 configurations
selected_configurations = random.sample(all_configurations, 10)
print("\nSelected configurations for testing:")
for i, config in enumerate(selected_configurations, 1):
    print(f"  {i}. Frequency: {config[0]}, Voltage: {config[1]}V, "
          f"Mode: {config[2]}, Temperature: {config[3]}")

# Store selected configurations (in a file for persistence)
with open("test_configurations.txt", "w") as f:
    for config in selected_configurations:
        f.write(f"{config[0]},{config[1]},{config[2]},{config[3]}\n")

# Create an independent copy and modify it
config_copy = copy.deepcopy(selected_configurations)
# Modify the copy (e.g., change all voltages to 1.2V)
for i, config in enumerate(config_copy):
    config_copy[i] = (config[0], 1.2, config[2], config[3])

print("\nOriginal first 3 configurations:")
for config in selected_configurations[:3]:
    print(f"  {config}")

print("\nModified copy first 3 configurations:")
for config in config_copy[:3]:
    print(f"  {config}")

# Verify independence
print(f"\nCopy independent: {selected_configurations != config_copy}")


from collections import Counter
import random
import copy

signals = [
    "clk",
    "reset",
    "data_in",
    "data_out",
    "addr",
    "addr",
    "clk",
    "valid",
    "ready"
]

# Find frequency of every signal
signal_frequency = Counter(signals)
print("Signal Frequencies:")
for signal, freq in signal_frequency.items():
    print(f"  {signal}: {freq}")

# Identify duplicate signal names
duplicates = {signal: freq for signal, freq in signal_frequency.items() if freq > 1}
print("\nDuplicate Signals:")
for signal, freq in duplicates.items():
    print(f"  {signal}: appears {freq} times")

# Extract signals containing "data"
data_signals = [signal for signal in signals if "data" in signal]
print("\nSignals containing 'data':", data_signals)

# Randomly select three signals
selected_signals = random.sample(list(set(signals)), 3)
print("\nRandomly selected signals for testing:", selected_signals)

# Create independent copy and modify
signals_copy = copy.deepcopy(signals)
signals_copy.append("test_clk")  # Modify the copy
signals_copy[0] = "modified_clk"

print("\nOriginal signals:", signals)
print("Modified copy:", signals_copy)
print(f"Copy independent: {signals != signals_copy}")

# Calculate total number of unique signals
unique_signals = len(set(signals))
print(f"\nTotal unique signals: {unique_signals}")


import itertools
import random

frequencies = [10, 25, 50, 100, 200]  # MHz

# Calculate time periods (T = 1/f)
time_periods = []
for freq in frequencies:
    period_ns = 1000 / freq  # Convert MHz to ns (1/f in MHz = 1000/f in ns)
    time_periods.append((freq, period_ns))
    print(f"Frequency: {freq} MHz, Time Period: {period_ns:.2f} ns")

# Determine min and max frequency
min_freq = min(frequencies)
max_freq = max(frequencies)
print(f"\nMinimum frequency: {min_freq} MHz")
print(f"Maximum frequency: {max_freq} MHz")

# Generate all possible pairs
all_pairs = list(itertools.combinations(frequencies, 2))
print(f"\nAll possible frequency pairs ({len(all_pairs)} pairs):")
for pair in all_pairs:
    print(f"  {pair[0]} MHz vs {pair[1]} MHz")

# Randomly select three pairs
selected_pairs = random.sample(all_pairs, 3)
print("\nRandomly selected pairs for testing:")
for pair in selected_pairs:
    print(f"  {pair[0]} MHz vs {pair[1]} MHz")

# Store test data in a dictionary
test_data = {
    "frequencies": frequencies,
    "time_periods": dict(time_periods),
    "all_pairs": all_pairs,
    "selected_pairs": selected_pairs
}

print(f"\nTest data stored in dictionary with keys: {list(test_data.keys())}")


from collections import Counter
import random
import copy

results = [
    "PASS", "FAIL", "PASS", "PASS",
    "TIMEOUT", "FAIL", "PASS", "TIMEOUT",
    "PASS", "FAIL"
]

# Count occurrence of each result type
result_counts = Counter(results)
print("Result Counts:")
for result_type, count in result_counts.items():
    print(f"  {result_type}: {count}")

# Calculate percentage of tests that passed
total_tests = len(results)
pass_count = result_counts.get("PASS", 0)
pass_percentage = (pass_count / total_tests) * 100
print(f"\nPass percentage: {pass_percentage:.1f}%")

# Identify all unique result types
unique_results = list(result_counts.keys())
print(f"Unique result types: {unique_results}")

# Randomly select one result for further analysis
selected_result = random.choice(results)
print(f"Randomly selected result: {selected_result}")

# Create a copy and modify it
results_copy = copy.deepcopy(results)
results_copy.append("PASS")  # Add an extra PASS to the copy
results_copy[0] = "FAIL"     # Change first element in copy

print("\nOriginal results:", results)
print("Modified copy:", results_copy)
print(f"Copy independent: {results != results_copy}")

# Verify original is unchanged
print(f"Original length: {len(results)}")
print(f"Copy length: {len(results_copy)}")