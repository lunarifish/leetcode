// 2022-04-20 02:26:57
// Runtime 1150ms(6.9%)
// Memory 48mb(69.0%)

class CQueue {
    Stack<Integer> in;
    Stack<Integer> out;
    Integer ret;
    public CQueue() {
        this.in = new Stack();
        this.out = new Stack();
    }
    
    public void appendTail(int value) {
        this.in.push(value);
    }
    
    public int deleteHead() {
        if(this.in.empty())
            return -1;
        while(!this.in.empty())
            this.out.push(this.in.pop());
        this.ret = this.out.pop();
        while(!this.out.empty())
            this.in.push(this.out.pop());
        return ret.intValue();
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue obj = new CQueue();
 * obj.appendTail(value);
 * int param_2 = obj.deleteHead();
 */
