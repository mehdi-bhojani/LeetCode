#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # method 1 by hashmap/dic

        # freq_map={}
        # # create frequency map
        # for i in s1:
        #     freq_map[i]= 1 if i not in freq_map else freq_map[i]+1
        # print(freq_map)
        # count=0
        
        # freq_map_copy = freq_map.copy()
        # left=0
        # right=0
        # while(left < len(s2)):
        #     if s2[left] in freq_map_copy:
        #         freq_map_copy[s2[left]]-=1
        #         if freq_map_copy[s2[left]]==0:
        #             print("popping: ",s2[left])
        #             freq_map_copy.pop(s2[left])
        #         count += 1
        #     else:
        #         freq_map_copy = freq_map.copy()
        #         left = right
        #         right += 1
        #         print(left)

        #         count=0
            
        #     if len(freq_map_copy) == 0:
        #         return True

        #     left += 1
            
        # if len(freq_map_copy) == 0:
        #     return True
        
        # return False

        # method 2 by array
        freq_map1 = [0]*26
        freq_map2 = [0]*26

        if len(s1) > len(s2):
            return False

        # calculate frequnecy map for s1
        for i in s1:
            freq_map1[ord(i)-ord('a')] += 1
        print("freq_map1",freq_map1)

        # calculate frequency map 2 with window size
        for i in range(len(s1)-1):
            freq_map2[ord(s2[i])-ord('a')] += 1
        
        print("freq_map2",freq_map2)

        right = len(s1) - 1
        left = 0
        
        while(right < len(s2)):
            freq_map2[ord(s2[right])-ord('a')] +=1
            if(freq_map1==freq_map2):
                return True
            freq_map2[ord(s2[left])-ord('a')] -=1
            right += 1
            left += 1

        return False



    
# @lc code=end

