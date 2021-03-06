#include<string.h>
#include<iostream>
#include<string>
using namespace std;

const int MAX_CHARS = 26;

/*Trie Node */
class TrieNode {
    public: 
        TrieNode():isWord(false) {
            memset(children, 0, sizeof(children));
        }
        TrieNode* & operator[](char idx) {
            int i = (idx - 'a') % MAX_CHARS;
            return children[i];
        }
        TridNode* & operator[](int idx) {
            int i = idx % MAX_CHARS;
            return children[i];
        }
        bool isWord;
    private:
        TrieNode* children[MAX_CHARS];
};

/*Trie Tree*/
class TrieTree {
    public: 
        TrieTree():root(new TrieNode()) {}
        ~TrieTree(){freeTree(root);}
        
        void put(string &s) {
            TrieNode* node = root;
            for (int i = 0; i < s.size(); i++) {
                if ((*node)[s[i]] == NULL) {
                    (*node)[s[i]] = new TrieNode();
                }
                node = (*node)[s[i]];
            }
            node->isWord = true;
        }
        bool search(string &s) {
            return get(s, this->root);
        }
    private:
        bool get(string &s, TrieNode* root, int idx=0) {
            TrieNode* node = root;
            for(int i = idx; i < s.size(); i++){
                if(s[i] != '.') {
                    node = (*node)[s[i]]
                    if(node == NULL) return false;
                } else {
                    for (int j = 0; j < MAX_CHARS; j++) {
                        TrieNode *p = (*node)[j];
                        if (p == NULL) {
                            continue;
                        }
                        
                        if(i < s.size() - 1) {
                            if(this->get(s, p, i + 1)) {
                                return true;
                            }
                            continue;
                        }
                        if(p->isWord) {
                            return true;
                        }
                    }
                    return false;
                }
            }
            return node->isWord;
            
        }
        
        void freeTree(TrieNode* root) {
            for(int i = 0; i < MAX_CHARS; i++) {
                if((*root)[i] != NULL) {
                    freeTree((*root)[i]);
                }
            }
            delete root;
        }
        
        TrieNode* root;
};

class WordDictionary {
    public:
      void addWord(string word) {
          tree.put(word);
      }
      
      bool search(string word) {
          return tree.search(word);
      }
      
    private: 
    TrieTree tree;
};