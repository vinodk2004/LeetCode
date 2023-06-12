class Solution {
    public int[] leftRightDifference(int[] nums) {
        int[] leftSum = new int[nums.length];
        int[] rightSum = new int[nums.length];
        leftSum[0] = 0;
        rightSum[nums.length-1] = 0;
        for (int i = 0 ; i<nums.length-1 ; i++){
            leftSum[i+1] = leftSum[i]+nums[i];
        }
        for(int i=nums.length-1 ; i>0 ;i--){
            rightSum[i-1] = rightSum[i] + nums[i];
        }
        for(int i = 0 ; i<nums.length ; i++){
            nums[i] = Math.abs(leftSum[i] - rightSum[i]);
        }
        return nums;
    }
}