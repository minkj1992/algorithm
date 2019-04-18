#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#define MAX_ITER 10
int count;

void *Thread_func(void *data){
    int k;
    char* tname = (char*)data;
    count=0;
    for (k=0;k<MAX_ITER;k++){
        printf("In [%s] COUNT %d\n",tname,count);
        count++;
        sleep(1);
    }
}
int main(){
    pthread_t t1,t2;
    int status;
    pthread_create(&t1,NULL,Thread_func,(void *)"Thread1");
    pthread_create(&t2,NULL,Thread_func,(void *)"Thread2");
    pthread_join(t1,(void *)&status);
    pthread_join(t2,(void *)&status);
}

// In [Thread1] COUNT 0
// In [Thread2] COUNT 0
// In [Thread1] COUNT 2
// In [Thread2] COUNT 3
// In [Thread2] COUNT 4
// In [Thread1] COUNT 4
// In [Thread1] COUNT 6
// In [Thread2] COUNT 6
// In [Thread1] COUNT 8
// In [Thread2] COUNT 9
// In [Thread1] COUNT 10
// In [Thread2] COUNT 10
// In [Thread1] COUNT 12
// In [Thread2] COUNT 12
// In [Thread1] COUNT 14
// In [Thread2] COUNT 14
// In [Thread2] COUNT 16
// In [Thread1] COUNT 16
// In [Thread2] COUNT 18
// In [Thread1] COUNT 19
