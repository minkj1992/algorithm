# 배열과 문자열

> 해법관련 소스코드 정리



### 1.1 중복이 없는가

### 1.2 순열 확인

- 풀이1: 정렬 후 비교
```java
// 순열확인 (Sort)

import java.util.Arrays;

class Solution {
    public String sort(String str) {
        char[] content = str.toCharArray();
        Arrays.sort(content);
        return new String(content);
    }

    public boolean isPermutation(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        return sort(s).equals(sort(t));
    }
}
```

- 풀이2: Counter를 활용

```java
// 순열확인 (Counter)

class Solution {
    boolean permutation(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] letters = new int[128];

        char[] sArr = s.toCharArray();
        for (char c : sArr) {
            //Array index는 non-negative int이며, 이로 인해 Explicit type Convert가 일어난다(char -> int, char가 int가 되면 ASCII로 변환된다.)
            letters[c]++;
        }

        char[] tArr = t.toCharArray();
        for (char c : tArr) {
            letters[c]--;
            if (letters[c]<0) {
                return false;
            }
        }
        return true;
    }
}
```



### 1.3 URLify

```java
    public static void replaceSpaces(char[] str, int length) {
        int spaceCount = 0;
        for (int i = 0; i < length; i++) {
            if (str[i] == ' ') {
                spaceCount++;
            }
        }

        int newLength = length + spaceCount * 2;
        for (int i = length - 1; i >= 0; i--) {
            if (str[i] != ' ') {
                str[--newLength] = str[i];
            } else {
                str[--newLength] = '0'; // 값이 참조되기 전에 감소시킨다.
                str[--newLength] = '2';
                str[--newLength] = '%';
            }
        }
    }
```

