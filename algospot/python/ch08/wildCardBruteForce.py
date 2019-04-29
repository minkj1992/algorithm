# [참고자료](https://shoark7.github.io/programming/algorithm/Algospot-Wildcard-%EB%A7%A4%EC%B9%AD.html)

def wildCardBF(pattern,word):
    len_p,len_w = len(pattern),len(word)
    nth = 0
    # 파일명은 공백없이 알파벳 대소문자와 숫자만으로 이뤄져있다.
    while nth<len_p and nth<len_w and (pattern[nth]=='?' or pattern[nth]==word[nth]):nth+=1
    if nth == len_p:return nth==len_w
    # 4번째 조건문에서 걸러진다.    
    # if nth == len_w:return pattern[nth]=='*'
    if pattern[nth]=='*':
        skip=0
        while skip+nth<=len_w:
            if wildCardBF(pattern[nth+1:],word[skip+nth:]): return True
            skip+=1
    return False

if __name__=='__main__':
    ret = []
    for _ in range(int(input())):
        pattern = input()
        problems = [input() for _ in range(int(input()))]
        for word in problems:
            if wildCardBF(pattern,word):ret.append(word)
    print('\n'.join(sorted(ret)))
