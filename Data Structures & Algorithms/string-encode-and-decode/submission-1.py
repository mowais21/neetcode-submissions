class Solution:
    # n individual strings
    # each string s can have varying length
    # need to figure out how to separate each indivudual string
    # the string has ASCII characters only

    # [0-9]*<delimiter>.
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for cur_str in strs:
            len_curr = len(cur_str)

            # len + delimiter + str
            res += str(len_curr)
            res += "_"
            res += cur_str

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        if len(s) != 0:
            # for each word, do the following:
            # 1. fetch the multi-digit length till the delimiter
            # 2. fetch the current word using the length and the delimiter
            cur_start = 0
            
            while cur_start < len(s):
                # find the delimiter, use its index to fetch length of the substring
                delimiter = s.find("_", cur_start)
                cur_length = int(s[cur_start: delimiter])
                # fetch the current substring
                cur_str = s[delimiter + 1: delimiter + cur_length + 1]
                res.append(cur_str)
                
                cur_start = delimiter + cur_length + 1

        return res
