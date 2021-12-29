# xrSolver

範例
====

範例取自 https://www.youtube.com/watch?v=WJEZh7GWHnw ，三個例子分別為 example1.py, example2.py, example3.py，用於示範如何建構問題及求解。

以 example1.py 為例，假設使用 Cassowary 為求解器：
```console
$ PYTHONPATH="solvers/cassowary/src/xrsolver/solver/cassowary/" python3 example/example1.py
```

其中 cassowary 的位置，可以換成以下的求解器：
1. cassowary
2. cvxpy
3. deap
4. dreal
5. gekko
6. pulp
7. z3

```console
$ example/solver/byCassowary.py
```

求解器範例
===
求解器的範例則位於 [solver/](solver/) 下， by{solver name}.py 分別對應相關的求解器。

