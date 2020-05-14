# 3. Longest Substring Without Repeating Characters
> https://leetcode.com/problems/longest-substring-without-repeating-characters/

## 1st try
> Brute Force
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

## 2nd try
> Sliding Window
- time cpx = O(2n) = O(n)
- spcae cpx = O(min(n,m))
  - n: length of String
  - m: number of alphabet & character
```java
import java.util.HashSet;
import java.util.Set;

// sliding window
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int answer = 0, i = 0, j = 0;
        while (i < n && j < n) {
            if (!set.contains(s.charAt(j))) {
                set.add(s.charAt(j++));
                answer = Math.max(answer, j - i);
            } else {
                set.remove(s.charAt(i++)); // 현재까지는 중복이 없기때문에 remove 시전해주면 된다.
            }
        }
        return answer;
    }
}
```

## 3rd try
> Sliding Window Optimized
```java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;
        Map<Character, Integer> map = new HashMap<>(); // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)), i);
            }
            ans = Math.max(ans, j - i + 1);
            map.put(s.charAt(j), j + 1);
        }
        return ans;
    }
}
```