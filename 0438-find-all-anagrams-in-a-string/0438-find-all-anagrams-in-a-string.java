class Solution {
    public List<Integer> findAnagrams(String s, String p) {

        List<Integer> result = new ArrayList<>();
        int n = s.length();
        int k = p.length();

        char[] pArray = p.toCharArray();
        Arrays.sort(pArray);

        for (int i = 0; i <= n - k; i++) {
            String window = s.substring(i, i + k);
            char[] windowArray = window.toCharArray();
            Arrays.sort(windowArray);

            if (Arrays.equals(pArray, windowArray)) {
                result.add(i);
            }
        }

        return result;

    }
}