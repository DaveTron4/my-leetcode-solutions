class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)

        bucket = [0] * (n + 1)

        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1

        total_papers = 0
        for i in range(n, -1, -1):
            total_papers += bucket[i]

            if total_papers >= i:
                return i

        return 0

        # citations.sort()
        
        # n = len(citations)
        
        # for i in range(n):
        #     count = n - i
        
        #     if citations[i] >= count:
        #         return count

        # return 0

