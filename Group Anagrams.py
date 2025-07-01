# https://leetcode.com/problems/group-anagrams/

class Solution:
    def calculateString(self, temp: str):
        zeros = ["0"] * 26  # Start with string list
        counts = [0] * 26   # Track actual counts as numbers

        for i in temp:
            idx = ord(i.lower()) - 97  # Assumes only letters a-z
            counts[idx] += 1

            if counts[idx] <= 9:
                zeros[idx] = str(counts[idx])
            else:
                zeros[idx] = "x" + str(counts[idx] - 10)

            print(f"char: {i}, idx: {idx}, value: {zeros[idx]}")  # Debug

        return ''.join(zeros)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_Hashmap={}
        for i in strs:
            # calculating string
            ans = self.calculateString(i)
            print(ans)
            if(ans in my_Hashmap):
                my_Hashmap[ans].append(i)
            else:
                my_Hashmap[ans]=[i]
        
        my_list=[]
        for value in my_Hashmap.values():
            my_list.append(value)
        
        return my_list