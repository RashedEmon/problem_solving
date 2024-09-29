class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])

            for i in range(start, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()
        backtrack(1, path)
        return result

"""
For n=4 and k=3
Recursive Tree (image: https://github.com/RashedEmon/problem_solving/blob/master/images/combinations_recursive_tree.png)

Start
|
|-- Choose 1
|    |
|    |-- Choose 2
|    |    |
|    |    |-- Choose 3 → [1, 2, 3]
|    |    |
|    |    \-- Choose 4 → [1, 2, 4]
|    |
|    \-- Choose 3
|         |
|         \-- Choose 4 → [1, 3, 4]
|
|-- Choose 2
|    |
|    |-- Choose 3
|    |    |
|    |    \-- Choose 4 → [2, 3, 4]
|
|-- Choose 3
|    |
|    \-- Choose 4 → No further valid combinations (size < 3)
|
\-- Choose 4 → No further valid combinations (size < 3)
"""
