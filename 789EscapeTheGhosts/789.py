class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        dist = target[0] + target[1]
        gDist = []
        for ghost in ghosts:
            d = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            gDist.append(d)
        gDist.sort()
        for item in gDist:
            if item > dist:
                break
            elif item == dist:
                return False
            else:
                val = dist - item
                if val % 4 == 0:
                    return False
                else:
                    return True
        return True

if __name__ == '__main__':
    ghosts = [[1,9],[2,-5],[3,8],[9,8],[-1,3]]
    target = [8, -10]
    print(Solution().escapeGhosts(ghosts, target))