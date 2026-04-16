public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> map = new Dictionary<int,int>();

        for(int i = 0; i< nums.Length; i++){
          
            int veggie = target - nums[i];

            if(map.ContainsKey(veggie)){
                return new int[]{map[veggie],i};
            }
                
            map[nums[i]] = i;
            

        } 

        return new int[0];
    }
}
