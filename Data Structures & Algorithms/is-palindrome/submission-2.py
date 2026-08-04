class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palindrome: string that reads the same backward and forward
        # case insensitive (considers uppercase and lowercase as equivalent) and nly considers non-alphanumeric characters

        # use a 2 pointer approach, working backwards to the middle and skipping characters as described above
        l = 0
        r = len(s) - 1

        while l < r:
            # print("l, r: %s, %s", s[l], s[r])
            # skip non-alphanumerics
            while l < r and not self.isAlphanumeric(s[l]):
                l += 1
            while l < r and not self.isAlphanumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l+= 1
            r -= 1
            
        return True

    def isAlphanumeric(self, c):
        return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

