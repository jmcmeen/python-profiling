# final_showcase_fixed_v2.py
import time
import math
import numpy as np

# ================================================
CPU_ITERATIONS = 34552942
STRING_ITERATIONS = 46658100
LOOP_ITERATIONS = 171796964
# ================================================

# --- Fix 1: Vectorization for the CPU-Bound Task ---
def cpu_heavy_task_fixed(iterations):
    """
    Fixed by using NumPy to perform the complex math on an entire array
    at once, in highly optimized C code instead of a Python loop.
    """
    print("  -> Running CPU-bound task...")
    # Create an array of numbers from 0 to iterations-1
    i = np.arange(iterations, dtype=np.float64)
    # The same calculation, but vectorized, is orders of magnitude faster
    result_array = np.sin(i) * np.cos(i) + np.sqrt(i)
    return np.sum(result_array)

# --- Fix 2: Efficient String Joining ---
def memory_heavy_string_task_fixed(iterations):
    """
    Fixed by using a list comprehension and a single, efficient ''.join().
    This avoids creating millions of intermediate strings.
    """
    print("  -> Running Memory/String-bound task...")
    chunk = "report_item_abcdefg_123456789_"
    # A list comprehension is fast and memory-efficient
    parts = [f"|{chunk}{i}" for i in range(iterations)]
    return "".join(parts)

# --- Fix 3: Eliminating the "Thousand Cuts" Loop ---
def iteration_heavy_task_fixed(iterations):
    """
    Fixed by recognizing the task can be a no-op or done in bulk.
    In a real-world scenario, you would find a way to batch the work.
    Here, we demonstrate the fix by simply removing the pointless loop.
    The goal is to show the cost of the loop itself.
    """
    print("  -> Running Iteration-bound task...")
    # The fix is to find a bulk operation or eliminate the loop.
    # Since the original function did nothing, the fix is to do nothing faster.
    return "OK"

# --- Main Orchestrator ---
def run_all_systems():
    """
    The main orchestrator now calls the FAST versions of each task.
    """
    print("--- Starting FINAL FAST Balanced Showcase ---")

    cpu_result = cpu_heavy_task_fixed(iterations=CPU_ITERATIONS)
    string_result = memory_heavy_string_task_fixed(iterations=STRING_ITERATIONS)
    iteration_result = iteration_heavy_task_fixed(iterations=LOOP_ITERATIONS)

    print("--- FINAL FAST Balanced Showcase Finished ---")


if __name__ == "__main__":
    run_all_systems()
