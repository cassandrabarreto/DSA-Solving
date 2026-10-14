"""
    There is a group of n people labeled from 0 to n - 1 where each person
    has a different amount of money and a different level of quietness.

    You are given an array `richer` where richer[i] = [a_i, b_i] indicates
    that a_i has more money than b_i, and an integer array `quiet` where
    quiet[i] is the quietness of the ith person. All the given data in
    richer are logically correct (i.e., the data will not lead you to a
    situation where x is richer than y and y is richer than x at the
    same time).

    Return an integer array `answer` where answer[x] = y if y is the
    least quiet person (that is, the person y with the smallest value
    of quiet[y]) among all people who definitely have equal to or more
    money than person x.

    Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
    Output: [5,5,2,5,4,5,6,7]

"""
from typing import List

class Solution:

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_graph = self.convert_to_graph(richer)  

        rich_nums = {}
        # Build parent relationship with children
        for node in richer_graph:
            rich_nums[node] = 0 

        for node in richer_graph[node]:
            pass


    def convert_to_graph(edges):
        graph = dict()
        for edge in edges:
            a = edge[0]
            b = edge[1]
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
        return graph