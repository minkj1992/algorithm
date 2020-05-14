# 3. Longest Substring Without Repeating Characters
> https://leetcode.com/problems/longest-substring-without-repeating-characters/

## 1st try
- O(n^3)
```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int answer = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j <= n; j++) {
                if (allUnique(s,i,j)) answer = Math.max(answer, j - i);
            }
        }
        return answer;
    }

    public boolean allUnique(String s, int start, int end) {
        Set<Character> set = new HashSet<>();
        for (int i = start; i < end; i++) {
            char c = s.charAt(i);
            if (set.contains(c)) return false;
            set.add(c);
        }
        return true;
    }
}
```