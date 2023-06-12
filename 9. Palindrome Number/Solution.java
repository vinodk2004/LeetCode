class Solution {
    public boolean isPalindrome(int x) {
        int ori=x;
        int rev=0;
        while(x!=0 && x>=0){
            rev = rev*10 + x%10;
            x = x/10;
        }
        if (ori == rev){
            return true;
        }
        else{
            return false;
        }  
    }
}