/*
Time complexity: O(n) average case
- Building the HashSet: O(n)
- Iterating through the HashSet: O(n)
- Total work across all while loops: O(n)

Space complexity: O(n)
- The HashSet stores at most n unique numbers.
- Other variables use O(1) space.
*/

class Solution {
    public int longestConsecutive(int[] nums) {

        HashSet<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        int maxLength = 0;

        for (int num : set) {
            if (!set.contains(num - 1)) {
                int currentNum = num;
                int currentLength = 1;

                while (set.contains(currentNum + 1)) {
                    currentNum++;
                    currentLength++;
                }
                maxLength = Math.max(maxLength, currentLength);
            }
        }

        return maxLength;
    }
}