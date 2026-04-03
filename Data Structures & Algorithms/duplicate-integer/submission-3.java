class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> hasone = new HashSet<>();

        for(int i = 0 ; i < nums.length; i++) {
            if(hasone.contains(nums[i])) {
                return true;
            }

            hasone.add(nums[i]);
        }
        
        return false;


    }
}