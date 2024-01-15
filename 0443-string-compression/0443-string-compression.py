class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return len(chars)

        left, right = 0, 0
        num = 0
        while right < len(chars):
            if (chars[left] != chars[right]):
                ## insert the num right next to the alphabet
                if num == 1:
                    left = right
                else:
                    num_str = str(num)
                    chars[left + 1] = num_str[0]
                    if len(num_str) > 1:
                        for i in range(1, len(num_str)):
                            chars.insert(left + 1 + i, num_str[i])
                        ## erase other alphabet in between (left+ lenstr +1 < idx < right)
                        del chars[left + len(num_str) + 1:right+len(num_str)-1]
                        right = left = left + len(num_str) + 1
                    else:
                        if num > 2:
                            del chars[left + 2:right]
                            right = left = left + 2
                        else:
                            left = right
                num = 0
            else:
                num += 1
                right += 1

        # 마지막 후처리
        if right == len(chars):
            num_str = str(num)
            if num > 1:
                chars[left + 1] = num_str[0]
                if len(num_str) > 1:
                    for i in range(1, len(num_str)):
                        chars.insert(left + 1 + i, num_str[i])
                    del chars[left + len(num_str) + 1:right+len(num_str)-1]
                else:
                    if num > 2:
                        del chars[left + 2:right]
        

        return len(chars)
