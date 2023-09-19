class TrieNode:
    def __init__(self):
        self.is_end = False
        self.next = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for char in word:
            _id = ord(char) - ord('a')
            if curr.next[_id] is None:
                curr.next[_id] = TrieNode()
            curr = curr.next[_id]
        curr.is_end = True

    def search(self, word: str):
        curr = self.root
        for char in word:
            _id = ord(char) - ord('a')
            if curr.next[_id] is None:
                return False
            curr = curr.next[_id]
        return curr.is_end


if __name__ == "__main__":
    word_list = ["java", "javascript", "python", "py", "script", "job", "base"]

    trie = Trie()
    for word in word_list:
        trie.insert(word)

    search_list = ["java", "process", "python", "linux"]
    for search in search_list:
        if trie.search(search):
            print(search)
            
