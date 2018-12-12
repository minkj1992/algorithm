struct Point2D {
	double x;
	double y;
};

void getPoints(int&cvpts, Point2D* &cvhull) {
    cvhull[i].x = ?
    cvhull[i].y = ?
    cvpts
}


int main() {
    int cvpts = 10;
    Point2D* cvhull = (Point2D*)malloc(sizeof(Point2D)*cvpts);
    getPoints(cvpts, cvhull);
    return 0;
}