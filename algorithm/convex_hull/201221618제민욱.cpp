// 201221618 제민욱 
#include <algorithm>
#include <iostream>
#include <vector>
#include <math.h> 
using namespace std;

struct Point2D {
	double x;
	double y;
};

/* 수학 계산용 함수들 START */
double counter_clock_wise(const Point2D& a, const Point2D& b, const Point2D& c) {
	return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

bool isleft(const Point2D& a, const Point2D& b) {
	return (a.x < b.x || (a.x == b.x && a.y < b.y));
}

struct counter_clock_sorter {
	const Point2D& piv;

	counter_clock_sorter(const Point2D& inPivot) : piv(inPivot) { }

	bool operator()(const Point2D& a, const Point2D& b) {
		return counter_clock_wise(piv, a, b) < 0;
	}
};

double len(const Point2D& a, const Point2D& b) {
	return sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y));
}

double dist(const Point2D& a, const Point2D& b, const Point2D& p) {
	return fabs((b.x - a.x) * (a.y - p.y) - (b.y - a.y) * (a.x - p.x)) / len(a, b);
}

size_t farthest(const Point2D& a, const Point2D& b, const vector<Point2D>& v) {
	size_t index_max = 0;
	double dist_max = dist(a, b, v[index_max]);

	for (size_t i = 1; i < v.size(); ++i) {
		double cur_dist = dist(a, b, v[i]);
		if (cur_dist > dist_max) {
			index_max = i;
			dist_max = cur_dist;
		}
	}
	return index_max;
}
/* 수학 계산용 함수들  END*/


// recursive call 
void quickHull(const vector<Point2D>& v, const Point2D& a, const Point2D& b, 
			   vector<Point2D>& hull) {
    
	if (v.empty()) {
		return;
	}

	Point2D f = v[farthest(a, b, v)];

	// Collect points to the left of segment (a, f)
	vector<Point2D> left;
	for (auto p : v) {
		if (counter_clock_wise(a, f, p) > 0) {
			left.push_back(p);
		}
	}
	quickHull(left, a, f, hull);
	
	// Add f to the hull
	hull.push_back(f);

	// Collect points to the left of segment (f, b)
	vector<Point2D> right;
	for (auto p : v) {
		if (counter_clock_wise(f, b, p) > 0) {
			right.push_back(p);
		}
	}
	quickHull(right, f, b, hull);
}

// 내 코드 정답용 print
void print(const vector<Point2D>& v) {
	for (auto p : v) {
		cout << p.x << ", " << p.y << endl;
	}
}

// 답 정답용 print
void print(int &cvpts,Point2D* &cvhull) {
	
	for (int i = 0; i < cvpts; ++i){
		cout << cvhull[i].x << ", " << cvhull[i].y << endl;
	}
}

// QuickHull algorithm
vector<Point2D> quickHull(const vector<Point2D>& v) {
	vector<Point2D> hull;
	
    // // 맨 왼쪽, 맨 오른쪽 pick
	Point2D a = *min_element(v.begin(), v.end(), isleft);
	Point2D b = *max_element(v.begin(), v.end(), isleft);

	// segment split
	vector<Point2D> left, right;
	for (auto p : v) {
		counter_clock_wise(a, b, p) > 0 ? left.push_back(p) : right.push_back(p);
	}
	// leftmost Point2D
	hull.push_back(a);
    
	// top(left) 포인트 add
	quickHull(left, a, b, hull);

	// rightmost Point2D
	hull.push_back(b);

	// bottom(right) 포인트 add
	quickHull(right, b, a, hull);

	return hull;
}


/*
int npts: 입력점의 개수
Point2D pset[]: 입력점의 데이터, point2D element, array
int &cvpts: Convex hull 정점 개수
Point2D* &cvhull: Convex hull 정점 데이터(Point2D 포인터 size*cvpts갯수인 malloc 메모리 영역)
*/

int check(const vector<Point2D>& h, Point2D* &cvhull){
	for (int i = 0; i < h.size(); ++i){
		if(cvhull[i].x != h[i].x || cvhull[i].y != h[i].y){
			return 0;
		}
	}
	return 1;
} 

// 입력 점의 갯수, 입력점의 데이터, convex_set 갯수, convex_set 점들의 집합.
// bool ConvexHull_201221618(int npts, Point2D pset[], int &cvpts, Point2D &cvhull){
int ConvexHull_201221618(int npts, Point2D pset[],int &cvpts, Point2D* &cvhull){    

    vector<Point2D> h = quickHull(vector<Point2D>(pset, pset + npts));
	// cout << "quickHull Point2D count: " << h.size() << endl;
    // printf("###############################My convex hull output######################\n");
	// print(h);
	// printf("###############################Answer convex hull output######################\n");
	// print(cvpts, cvhull);
    return check(h,cvhull);
}



vector<Point2D> ConvexHull_201221618(int npts, Point2D pset[]){    
    vector<Point2D> h = quickHull(vector<Point2D>(pset, pset + npts));
    return h;
}

// // Random sample
// Point2D *getPoints(int npts) {
// 	Point2D *pset = new Point2D[npts];
// 	// static Point2D pset[npts];
// 	// vector<Point2D> v;

// 	const double lo = -100.0;
// 	const double hi = 100.0;

// 	for (int i = 0; i < npts; ++i) {
// 		double x = lo + 
// 			static_cast<double>(
// 				rand()) / static_cast<double>(RAND_MAX / (hi - lo));

// 		double y = lo + 
// 			static_cast<double>(
// 				rand()) / static_cast<double>(RAND_MAX / (hi - lo));

// 		// v.push_back(Point2D(x, y));
//         pset[i].x = x;
//         pset[i].y = y;       
// 	}
// 	// // return v;
//     return pset;
// }

// // vector2malloc
// void vec2mal(vector<Point2D>& v, Point2D* &cvhull) {
// 	for (int i = 0; i < v.size(); ++i) {
// 		Point2D tmp = v[i];
// 		cvhull[i] = tmp;
// 	}
// }




int main() { 	

	// variable setting
	// int npts = 1000;
	// Point2D *pset = getPoints(npts);
	// vector<Point2D> tmp = ConvexHull_201221618(npts,pset);
	// int cvpts = tmp.size();
	// Point2D* cvhull = (Point2D*)malloc(sizeof(Point2D)*cvpts);
	// vec2mal(tmp,cvhull);



// 결과값 return
	printf(ConvexHull_201221618(npts,pset,cvpts,cvhull) ? "결과값: True" : "결과값: False");  
	free(cvhull);
	return 0;
}
