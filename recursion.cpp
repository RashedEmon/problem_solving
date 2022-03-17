#include <iostream>
int solve(int a,int b,int c,int sum,int n,int i){
    if(i==n){
        return sum;
    }
    sum+=a*b*c;
    return solve(a*2,b+2,c-1,sum,n,i+1);
    
}
int main() {
    int res=solve(2,3,4,0,3,0);
    std::cout<<res;
    
    return 0;
}
