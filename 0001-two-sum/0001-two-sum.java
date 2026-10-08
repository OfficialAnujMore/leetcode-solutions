class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashmap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {

            int difference = target - nums[i];
            if (hashmap.containsKey(difference)) {
                return new int[] { hashmap.get(difference), i };
            } else {
                hashmap.put(nums[i], i);
            }
        }

        return new int[] {};

    }
}