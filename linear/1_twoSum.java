class Solution {
    
    public int[] twoSum(int[] nums, int target) {
        
        int[] res = new int[2];
        if (nums == null || nums.length < 2) {
            return res;
        }
        
        //copy the nums.
        int[] copy = Arrays.copyOf(nums, nums.length);
        Arrays.sort(copy);
        
        int a = 0, b = 0, i = 0, j = copy.length - 1;
        while (i < j) {
            int sum = copy[i] + copy[j];
            if (sum > target) {
                j --;
            } else if (sum < target) {
                i ++;
            } else {
                res[0] = copy[i];
                res[1] = copy[j];
                break; //找到了就直接break掉
            }
        }
        
        // find index from original list
        int index1 = -1, index2 = -1;
        for (int k = 0; k < nums.length; k++) {
            if (nums[k] == res[0] && index1 == -1) {
                index1 = k;
            } else if (nums[k] == res[1] && index2 == -1) {
                index2 = k;
            }
        }
        res[0] = index1;
        res[1] = index2;
        return res;
        
    }
}