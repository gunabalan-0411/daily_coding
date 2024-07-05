class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Bottom-up Dynamic Programming style
        cache = [ 
                [float('inf') for _ in range(len(word2)+1)] 
                for _ in range(len(word1)+1)
            ]
        
        # Fill base case: empty word2 to word1 and vice versa
        for j in range(len(word2)+1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1)+1):
            cache[i][len(word2)] = len(word1) - i

        # Bottom - up approach
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    # Capturing the diagonal value
                    cache[i][j] = cache[i+1][j+1] 
                else:
                    # getting the min of all operations
                    cache[i][j] = 1 + min(
                        cache[i+1][j], # insert
                        cache[i][j+1], # delete
                        cache[i+1][j+1]# replace
                    )

        return cache[0][0]
        