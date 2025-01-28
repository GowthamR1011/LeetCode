class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;

        for(auto c:s){
            if(c == '(' || c == '{' || c == '[')
                stack.push_back(c);
            
            else if(stack.size() > 0 ){
                if(c == ')' && stack.back() == '(')
                    stack.pop_back();
                
                else if(c == '}' && stack.back() == '{')
                    stack.pop_back();
                
                else if(c==']' && stack.back() == '[')
                    stack.pop_back();
                
                else 
                    return false;
            }
            else 
                return false;
        }
        if(stack.size()>0)
            return false;
        
        return true;
    }
};