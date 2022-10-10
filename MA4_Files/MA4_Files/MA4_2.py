#!/usr/bin/env python3.9

from person import Person
from time import perf_counter as pc
from numba import njit
import matplotlib.pyplot as plt


def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)





def main():
	f = Person(5)
	n = [nn for nn in range(30,46)]
	pytimes = []
	numbatimes = []
	cpptimes = []
	for nn in n:
		print(nn)
		f.set(nn)
		print("Py")
		t0 = pc()
		fib_py(nn)
		t1 = pc()
		pytimes.append(t1-t0)
		print("Numba")
		t0 = pc()
		fib_numba(nn)
		t1 = pc()
		numbatimes.append(t1-t0)
		print("C++")
		t0 = pc()
		f.fib()
		t1 = pc()
		cpptimes.append(t1-t0)
	plt.plot(n, pytimes, 'r.')
	plt.plot(n, numbatimes, 'b.')
	plt.plot(n, cpptimes, 'g.')
	plt.savefig("FibCompTimes", facecolor='white', transparent=False) 
if __name__ == '__main__':
	main()
