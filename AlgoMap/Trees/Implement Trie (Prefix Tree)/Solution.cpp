class TrieNode{
    public:
        TrieNode* child[26] = {NULL};
        bool isWord;
    
        TrieNode(){
            isWord = false;
        }
    };
    
    class Trie {
    public:
        TrieNode* start;
        Trie() {
            start = new TrieNode();
        }
        
        void insert(string word) {
            TrieNode* d = start;
    
            for(int j = 0;j<word.size();j++){
                int i = word[j]-'a';
                if(d->child[i] == NULL)
                    d->child[i] = new TrieNode();
                d = d->child[i];
            }
            d->isWord = true;
        }
        
        bool search(string word) {
            TrieNode *d = start;
    
            for(int j = 0;j<word.size();j++){
                int i = word[j]-'a';
                if(d->child[i] == nullptr)
                    return false;
                d = d->child[i];
            }
            return d->isWord;
        }
        
        bool startsWith(string prefix) {
            TrieNode* d = start;
    
            for(int j = 0;j<prefix.size();j++){
                int i = prefix[j]-'a';
                if(d->child[i] == nullptr)
                    return false;
                d = d->child[i];
            }
            return true;
        }
    };
    
    /**
     * Your Trie object will be instantiated and called as such:
     * Trie* obj = new Trie();
     * obj->insert(word);
     * bool param_2 = obj->search(word);
     * bool param_3 = obj->startsWith(prefix);
     */