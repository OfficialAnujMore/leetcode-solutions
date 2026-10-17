class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // nums = [1,1,1,2,2,3], k = 2
        // Store each number and it frequency
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        // Min heap to store the ordered frequency
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(map.get(a), map.get(b)));

        for (int num : map.keySet()) {
            minHeap.offer(num);

            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = minHeap.poll();
        }

        return result;

    }
}