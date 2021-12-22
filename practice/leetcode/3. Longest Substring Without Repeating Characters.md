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
## 2nd try(20.05.15)
- tc: O(n^2)
- sc: O(n)
```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
            Map<Character, Boolean> map = new HashMap<>();
            int subLength = 0;
            for (int j = i; j < s.length(); j++, ++subLength) {
                Character c = s.charAt(j);
                if (map.containsKey(c)) {
                    break;
                }
                map.put(c, true);
            }
            answer = Math.max(answer, subLength);
        }
        return answer;
    }
}
```

## 3rd try
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

## 4th try
> Sliding Window Optimized

- TC: O(n) 
```java
//20.05.14
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;
        Map<Character, Integer> map = new HashMap<>(); // current index of character
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
```java
//20.05.15
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int answer = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int end = 0, start = 0; end < n; end++) {
            char c = s.charAt(end);
            if (map.containsKey(c)) { start = Math.max(map.get(c),start); }
            answer = Math.max(end-start+1, answer);
            map.put(c,end+1);
        }
        return answer;
    }
}
```

## 5th try (ASCII Array)
- Hash Key 만드는 overhead 줄인 버전
```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int answer = 0;
        int n = s.length();
        int[] index = new int[128];
        for (int j = 0, i = 0; j <n; j++) {
            i = Math.max(index[s.charAt(j)], i);
            answer = Math.max(answer, j - i + 1);
            index[s.charAt(j)] = j + 1;
        }
        return answer;
    }
}
```