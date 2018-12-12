#include <unistd.h>
using namespace std;


typedef long long ll;
typedef struct {
        double x, y;
} Point2D;

Point2D p[100003];
 
inline int ConvexHull_201221618(int npts, Point2D pset[], int &cvpts, Point2D &cvhull){
// 	// i =x, j = 
//     // //  return true or false
//     // // print(컨벡스홀을 이루는 sequence of points)

//     // return (ll)(p[j].y-p[i].y)*(p[k].x-p[j].x)
// 	// 	< (ll)(p[j].x-p[i].x)*(p[k].y-p[j].y);
//     return 1;
// }

// // 1. 외곽선 구하기
// // 2. 외곽선위에 패턴을 포함하는 가장 작은 직사각형의 bounding box덮어씌우기(외곽선과 bounding box 겹치는 점 추출)
// // 2. G = 겹치는 점들의 그룹
// // 2. S = G(i)G(i+1)사이에 있는 점들의 집합 = 세그먼트
// // 2. 전체패턴(P) = G U S && G  n S = NONE

// // 3. 세그먼트 바로 앞의 점 S(c) (x1,y1), 맨 뒤의점(S(d)(x2,y2))
// //  a = y2-y1, b = x1-x2, c = Y1*X2-Y2*X1;
// // a = ;
// // b = ;
// // c = ;
// // Remove mark는 검사 대상에서 제외 한다는 bool variable
// // 이게 실제 구현에서 필요할까?
// // 모든 세그먼트들에 대하여 후보점들 변별 실행
// for(i=0; i<len(S);i++){
//     for(j=0; j<len(S[i]); j++){
//         y=S[j].y; x=S[j].x;
//         if ((a*x+b*y+c)>0){
//             S[j] == convex point;
//             mark not_remove
//         }else{
//             S[j] != convex_point;
//             Remove mark;
//         }
//     }
// }

// 4. 최종 Convex_set 추출
// 추출된 후보점들을 대상으로 최종적인 입력 패턴의 convex_set구하는 단계




int main(){
    return 0;
}





