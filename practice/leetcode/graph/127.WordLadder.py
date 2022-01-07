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
