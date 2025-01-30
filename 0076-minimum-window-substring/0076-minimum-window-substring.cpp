class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char,int>mpp;
        for(auto & ch: t){
            mpp[ch]++;
        }

        int cnt = 0, minlen = INT_MAX, l = 0, r = 0, sIndex = -1, n = s.length(),m = t.size();

        while(r<n){
            if(mpp[s[r]]>0){
                cnt++;
            }
            mpp[s[r]]--;
            while(cnt==m){
                if(r-l+1<minlen){
                    minlen = r-l+1;
                    sIndex =l;
                }
                mpp[s[l]]++;
                if(mpp[s[l]]>0)cnt--;
                l++;
            }
            r++;
        }
    return sIndex==-1?"":s.substr(sIndex,minlen);
    }
};