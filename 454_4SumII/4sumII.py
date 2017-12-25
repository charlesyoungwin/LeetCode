import collections

class Solution:

    # not ac 最暴力的方法，显然不能通过
    def fourSumCountNotAc(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        length = len(A)
        if length == 0:
            return 0
        count = 0
        for i in range(0, length):
            for j in range(0, length):
                for k in range(0, length):
                    for m in range(0, length):
                        if A[i] + B[j] + C[k] + D[m] == 0:
                            count += 1
        return count

    def fourSumCount2(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)


if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    solu = Solution()
    print(solu.fourSumCount2(A, B, C, D))