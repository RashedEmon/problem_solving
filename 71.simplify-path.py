class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.strip("/")
        directory_list = path.split("/")
        
        stack = []
        canonical_path = []
        for directory in directory_list:
            if directory != '':
                stack.append(directory)

        for directory in stack:
            if directory == ".":
                continue

            if directory == ".." and canonical_path:
                canonical_path.pop()
                continue
                
            if directory not in (".", ".."):
                canonical_path.append(directory)

        if canonical_path:
            return "/"+"/".join(canonical_path)
        
        return "/"
