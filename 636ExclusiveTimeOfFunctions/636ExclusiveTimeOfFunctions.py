class Solution:

    #wrong anwser 想了半天都没有做出来，搞得有点乱
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        import re
        pattern = re.compile(r'(\d+).*?(\d+)')
        tmp = []
        res = []
        for log in logs:
            tmp.append(pattern.match(log).groups())
        tmp = list( map(lambda x: (int(x[0]), int(x[1])), tmp) )
        for i in range(n):
            d = []
            for j in range(len(tmp)):
                if tmp[j][0] == i:
                    d.append((j, tmp[j][1]))

            if  d[0][0] != d[1][0] - 1:
                durationS = tmp[d[0][0]+1][1] - d[0][1]
                durationE = d[1][1] - tmp[d[1][0] - 1][1]
                duration = durationS + durationE
            else:
                duration = d[1][1] - d[0][1] + 1
            res.append(duration)
        return res

    def exclusiveTimeV2(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn, typ, time = log.split(":")
            fn, time = int(fn), int(time)

            if typ == 'start':
                if stack: 
                    ans[stack[-1]] += time - prev_time
                stack.append(fn)
                prev_time = time
            else: 
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return ans

                


if __name__ == '__main__':
    n = 2
    logs = \
        ["0:start:0", 
         "1:start:2", 
         "1:end:5",   
         "0:end:6"]
    print(Solution().exclusiveTimeV2(n, logs))