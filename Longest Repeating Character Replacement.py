class Solution:
    def __init__(self):
        self.distinct = {}

    def characterReplacement(self, s: str, k: int) -> int:
        max_window = 1
        window_size = 1
        
        first = 0
        last = 0
        self.distinct[s[last]]=1
        while True:
            current_window = int(abs(last-first)+1)
            if current_window - self.most_frequency() <= k:
                last += 1
                if last >= len(s):
                    max_window = int(abs(last-first)) if int(abs(last-first)+1) > max_window else max_window
                    break
                self.insert_to_dict(s[last])
                
                if max_window < current_window:
                    max_window = current_window
            else:
                self.delete_to_dict(s[first])
                first += 1
        
        return max_window


    def insert_to_dict(self, char):
        if char in self.distinct:
            self.distinct[char] = self.distinct[char] + 1
        else:
            self.distinct[char] = 1
    
    def delete_to_dict(self, char):
        if  char in self.distinct:
            count = self.distinct.get(char)
            if count > 1:
                self.distinct[char] = self.distinct[char] - 1
            else:
                del self.distinct[char]


    def most_frequency(self):
        max_freq = 0
        for char, freq in self.distinct.items():
            if freq > max_freq:
                max_freq = freq
        return max_freq


        
