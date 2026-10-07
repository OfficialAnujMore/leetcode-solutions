class Solution {
public:
int n;
vector<int>prices;
vector<vector<vector<int>>>dp;
int dfs(int i,int k,int buy){
if(i>=n|| k<=0){
    //return k>0?0:INT_MIN;
    return 0;
}
//if(k<=0)return INT_MIN;
if(dp[i][k][buy]!=-1)return dp[i][k][buy];
int ans=dfs(i+1,k,buy);
int op=0;
//option1
if(buy){
    op=dfs(i+1,k,!buy);
    if(op!=INT_MIN)
   ans=max(ans,-prices[i]+op);
}
else{
    op=dfs(i+1,k-1,!buy);
    if(op!=INT_MIN)
   ans=max(ans,+prices[i]+op);
  //ans=max(ans,prices[i]+dfs(i+1,k-1,!buy));
}
return dp[i][k][buy]=ans;

}
    int maxProfit(int k, vector<int>& prices) {
        n=prices.size();
        //bool b=true;
        this->prices=prices;
        int b=1;
        dp.resize(n+4,vector<vector<int>>(k+4,vector<int>(3,-1)));
        return dfs(0,k,b);

    }
};