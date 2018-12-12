#include <algorithm>
#include <iostream>
#include <vector>
#include <math.h> 
#include <chrono>  // for high_resolution_clock
using namespace std;

int cvpts = 10;

struct Point2D {
	double x;
	double y;
};

// Random sample
void getPoints(int&cvpts, Point2D* &cvhull) {
	// Point2D *pset = new Point2D()[cvpts]; 
	// printf("%d",cvpts);
	// // vector<Point2D> v;
	const double lo = -100.0;
	const double hi = 100.0;
    

	for (int i = 0; i < cvpts; ++i) {
		double x = lo + 
			static_cast<double>(
				rand()) / static_cast<double>(RAND_MAX / (hi - lo));

		double y = lo + 
			static_cast<double>(
				rand()) / static_cast<double>(RAND_MAX / (hi - lo));

		// v.push_back(Point2D(x, y));
        cvhull[i].x = x;
        cvhull[i].y = y;
        
	}

	// return v;
    // return ;
}

void print(Point2D* &cvhull) {
	
	cout << cvhull[0].x << ", " << cvhull[0].y << endl;
	
}

int main() {
    Point2D* cvhull = (Point2D*)malloc(sizeof(Point2D)*cvpts);
    getPoints(cvpts, cvhull);
    print(cvhull);
    cvhull();
    free(cvhull);
    
	return 0;
}