# [Project Euler Problem 5](https://projecteuler.net/problem=5)

## 问题

**Smallest Multiple**

![题目截图](../images/problem_5.png)

## 答案

`232792560`

## 解法

直接求这些整数的最小公倍数即可。
算法部分的 Python 代码如下，完整的代码见 [solution_5.py](../solutions/solution_5.py)，这里直接调用 `math.lcm()` 求最小公倍数。

```python
def solve_p5(n: int) -> int:
    return math.lcm(*list(range(1, n + 1)))
```
