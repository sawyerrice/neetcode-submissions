class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        map<char, int> vals;
        for(char c: s){
            if(vals.find(c) == vals.end()){
                vals[c] = 1;
            }else{
                vals[c] += 1;
            }
        }

        for(char c: t){
            if( vals.find(c) == vals.end()){
                return false;
            }else {
                vals[c] -=1;
                if(vals[c] < 0){
                    return false;
                }
            }
        }
        return true;
    }
};
