#!/usr/bin/env python
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self. leaves = {}
        
class WordDictoinary(object):
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        curr = self.root
        for c in word:
            if not c in curr.leaves:
                curr.leaves[c] = TrieNode()
                
        curr.is_word = True
    
    def search(self, word):
       return self.searchHelper(word, 0, self.root)
    
    def searchHelper(self, word, start, curr):
        if start == len(word):
            return curr.is_word
        
        if word[start] in curr.leaves:
            return self.searchHelper(word, start + 1, curr.leaves[word[start]])
            
        elif word[start] == '.':
            for c in curr.leaves:
                if self.searchHelper(word, start + 1, curr.leaves[c]):
                    return True
                    
        return False
        