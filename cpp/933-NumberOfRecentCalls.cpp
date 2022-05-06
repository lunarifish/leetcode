// 2022-05-06 13:30:43
// Runtime 128ms(72.5%)
// Memory 55.8mb(96.3%)

class RecentCounter {
public:
    std::queue<int> qu;
    RecentCounter() {
        ;
    }
    
    int ping(int t) {
        qu.push(t);
        while (t - 3000 > qu.front())
            qu.pop();
        return qu.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
