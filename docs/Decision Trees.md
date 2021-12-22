# Decision Trees
leaf 갯수가 n!, 높이는 leaf 갯수에 log를 씌운것 그래서 최소한 nlogn

# Adversary Arguments
그냥 한번 읽어바라

# problem reduction

Q의 lower bound가 f(n)이라고 알고 있을때, P의 lower bound(g(n))를 알고 싶을 때
1)
Q -> p로 h(n)의 시간이 걸려서 바꾼다
2)
P를 푼다. 그 후 Q로 다시 바꾼다. 

total = 2h(n) + g(n) >= f(n)이 된다.
h(n)이 f(n)보다 작다면 g(n)이 f(n)보다 커야 한다. 그렇지 않으면 f(n)이 Q의 lower bound가 되지 못한다. 

# Classifying Problem Complexity

tractable: 우리가 문제를 풀 수 있다. polynomial time안에 풀수 있는 알고리즘으로. ex) n^10 시간 안에 풀 수 있는 문제
intractable: poly이 아닌 문제 (exp, factorial time...)

# Optimization and Descision Problem

Optimization Problem: 주어진 cost를 가장 적게 하는 것
Decision Problem: 해밀턴 처럼, 주어진 node를 모두 지나가는 길이 있느냐 없느냐.(yes/no)

Optimization은 Descision problem을 반복함으로써 풀 수 있다.

# Class p (상식, p-problem)

poly time안에 답을 풀 수 있는 문제들의 집합 = P

# Class NP

nondeterministic polynomial(NP): candidate들이 주어져있고 그게 답인지 아닌지 poly time안에 판단 할 수 있는 문제들
해밀턴 path도 ( factorial 조합 만들고, edge가 있는지만 check하면 되니까 1개의 path 검사는 O(n)

모든 P는 NP에 들어가거나, 아니면 같다.

# NP-Complete
NP 문제들 중에서 가장 어려운 문제들이 NP-Complete이다.

가장 어렵다: NP의  모든 문제들이 Poly time안에 풀수 있는 D문제로 풀 수 있다면, 그 D가 NP-Complete

ex) CNF-sat

# Turing's halting problem
계산 할 수 없는 문제가 존재하느냐?에 대한 답을 제공

:이 program이 무한 loop에 빠지는지 아닌지 여부에 대한 답을 찾을 수 있을까? (프로그램 검증하는 또 다른 프로그램)
이론적으로 불가능하다고 증명됬다. (proof is in book)

만약 굉장히 좋은 검증 프로그램이 있다고 가정한다면(A 프로그램) 
A(P,i) = 1 or 0 

또다른 program Q(P)
A(P,P): 프로그램의 입렵값으로 자기자신을 넣어준다. if 0 -> halt, 1 



Q(p)
	if(A(P,P)) = 0
		return;
	else
		while(true);


ProgramQ.exe()

main(){
	Q(programQ);
}

즉 여기서 모순이 발생한다. q가 무한푸르에 빠지면 끝난다는 모순이 생긴다. 멈춘다면 무한루프에빠진다.

즉 현실적으로 A()알고리즘이 존재할 수 없다. 

결국 우리가 풀 수 없는 문제들이 존재 할 수 밖에 없다.




