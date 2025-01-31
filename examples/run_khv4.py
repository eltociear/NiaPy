# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys

sys.path.append('../')
# End of fix

from niapy.algorithms.basic import KrillHerdV4
from niapy.task import StoppingTask
from niapy.problems import Sphere

# we will run Fireworks Algorithm for 5 independent runs
for i in range(5):
    task = StoppingTask(problem=Sphere(dimension=10), max_iters=50)
    algo = KrillHerdV4(population_size=70)
    best = algo.run(task)
    print('%s -> %s' % (best[0], best[1]))

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
