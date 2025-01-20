class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ann_groups = dict()
        for ann in strs :
            key = ''.join(sorted(ann))
            if key in ann_groups :
                ann_groups[key].append(ann)
            else :
                ann_groups[key] = [ann]
        return list(ann_groups.values())