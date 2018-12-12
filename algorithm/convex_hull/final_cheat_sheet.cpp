
#include <algorithm>
#include <iostream>
#include <vector>
#include <math.h> 
// #include <time.h>
#include <chrono>  // for high_resolution_clock
using namespace std;

struct Point2D {
	double x;
	double y;

	Point2D(double xIn, double yIn) : x(xIn), y(yIn) { } 
};

// The z-value of the cross product of segments 
// (a, b) and (a, c). Positive means c is ccw
// from (a, b), negative cw. Zero means its collinear.
double ccw(const Point2D& a, const Point2D& b, const Point2D& c) {
	return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

// Returns true if a is lexicographically before b.
bool isLeftOf(const Point2D& a, const Point2D& b) {
	return (a.x < b.x || (a.x == b.x && a.y < b.y));
}

// Used to sort points in ccw order about a pivot.
struct ccwSorter {
	const Point2D& pivot;

	ccwSorter(const Point2D& inPivot) : pivot(inPivot) { }

	bool operator()(const Point2D& a, const Point2D& b) {
		return ccw(pivot, a, b) < 0;
	}
};

// The length of segment (a, b).
double len(const Point2D& a, const Point2D& b) {
	return sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y));
}

// The unsigned distance of p from segment (a, b).
double dist(const Point2D& a, const Point2D& b, const Point2D& p) {
	return fabs((b.x - a.x) * (a.y - p.y) - (b.y - a.y) * (a.x - p.x)) / len(a, b);
}

// Returns the index of the farthest Point2D from segment (a, b).
size_t getFarthest(const Point2D& a, const Point2D& b, const vector<Point2D>& v) {
	size_t idxMax = 0;
	double distMax = dist(a, b, v[idxMax]);

	for (size_t i = 1; i < v.size(); ++i) {
		double distCurr = dist(a, b, v[i]);
		if (distCurr > distMax) {
			idxMax = i;
			distMax = distCurr;
		}
	}

	return idxMax;
}


// The gift-wrapping algorithm for convex hull.
// https://en.wikipedia.org/wiki/Gift_wrapping_algorithm
vector<Point2D> giftWrapping(vector<Point2D> v) {
	// Move the leftmost Point2D to the beginning of our vector.
	// It will be the first Point2D in our convext hull.
	swap(v[0], *min_element(v.begin(), v.end(), isLeftOf));

	vector<Point2D> hull;
	// Repeatedly find the first ccw Point2D from our last hull Point2D
	// and put it at the front of our array. 
	// Stop when we see our first Point2D again.
	do {
		hull.push_back(v[0]);
		swap(v[0], *min_element(v.begin() + 1, v.end(), ccwSorter(v[0])));
	} while (v[0].x != hull[0].x && v[0].y != hull[0].y);

	return hull;
}


// The Graham scan algorithm for convex hull.
// https://en.wikipedia.org/wiki/Graham_scan
vector<Point2D> GrahamScan(vector<Point2D> v) {
	// Put our leftmost Point2D at index 0
	swap(v[0], *min_element(v.begin(), v.end(), isLeftOf));

	// Sort the rest of the points in counter-clockwise order
	// from our leftmost Point2D.
	sort(v.begin() + 1, v.end(), ccwSorter(v[0]));
	
	// Add our first three points to the hull.
	vector<Point2D> hull;
	auto it = v.begin();
	hull.push_back(*it++);
	hull.push_back(*it++);
	hull.push_back(*it++);
	
	while (it != v.end()) {
		// Pop off any points that make a convex angle with *it
		while (ccw(*(hull.rbegin() + 1), *(hull.rbegin()), *it) >= 0) {
			hull.pop_back();
		}
		hull.push_back(*it++);
	}

	return hull;
}


// The monotone chain algorithm for convex hull.
vector<Point2D> monotoneChain(vector<Point2D> v) {
	// Sort our points in lexicographic order.
	sort(v.begin(), v.end(), isLeftOf);
	
	// Find the lower half of the convex hull.
	vector<Point2D> lower;
	for (auto it = v.begin(); it != v.end(); ++it) {
		// Pop off any points that make a convex angle with *it
		while (lower.size() >= 2 && ccw(*(lower.rbegin() + 1), *(lower.rbegin()), *it) >= 0) {
			lower.pop_back();
		}
		lower.push_back(*it);
	}
		
	// Find the upper half of the convex hull.
	vector<Point2D> upper;
	for (auto it = v.rbegin(); it != v.rend(); ++it) {
		// Pop off any points that make a convex angle with *it
		while (upper.size() >= 2 && ccw(*(upper.rbegin() + 1), *(upper.rbegin()), *it) >= 0) {
			upper.pop_back();
		}
		upper.push_back(*it);
	}

	vector<Point2D> hull;
	hull.insert(hull.end(), lower.begin(), lower.end());
	// Both hulls include both endpoints, so leave them out when we 
	// append the upper hull.
	hull.insert(hull.end(), upper.begin() + 1, upper.end() - 1);
	return hull;
}


