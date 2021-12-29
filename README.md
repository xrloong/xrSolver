# xrSolver
約束滿足問題及求解器的包裝（A Wrapper for Constraint Satisfication Problem and its solver）

這個計劃的目的，是為約束滿足問題的求解器的各個函式庫，提供一個通用的包裝介面。此計劃初始實作，原本是在 [Yong8](https://github.com/xrloong/Yong8) 中，現將求解器的部分提出。

The goal of this project to to provide a common wrapper APIs for many solvers to Constraint Satisfaction Problems. The initial implementation is in [Yong8](https://github.com/xrloong/Yong8). To extract the foundation of solvers as this project.

編譯
====
主程式的部分：
```console
$ python3 -m build
```

求解器的部分：
```console
$ python3 -m build solvers/cassowary
$ python3 -m build solvers/cvxpy
$ python3 -m build solvers/deap
$ python3 -m build solvers/dreal
$ python3 -m build solvers/gekko
$ python3 -m build solvers/pulp
$ python3 -m build solvers/z3
```


安裝
====

* 第三方函式庫（Third-party libraries）
```console
$ pip3 install xrSolver-{version}-py3-none-any.whl
$ pip3 install xrSolver_{solver name}-{version}-py3-none-any.whl
```

|   solver  | PIP package |
| :-------: | :---------: |
| cassowary |  cassowary  |
|   cvxpy   |    cvxpy    |
|    deap   |     deap    |
|   dreal   |    dreal    |
|   gekko   |    gekko    |
|    pulp   |    PuLP     |
|     z3    |  z3-solver  |

範例
===

相關範例，請參考[相關說明](example/README.md) 。

