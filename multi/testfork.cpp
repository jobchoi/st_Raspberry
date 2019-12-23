#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

void fork0();
void fork1();

int main(int argc, char* argv[]){
	pid_t pid;

	pid = fork();
	if(pid > 0 )
		printf("process1 : %d , process2 : %d \n",getpid(), pid);
	while(1){
		if(pid > 0 ){
			sleep(3);
			fork0();

		} else if(pid == 0){
			sleep(3);
			fork1();
		} else if(pid == -1){
			perror("fork error");
			exit(0);
		}
	}
	return 0;
}


void fork0(){
	system("../LED/on");
}

void fork1(){
	system("../LED/off");
}
