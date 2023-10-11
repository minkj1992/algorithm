"""
# https://leetcode.com/problems/word-ladder/
# time: O(L * 26 * n) -> O(n)
# space: O(n)

import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)): # word length (const)
                for c in string.ascii_lowercase: # 26
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
"""
### Solution0 (8812ms)
import collections
from typing import List


def is_adjacent(str1: str, str2: str) -> bool:
    flag = False
    for a, b in zip(str1, str2):
        if a == b:
            continue
        if flag:
            return False
        flag = True
    return True


class Solution:
    def clean(self, pop_list: List[int]) -> None:
        # reindex 되는 것을 방지하려면, 뒤에서 부터 del 해주어야 한다.
        for i in sorted(pop_list, reverse=True):
            del self.word_list[i]

    def ladderLength(self, beginWord: str, endWord: str, raw_word_list: List[str]) -> int:
        if endWord not in raw_word_list:
            return 0
        self.word_list = list(set(raw_word_list) - set(beginWord))
        print(self.word_list)
        num_of_words = 1
        queue = collections.deque([beginWord])

        while queue:
            n = len(queue)
            num_of_words += 1
            for _ in range(n):
                target = queue.pop()
                pop_list = []
                for i, neighbor in enumerate(self.word_list):
                    if not is_adjacent(target, neighbor):
                        continue
                    if neighbor == endWord:
                        return num_of_words
                    pop_list.append(i)
                    queue.appendleft(neighbor)
                self.clean(pop_list)
        return 0


### Solution1 (time exceed)
import string
from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList) - set(beginWord)
        if endWord not in word_set:
            return 0

        words = list(word_set)
        visited = [False] * len(words)
        queue = deque([beginWord])
        loop_count = 1
        while queue:
            word = queue.pop()
            n = len(queue)
            loop_count += 1
            for _ in range(n):
                for i, word2 in enumerate(wordList):
                    if visited[i]:
                        continue
                    if not Solution.is_adjacent(word, word2):
                        continue
                    if word2 == endWord:
                        return loop_count

                    visited[i] = True
                    queue.appendleft(word2)
        return 0

    @staticmethod
    def is_adjacent(str1, str2) -> bool:
        life = 1
        for a, b in zip(str1, str2):
            if a == b:
                continue
            if life == 0:
                return False
            life -= 1
        return True


# Solution2 (time limit exceed)
class Solution2(object):
    from collections import deque

    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList) - set(beginWord)
        if endWord not in word_set:
            return 0

        words = list(word_set)
        visited = [False] * len(words)
        queue = deque([beginWord])
        loop_count = 1
        while queue:
            n = len(queue)
            loop_count += 1
            for _ in range(n):
                word = queue.pop()
                for i, word2 in enumerate(words):
                    if visited[i]:
                        continue
                    if not Solution.is_adjacent(word, word2):
                        continue
                    if word2 == endWord:
                        return loop_count

                    visited[i] = True
                    queue.appendleft(word2)
        return 0

    @staticmethod
    def is_adjacent(str1: str, str2: str) -> bool:

        life = 1
        for a, b in zip(str1, str2):
            if a == b:
                continue
            if life == 0:
                return False
            life -= 1
        return True


### Solution3 (O)
from collections import deque


def get_adjacent_word(word):
    for i, c in enumerate(word):
        for alphabet in string.ascii_lowercase:
            if alphabet == c:
                continue
            yield word[:i] + alphabet + word[i + 1 :]


class Solution3:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList) - set(beginWord)
        if endWord not in words:
            return 0

        queue = deque([beginWord])
        loop_count = 1
        while queue:
            n = len(queue)
            loop_count += 1
            for _ in range(n):
                word = queue.pop()
                for neighbor in get_adjacent_word(word):
                    if neighbor not in words:
                        continue
                    if neighbor == endWord:
                        return loop_count
                    queue.appendleft(neighbor)
                    words.remove(neighbor)
        return 0


### Solution4 ()

import string
import collections


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList) - set(beginWord)
        if endWord not in words:
            return 0

        queue = collections.deque(
            [
                beginWord,
            ]
        )
        loop_count = 1
        while queue:
            n = len(queue)
            loop_count += 1
            for _ in range(n):
                word = queue.popleft()
                for i, c in enumerate(word):
                    for alphabet in string.ascii_lowercase:
                        nxt_word = word[:i] + alphabet + word[i + 1 :]
                        if nxt_word == endWord:
                            return loop_count
                        if nxt_word not in words:
                            continue
                        words.remove(nxt_word)
                        queue.append(nxt_word)
        return 0