// Recursive call of the quickhull algorithm.
void quickHull(const vector<Point2D>& v, const Point2D& a, const Point2D& b, 
			   vector<Point2D>& hull) {
    
	if (v.empty()) {
		return;
	}

	Point2D f = v[getFarthest(a, b, v)];

	// Collect points to the left of segment (a, f)
	vector<Point2D> left;
	for (auto p : v) {
		if (ccw(a, f, p) > 0) {
			left.push_back(p);
		}
	}
	quickHull(left, a, f, hull);
	
	// Add f to the hull
	hull.push_back(f);

	// Collect points to the left of segment (f, b)
	vector<Point2D> right;
	for (auto p : v) {
		if (ccw(f, b, p) > 0) {
			right.push_back(p);
		}
	}
	quickHull(right, f, b, hull);
}

// QuickHull algorithm. 
vector<Point2D> quickHull(const vector<Point2D>& v) {
	vector<Point2D> hull;
	
	// Start with the leftmost and rightmost points.
	Point2D a = *min_element(v.begin(), v.end(), isLeftOf);
	Point2D b = *max_element(v.begin(), v.end(), isLeftOf);

	// Split the points on either side of segment (a, b)
	vector<Point2D> left, right;
	for (auto p : v) {
		ccw(a, b, p) > 0 ? left.push_back(p) : right.push_back(p);
	}
	
	// Be careful to add points to the hull
	// in the correct order. Add our leftmost Point2D.
	hull.push_back(a);

	// Add hull points from the left (top)
	quickHull(left, a, b, hull);

	// Add our rightmost Point2D
	hull.push_back(b);

	// Add hull points from the right (bottom)
	quickHull(right, b, a, hull);

	return hull;
}

vector<Point2D> getPoints() {
	vector<Point2D> v;
	
	const double lo = -100.0;
	const double hi = 100.0;

	for (int i = 0; i < 1000; ++i) {
		double x = lo + 
			static_cast<double>(
				rand()) / static_cast<double>(RAND_MAX / (hi - lo));

		double y = lo + 
			static_cast<double>(
				rand()) / static_cast<double>(RAND_MAX / (hi - lo));

		v.push_back(Point2D(x, y));
	}

	return v;
}

void print(const vector<Point2D>& v) {
	for (auto p : v) {
		cout << p.x << ", " << p.y << endl;
	}
}


inline int ConvexHull_201221618(int npts, Point2D pset[], int &cvpts, Point2D &cvhull){
    

    return 1;
}

int main() { 	
	vector<Point2D> v = getPoints();
	
    
    // Record start time
    // auto start = std::chrono::high_resolution_clock::now();
    vector<Point2D> h = quickHull(v);
	cout << "quickHull Point2D count: " << h.size() << endl;
	print(h);
    // Record end time
    // auto finish = std::chrono::high_resolution_clock::now();
    // std::chrono::duration<double> elapsed = finish - start;
    // std::cout << "Elapsed time: " << elapsed.count() << " s\n";

    // Record start time
    // auto start = std::chrono::high_resolution_clock::now();
 	h = giftWrapping(v);
	cout << endl << "giftWrapping Point2D count: " << h.size() << endl;
	print(h);
    // Record end time
    // auto finish = std::chrono::high_resolution_clock::now();
    // std::chrono::duration<double> elapsed = finish - start;
    // std::cout << "Elapsed time: " << elapsed.count() << " s\n";

    // Record start time
    // auto start = std::chrono::high_resolution_clock::now();
	h = monotoneChain(v);
	cout << endl << "monotoneChain Point2D count: " << h.size() << endl;
	print(h);
    // Record end time
    // auto finish = std::chrono::high_resolution_clock::now();
    // std::chrono::duration<double> elapsed = finish - start;
    // std::cout << "Elapsed time: " << elapsed.count() << " s\n";

    // Record start time
    // auto start = std::chrono::high_resolution_clock::now();
	h = GrahamScan(v);
	cout << endl << "GrahamScan Point2D count: " << h.size() << endl;
	print(h);
    // Record end time
    // auto finish = std::chrono::high_resolution_clock::now();
    // std::chrono::duration<double> elapsed = finish - start;
    // std::cout << "Elapsed time: " << elapsed.count() << " s\n";

	return 0;
}
