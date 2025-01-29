class Solution {
public: vector<int>dp;
int noofways(int i , string s){
    if(i>=s.size()) return 1;
    else if(s[i] == '0') return 0; //if the input no start with  0  just return  0 
    else if(i==s.size()-1) return 1;
else if(dp[i] != -1) return dp[i];//if it is already seen before dont do antthing to it just return the previous ans
    else if(s[i]=='1' || (s[i]=='2' && (s[i+1]>=48 && s[i+1]<=54)))
    return dp[i]= noofways(i+1,s) + noofways(i+2,s);
    else return dp[i] = noofways(i+1 ,s);
}


    int numDecodings(string s) {
        dp.resize(s.size());// resize the dp size by which is the size of the given string 
        dp.assign(s.size() , -1); //initially all the value is -1
        return noofways(0 , s);
    }
};