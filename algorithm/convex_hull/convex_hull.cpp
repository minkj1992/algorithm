// #include <bits/stdc++.h>
#include <unistd.h>
#include <sys/mman.h>
// 추가
#include <vector>
#include <cstdio>
#include <algorithm>


#define SZ(v) ((int)(v).size())
#define x first
#define y second

using namespace std;

// template<
//     class T1,
//     class T2
// > struct pair;

typedef long long ll;

// typedef struct {
//         int x, y;
// } pii;

typedef pair<int, int> pii;


int n;
pii p[100003];
vector<int> v, w;

inline bool concave(int i, int j, int k){
	return (ll)(p[j].y-p[i].y)*(p[k].x-p[j].x)
		> (ll)(p[j].x-p[i].x)*(p[k].y-p[j].y);
}

inline bool convex(int i, int j, int k){
	return (ll)(p[j].y-p[i].y)*(p[k].x-p[j].x)
		< (ll)(p[j].x-p[i].x)*(p[k].y-p[j].y);
}

namespace fio {
	size_t sz = 2097152, cur = 2097152;
	off_t ofs;
	char *buf;

	inline void init(size_t n) {
		int pgsize = getpagesize();
		sz = ((n - 1) / pgsize + 1) * pgsize;
		cur = sz;
	}

	inline int next_char() {
		if (sz == cur) {
			if (buf) munmap(buf, sz);
			buf = (char *)mmap(NULL, sz, PROT_READ, MAP_PRIVATE, 0, ofs);
			if (buf == MAP_FAILED) return EOF;
			ofs += sz;
			cur = 0;
		}
		return buf[cur] ? buf[cur++] : EOF;
	}

	inline unsigned next_unsigned() {
		int fst = 0;
		unsigned ans = 0;
		while (fst != EOF && (fst < 48 || fst > 57)) fst = next_char();
		while (fst >= 48 && fst <= 57) {
			ans = 10 * ans + (fst & 15);
			fst = next_char();
		}
		return ans;
	}

	inline int next_int() {
		int fst = 0, ans = 0, inv = 0;
		while (fst != EOF && (fst < 45 || fst > 57)) fst = next_char();
		if (fst == 45) {
			fst = next_char();
			inv = 1;
		}
		while (fst >= 48 && fst <= 57) {
			ans = 10 * ans + (fst & 15);
			fst = next_char();
		}
		return inv ? -ans : ans;
	}
};

int main(){
    n = fio::next_int();
	for (int i=0; i<n; i++){
        p[i].x = fio::next_int();
        p[i].y = fio::next_int();
	}
	sort(p, p+n);

	for (int i=0; i<n; i++){
		while (SZ(v) > 1 && !concave(v[SZ(v)-2], v.back(), i)){
			v.pop_back();
		}
		v.push_back(i);
	}


	for (int i=n-1; i>=0; i--){
		while (SZ(w) > 1 && !convex(i, w.back(), w[SZ(w)-2])){
			w.pop_back();
		}
		w.push_back(i);
	}
	printf("%d\n", SZ(v)+SZ(w)-2);
    return 0;
}
