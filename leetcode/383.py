class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        checks = 0 
        for i in ransomNote:
            if i in magazine:
                checks += 1
                magazine = magazine.replace(i, '', 1)
        
        if checks == len(ransomNote):
            return True
        else:
            return False
        
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    checks = 0 
    for i in ransomNote:
        if i in magazine:
            checks += 1
            magazine = magazine.replace(i, '', 1)
        elif i not in magazine:
            return False

    return True
        
canConstruct("aa", "aab")