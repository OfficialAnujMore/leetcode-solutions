class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, ArrayList<String>> values = new HashMap<>();

        for (String str : strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedStr = new String(charArray);

            values.putIfAbsent(sortedStr, new ArrayList<>());
            values.get(sortedStr).add(str);
        }

        return new ArrayList<>(values.values());
    }
}