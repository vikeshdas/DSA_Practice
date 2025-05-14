
def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    dic={}
    def word_break(word,st):
        if word in dic:
            return dic[word]
        if len(word)==0 or word in st:
            dic[word]=True
            return True
        
        for i in range(1,len(word)):
            if word[:i] in st:
                if word_break(word[i:],st)==True:
                    dic[word]=True
                    return True
        if len(word)>0:
            dic[word]=False
            return False
            
        dic[word]=True
        return True
    return word_break(s,set(wordDict))
        