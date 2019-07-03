#include <vector>

using namespace std;

long long solution(int N) {
    long long answer = 0;
    bool visited[N] = {0,};
    for(int i=1;i<N;++i){
        if (!visited[i]){continue;}
        for(int j=i+1;j<N;++j){
            if (!visited[j]){continue;}
            else if (visited[j]%visited[i]==0){visited[j]=1;}
        }
        answer += (long long)visited[i];
    }
    
    return answer;
}