class MinStack {
public:
    vector<vector<int>> stack;
    MinStack() {  
    }
    
    void push(int val) {
        if(stack.empty())
            stack.push_back({val,val});
        else{
            
            stack.push_back({val,min(val,stack.back()[1])});
        }
    }
    
    void pop() {
        stack.pop_back();
    }
    
    int top() {
        return    stack.back()[0];
    }
    
    int getMin() {
        return stack.back()[1];
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */