# profile_fixed.py
# Profile the fixed version of the script using cProfile
import cProfile, pstats, io
from final_showcase_fixed_v2 import run_all_systems

pr = cProfile.Profile()
pr.enable()

# Run the function you want to profile
run_all_systems()

pr.disable()

# Dump stats to a string and print the top 10 by cumulative time
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
ps.print_stats(10)
print(s.getvalue())
