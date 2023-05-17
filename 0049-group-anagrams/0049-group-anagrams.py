class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict= {}
        for word in strs :
            a = sorted(word)
            srt = ''.join(a)
            if srt in word_dict.keys() :
                word_dict[srt].append(word)
            else :
                word_dict[srt] = []
                word_dict[srt].append(word)
        return list(word_dict.values())