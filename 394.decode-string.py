class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for char in s:
            if char == "]":
                char_in_bracket = []
                while stack and stack[-1] != "[":
                    char_in_bracket.append(stack.pop())
                stack.pop() if stack else None
                number_to_multiply = ""

                while stack and str.isnumeric(stack[-1]):
                    number_to_multiply = stack.pop() + number_to_multiply

                if number_to_multiply:
                    stack.extend(char_in_bracket[::-1] * int(number_to_multiply))
            
            if char != "]":
                stack.append(char)

        return "".join(stack)

