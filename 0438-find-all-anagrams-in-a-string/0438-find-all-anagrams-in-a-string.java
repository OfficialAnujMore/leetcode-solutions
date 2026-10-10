class Solution {
    public List<Integer> findAnagrams(String s, String p) {

        List<Integer> result = new ArrayList<>();

        int n = s.length();
        int k = p.length();

        if (k > n)
            return result;

        int[] pFreq = new int[26];
        int[] windowFreq = new int[26];

        for (int i = 0; i < k; i++) {
            pFreq[p.charAt(i) - 'a']++;
            windowFreq[s.charAt(i) - 'a']++;
        }

        if (Arrays.equals(pFreq, windowFreq)) {
            result.add(0);
        }

        for (int right = k; right < n; right++) {
            windowFreq[s.charAt(right) - 'a']++;

            windowFreq[s.charAt(right - k) - 'a']--;

            if (Arrays.equals(pFreq, windowFreq)) {
                result.add(right - k + 1);
            }
        }

        return result;

    }
}