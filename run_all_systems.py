# run_all_systems.py
import time
import math

# ================================================
CPU_ITERATIONS = 34552942
STRING_ITERATIONS = 46658100
LOOP_ITERATIONS = 171796964
# ================================================

# --- Task 1: A Calibrated CPU-Bound Bottleneck ---
def cpu_heavy_task(iterations):
    print("  -> Running CPU-bound task...")
    result = 0
    for i in range(iterations):
        result += math.sin(i) * math.cos(i) + math.sqrt(i)
    return result

# --- Task 2: A Calibrated Memory/String Bottleneck ---
def memory_heavy_string_task(iterations):
    print("  -> Running Memory/String-bound task...")
    report = ""
    chunk = "report_item_abcdefg_123456789_"
    for i in range(iterations):
        report += f"|{chunk}{i}"
    return report

# --- Task 3: A Calibrated "Thousand Cuts" Iteration Bottleneck ---
def simulate_tiny_op(n):
    pass

def iteration_heavy_task(iterations):
    print("  -> Running Iteration-bound task...")
    for i in range(iterations):
        simulate_tiny_op(i)
    return "OK"

# --- Main Orchestrator ---
def run_all_systems():
    print("--- Starting FINAL SLOW Balanced Showcase ---")

    cpu_result = cpu_heavy_task(iterations=CPU_ITERATIONS)
    string_result = memory_heavy_string_task(iterations=STRING_ITERATIONS)
    iteration_result = iteration_heavy_task(iterations=LOOP_ITERATIONS)

    print("--- FINAL SLOW Balanced Showcase Finished ---")


if __name__ == "__main__":
    run_all_systems()
