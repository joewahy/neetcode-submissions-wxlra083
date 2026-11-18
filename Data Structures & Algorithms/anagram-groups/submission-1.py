class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## count the characters in each word

        ## compare to see if counts are the same

        ## return the words that are valid

        result = []

        comp = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in comp:
                comp[sorted_word] = []
            
            comp[sorted_word].append(word)
        
        
        return list(comp.values())
        