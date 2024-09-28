class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # sort pair by attack in ascending order and defense descending order.
        # [[1,1], [2,2], [1,2], [2,1]] convert to [[1,2], [1,1], [2,2], [2,1]]
        properties.sort(key=lambda item: (item[0], -item[1]))
        print(properties)
        defense = [d for a,d in properties]
        stack = []
        result = 0
        for i in range(len(defense)):
            while stack and defense[stack[-1]] < defense[i]:
                idx = stack.pop()
                result+=1
            stack.append(i)

        return result
