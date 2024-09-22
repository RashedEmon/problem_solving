class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "o", "i", "u"])
        res = 0
        vowel_count = 0
        if len(s) < k:
            return vowel_count

        window_queue = []
        for i in range(k):
            if s[i] in vowels:
                vowel_count+=1
                res = max(vowel_count, res)
            window_queue.append(s[i])

        if len(s) >= k:
            for i in range(k, len(s)):
                char = window_queue.pop(0)
                if char in vowels:
                    vowel_count-=1

                window_queue.append(s[i])
                if s[i] in vowels:
                    vowel_count+=1
                    res = max(vowel_count, res)

        return res
