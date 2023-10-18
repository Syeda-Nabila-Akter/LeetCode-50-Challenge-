# Problem link: https://leetcode.com/problems/find-center-of-star-graph/
# 54 / 60 testcases passed

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        flatten_list = [] 
        output = None
        edges_lenth = len(edges)
  
        for sublist in edges: 
            for val in sublist: 
                flatten_list.append(val) 
 
        for a in flatten_list:
            n = flatten_list.count(a)
            if n >= edges_lenth:
                output = a
        return output
        

