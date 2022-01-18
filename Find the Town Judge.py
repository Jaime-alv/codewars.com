# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
#
# If the town judge exists, then:
#
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
#
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
#
#
#
# Example 1:
#
# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:
#
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:
#
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
#
#
# Constraints:
#
# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n

def find_judge(N, trust):
    """
    :type N: int
    :type trust: List[List[int]]
    :rtype: int
    """
    graph = {i: [] for i in range(1, N + 1)}
    for t in trust:
        graph[t[0]].append(t[1])

    # check if the judge exists
    for k in graph:
        if len(graph[k]) == 0:
            # check if others trusts the judge
            judge = k
            for person in graph:
                if person != judge and judge not in graph[person]:
                    return -1
            return judge

    return -1
