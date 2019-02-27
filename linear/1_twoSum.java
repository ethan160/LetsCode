/* Solution 1: 
first idea --> brute force always:
use two for loop to through the each elements in the array: 
instead of thinking of nums[i] + nums[j] == target; using 
nums[j] == target - nums[i]
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] == target - nums[i]) {
                    return new int[] {i, j};
                }
            }
        }
        throw new IllegalArgumentException ("no such solution");
    }
}

// Time complexity: O(n^2) ; Space complexity: O(1)


/*Solution2: 
How to reduce the time complexity? Use space to reduce time --> hashmap
while iterate though the loop and insert all the elements in the map; 
we can look back to see if the current value already in the map; */

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            //while loop though and insert all the elements in the map
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}

//Time complexity O(n^2) ; Space complexity: O(n)


/* Solution3:
If we have still want to reduce time complexity, how to improve? 
Normally,time complexity less than O(n) is log(n);
--> can we sort the array and then use binary search? 
step1: create a length 2 array to store the results; (corer cases)
step2: copy the original array 
step3: use binary search to find the two nums
step4: go back to original array, find the original associated indexes; 

*/

class Solution {
    
    public int[] twoSum(int[] nums, int target) {
        
        int[] res = new int[2];
        //corner case 
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

// Time Complexity Olog(n); (Sort complexity is log(n), binary search also log(n); one mistake above)
// Sapce Complexity: O(n)








