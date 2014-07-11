import cProfile, pstats, io
import unittest
from os import getcwd
import Constants
import re

if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()

    # run all unit tests
    suites = unittest.TestLoader().discover(start_dir=getcwd())
    unittest.runner.TextTestRunner().run(suites)

    profiler.disable()
    s = io.StringIO()
    sortby = 'tottime'
    ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
    ps.print_stats()
    
    count = 0
    max_count = 10
    for line in s.getvalue().split('\n'):
        m = re.search(r"ncalls.*tottime.*percall", line)
        if m:
            print(line)
            continue
        m = re.search(Constants.PROJECT_ROOT, line)
        if not m:
            # we don't want these
            continue
        else:
            if count >= max_count:
                break
            print(line)
            count += 1
