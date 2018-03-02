class Solution:

    #solution 1
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0

    # solution 2
    def hIndexV2(self, citations):
        if not citations:
            return 0
        citations.sort()
        length = len(citations)
        for i in range(length):
            if length <= citations[i]:
                return length
            else:
                length -= 1
        return length

if __name__ == '__main__':
    citations = [4, 0, 6, 2, 5]
    print(Solution().hIndex(citations))
    print(Solution().hIndexV2(citations))
    