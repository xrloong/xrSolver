all:
	python3 -m build
	python3 -m build solvers/cassowary
	python3 -m build solvers/cvxpy
	python3 -m build solvers/deap
	python3 -m build solvers/dreal
	python3 -m build solvers/gekko
	python3 -m build solvers/pulp
	python3 -m build solvers/z3

clean:
	rm -rf dist solvers/*/dist

