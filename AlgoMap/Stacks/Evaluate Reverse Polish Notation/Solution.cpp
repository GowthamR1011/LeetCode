class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack;
        int value,val1,val2;
        for(auto ch:tokens){
            
            char c = ch[0];


            if(c == '+'){
                val1 = stack.back();
                stack.pop_back();
                val2 = stack.back();
                stack.pop_back();
                value = val1 + val2;
                stack.push_back(value);
            }
            else if(c == '-'){
                if(ch.size()>1){
                    stack.push_back(stoi(ch));
                }
                    
                else{
                    val1 = stack.back();
                    stack.pop_back();
                    val2 = stack.back();
                    stack.pop_back();
                    stack.push_back(val2 - val1);
                }

            }
            else if(c == '*'){
                val1 = stack.back();
                stack.pop_back();
                val2 = stack.back();
                stack.pop_back();
                value = val1* val2;
                stack.push_back(value);
            }
            else if(c == '/'){
                val1 = stack.back();
                stack.pop_back();
                val2 = stack.back();
                stack.pop_back();
                value = int(val2 / val1);
                stack.push_back(value);
            }


            else{
                    stack.push_back(stoi(ch));
            }
                
        }
        return stack[0];
    }
};