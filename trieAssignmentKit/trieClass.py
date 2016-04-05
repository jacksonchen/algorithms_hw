#LastName: Chen
#FirstName: Jackson
#Email: jackson@chenjackson.com
#Comments:

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields

    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):
        assert(len(w) > 0)
        tmpNode = self
        for c in w:
            if c in tmpNode.next:
                tmpNode = tmpNode.next[c]
            else:
                newNode = MyTrieNode(False)
                tmpNode.next[c] = newNode
                tmpNode = newNode
        tmpNode.count += 1
        tmpNode.isWordEnd = True

        return

    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.
        if len(w) == 0:
            return 0
        else:
            tmpNode = self
            for c in w:
                if c in tmpNode.next:
                    tmpNode = tmpNode.next[c]
                else:
                    return 0
            return tmpNode.count

    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        if len(w) == 0:
            return []
        else:
            tmpNode = self
            for c in w:
                if c in tmpNode.next:
                    tmpNode = tmpNode.next[c]
                else:
                    return []
            res = []
            string = w
            return self.autoCompleteRec(tmpNode, w, [])

    def autoCompleteRec(self, node, string, res):
        if node.isWordEnd:
            res.append((string, node.count))
        if len(node.next) > 0:
            for c in node.next:
                res = self.autoCompleteRec(node.next[c], string + c, res)
        return res


if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)

    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
