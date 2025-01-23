class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split('/')
        queue = []

        for i in range(len(pathList)):
            if pathList[i] == '':
                continue
            if pathList[i] == '..' :
                if queue:
                    queue.pop()
                continue
            if pathList[i] == '.':
                continue
            queue.append(pathList[i])
        
        ans = '/'.join(queue)
        return '/' + ans
        