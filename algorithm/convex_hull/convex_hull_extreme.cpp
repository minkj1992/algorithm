// 1. x,y에 대한 오름차순 정렬
// W x H 크기의 평면
// G(점의 배열) : 점의 개수N, 값의 범위 0~(M-1) 
// pG: 길이가 M인 포인터 배열, G의 index가 들어감.
// 2. zone1~4 구성
// 3. 각 zone의 convex set 판별(concave 삭제)

#include <unistd.h>
#include <iostream>
#include <vector>
using namespace std;


typedef long long ll;
typedef struct {
        double x, y;
} Point2D;

Point2D p[100003];
vector<Point2D> v;

inline int ConvexHull_201221618(int npts, Point2D pset[], int &cvpts, Point2D &cvhull){

    // 1. 연산 잘되면 return true or false
    // 2. print(컨벡스홀을 이루는 sequence of points)


    
    return 1;
}

// void print(std::vector<int> const &input)
// {
// 	for (int i = 0; i < input.size(); i++) {
// 		std::cout << input.at(i) << ' ';
// 	}
// }

int main(){

    // input
    sort(p[i].x)
    sort(p[i].y)
    
    p[0].x = 2.3;
    p[0].y = 2.9;
    // v.insert(0,p[0]);
    printf ("floats: %f %f\n", p[0].x,p[0].y);
    printf("%f", (double *)&v);
    // printf ("floats: %f %f\n", v.back.x,v.back.y);
    // printf(v[0])
    return 1;
}