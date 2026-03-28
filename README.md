# Python Profiling Examples

Code and examples from the article **"Think Your Python Code Is Slow? Stop Guessing and Start Measuring"** by **Thomas Reid**, published on [Towards Data Science](https://towardsdatascience.com/think-your-python-code-is-slow-stop-guessing-and-start-measuring/) (Dec 26, 2025).

## The Problem

When Python code is slow, developers often guess at the cause and start optimising the wrong things. As Donald Knuth said, *"Premature optimisation is the root of all evil."* Instead of guessing, you should **measure** where the bottlenecks actually are using profiling tools.

This project demonstrates a methodical workflow using two tools:

- **cProfile** — Python's built-in deterministic profiler that collects detailed statistics on every function call.
- **snakeviz** — A visualisation tool that turns cProfile's output into an interactive "icicle" chart, making bottlenecks immediately obvious.

## The Example Script

`run_all_systems.py` is a deliberately slow script with three distinct bottlenecks:

1. **CPU-bound task** (`cpu_heavy_task`) — A `for` loop performing millions of `math.sin/cos/sqrt` calculations one at a time. (~12.9s)
2. **Iteration-bound task** (`iteration_heavy_task`) — Calls a tiny no-op function 171 million times, demonstrating "death by a thousand cuts" from Python function call overhead. (~14.3s)
3. **Memory/String-bound task** (`memory_heavy_string_task`) — Builds a huge string via repeated `+=` concatenation, which creates a new string object each time. (~3.8s)

Total runtime: **~30 seconds**.

## The Fixes

`final_showcase_fixed_v2.py` applies targeted fixes identified through profiling:

1. **CPU-bound** — Replaced the Python loop with **NumPy vectorisation** (`np.sin`, `np.cos`, `np.sqrt` on arrays). Drops from ~12.9s to milliseconds.
2. **Iteration-bound** — Eliminated the unnecessary loop entirely. In real code, this means finding a bulk/batch operation. Drops from ~14.3s to near-zero.
3. **Memory/String-bound** — Replaced `+=` concatenation with a **list comprehension + `"".join()`**. Drops from ~3.8s to ~4.3s (now the dominant cost, but much more efficient).

Total runtime after fixes: **~6 seconds** (5x speedup).

## Setup

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

Install required packages:

```bash
pip install -r requirements.txt
```

> **Note:** `cProfile` and `pstats` are part of the Python standard library — no installation needed.

## Running the Code

### 1. Run the slow script directly

```bash
python run_all_systems.py
```

### 2. Profile the slow script with cProfile

```bash
python profile_slow.py
```

This prints a table of the top 10 functions sorted by cumulative time.

### 3. Run the fixed script directly

```bash
python final_showcase_fixed_v2.py
```

### 4. Profile the fixed script with cProfile

```bash
python profile_fixed.py
```

### 5. Visualise with snakeviz (Jupyter Notebook)

Open the included notebook:

```bash
jupyter notebook profiling_snakeviz.ipynb
```

Run the cells to produce an interactive icicle chart showing the call hierarchy and time spent in each function.

### 6. Visualise with snakeviz (command line)

You can also profile from the command line and open snakeviz in a browser:

```bash
python -m cProfile -o output.prof run_all_systems.py
snakeviz output.prof
```

## Attribution

All code and examples are from the article by **Thomas Reid**. See the original at:
https://towardsdatascience.com/think-your-python-code-is-slow-stop-guessing-and-start-measuring/
