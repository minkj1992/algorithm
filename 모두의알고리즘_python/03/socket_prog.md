network programming
socket programming

프로세스: 프로그램(실행가능한 파일) 인스턴스, 실행중인 프로그램
물리적으로 연속적이어야 한다(제약)

가상 메모리(페이징)-> 단편화 문제를 해결 시키기 위하여.

가상 메모리:
1)세그먼테이션 방식: intel cpu 
2)페이징(4k, 8k) 방식: intel cpu 이외의 (linux)
PFN(페이지 프레임 넘버)

real mode: fragmentation 문제, 
protected mode: 프로세스 끼리 침범할 수 없다. 운영체제의 도움 없이는


-모든 프로세스는 자신만의 페이지 테이블을 가지고 있다. ( 자신만의 가상 주소를 가지고 있다.)
=> 서로 다른 프로세스가 데이터를 교환하기 위해서는 IPC(inter process ,운영체제가 도와주는)가 필요하다.

IPC(inter process communication)
-message queue
-semaphore(게임 처럼 뮤텍스(=바이너리 세마포어) 세마포어는 2개 이상 가능)
-signal(동기화, kill-l )
-shared memory()

```terminal
minwookje@minwookje-900X5L:~$ ipcs

------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages    

------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status      
0x00000000 196608     minwookje  600        67108864   2          dest         
0x00000000 360449     minwookje  600        524288     2          dest         
0x00000000 458754     minwookje  600        524288     2          dest         
0x00000000 491523     minwookje  600        524288     2          dest         
0x00000000 524292     minwookje  600        524288     2          dest         
0x00000000 720901     minwookje  600        524288     2          dest         
0x00000000 8060934    minwookje  600        524288     2          dest         
0x00000000 8159239    minwookje  600        4194304    2          dest         
0x00000000 1015817    minwookje  600        524288     2          dest         

------ Semaphore Arrays --------
key        semid      owner      perms      nsems     
```


- TCP/IP
- FIle I/O: 리눅스의 기본 철학, "모든 인터페이스는 파일로(다형적으로, 폴리몰피즘)" = VFS(virtual file system, system call:open,read write, close 등을 통하여서 led, 프린터 )
virtual : compile time이 아닌  

checked exception
unchecked exception


File
//runtime에 기능들을 추가할 수 있다. 
DataInputStream

java NIO = New I O
자바의 io 속도 개선 

자바: 비메모리자원(file과 같은 형태)에 대해서는 반드시 명시적인 종료 메서드를 호출해야 한다. 가비지 컬렉션이 메모리자원을 

예외처리의 단점: 실제 코드처리 보다 예외처리가 훨씬 많아진다. java 6까지는 ...
이를 해결하기 위해서 java7에서는 try with resources문법! -> finally 하게 close하는것을 보장해준다. AutoClosable 인터페이스를 구현하면 된다. 



주소
    -컴퓨터의 주소(ip)
    -프로세스의 주소(port Address)

TCP 통신 
    - connection 수립
    -Domain name(Dns domain name server -> ip address)
    -kt에서는 168.126.63.1
    -google 
    8.8.8.8 
    8.8.4.4



IP: 
minwookje@minwookje-900X5L:~$ nslookup google.com
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	google.com
Address: 216.58.197.142
Name:	google.com
Address: 2404:6800:4004:800::200e


PORT:
서비스의 종류에 따라서 약속된 포트가 있다.
=> well known PORT
80: 일반적인
ex) 210.89.160.88:80

HTTP Server: 80
HTTPS:  443
SSH: 22(ec2같이)
FTP: 21
Redis: 6379

서버 과정
#### socket:
server socket: 연결을 수립하기 위한 socket
-> socket, listen, bind, accept
socket : 데이터 교환
