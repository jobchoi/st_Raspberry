#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "time.h"
#include "sys/types.h"
#include "sys/socket.h"
#include "netinet/in.h"
//.. ...... ... .... ..
 
#define BUF_LEN 128
//#define BUF_LEN 1024
//... .... ... .. ... ..

char* door1_Func(FILE* fp, int i, int bufferSize);
void run(char* getMsgClient);
 
int server_fd, client_fd;


int door1 = 0;
int door2 = 0;
int led = 0;

bool jobFlag = true;
bool jobrock = true;

int main(int argc, char *argv[])
{
	pid_t pid = 0;
	FILE* fpdoor1 = NULL;
	FILE* fpdoor2 = NULL;
	FILE* fpled = NULL;

	pid = fork();
	if(pid > 0){
		char buffer[BUF_LEN];
		char buffer1[BUF_LEN];
		struct sockaddr_in server_addr, client_addr;
		char temp[20];
		char door1Buffer[20] = {'\0',};
		char door2Buffer[20] = {'\0',};
		char ledBuffer[20] = {'\0',};

		int len=0, msg_size=0;
		char fileRead[20] = {0,};
		int po = 0, i = 0, linePo = 0;

		if(argc != 2)
		{
			printf("usage : %s [port]\n", argv[0]);
			exit(0);
		}
	 
		if((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
		{// .. ..
			printf("Server : Can't open stream socket\n");
			exit(0);
		}
		memset(&server_addr, 0x00, sizeof(server_addr));
		//server_Addr . NULL. ...
	 
		server_addr.sin_family = AF_INET;
		server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
		server_addr.sin_port = htons(atoi(argv[1]));
		//server_addr ..
	 
		if(bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) <0)
		{//bind() ..
			printf("Server : Can't bind local address.\n");
			exit(0);
		}
	 
		if(listen(server_fd, 5) < 0)
		{//... .. ..... ..
			printf("Server : Can't listening connect.\n");
			exit(0);
		}
	 
		memset(buffer, 0x00, sizeof(buffer));
		printf("Server : wating connection request.\n");
		len = sizeof(client_addr);

		puts("server start");

		fpdoor1 = fopen("door1state.txt","r+");
		fpdoor2 = fopen("door2state.txt","r+");
		fpled = fopen("ledstate.txt","r+");

		if(fpdoor1 == NULL){
			printf("FILE door1 OPEN ERROR!");
			return "open error";
		}
		if(fpdoor2 == NULL){
			printf("FILE door2 OPEN ERROR!");
			return "open error";
		}
		if(fpled == NULL){
			printf("FILE led OPEN ERROR!");
			return "open error";
		}

		fseek(fpdoor1, 0, SEEK_SET); // 파일 포인터 위치를 이동
		fseek(fpdoor2, 0, SEEK_SET); // 파일 포인터 위치를 이동
		fseek(fpled, 0, SEEK_SET); // 파일 포인터 위치를 이동

		fgets(door1Buffer, sizeof(door1Buffer), fpdoor1);
		fgets(door2Buffer, sizeof(door2Buffer), fpdoor2);
		fgets(ledBuffer, sizeof(ledBuffer), fpled);

		door1 = door1Buffer[6];
		door2 = door2Buffer[6];
		led = ledBuffer[6];

		printf("버퍼 확인 1: %s\n값확인 : %c\n", door1Buffer, door1);
		printf("버퍼 확인 2: %s\n값확인 : %c\n", door2Buffer, door2);
		printf("버퍼 확인 3: %s\n값확인 : %c\n", ledBuffer, led);

		while(1)
		{
			client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &len);
			if(client_fd < 0)
			{
				printf("Server: accept failed.\n");
				exit(0);
			}
			inet_ntop(AF_INET, &client_addr.sin_addr.s_addr, temp, sizeof(temp));

			printf("Server : %s client connected.\n", temp);
		
			msg_size = read(client_fd, buffer, 1024);
			write(client_fd, buffer, msg_size);
			printf("read buffer : %s\n" ,buffer);
			run(buffer);

			printf("Server : %s client closed.\n", temp);
			memset(buffer, 0, sizeof(buffer));
		}
		close(server_fd);
	} else {
		puts("fork sucess");
		system("python3 door.py");

		if(jobFlag){

		}
			
	}

    return 0;
} 


void run(char* getMsgClient){
	puts("==================== start run ===================");
	printf("getMsgClient : %s\n", getMsgClient);

	if(strcmp(getMsgClient, "request_and_door1")){
		printf("if - %s\n",getMsgClient);
	} else {
		printf("else - %s\n",getMsgClient);
	}

	close(client_fd);
}



char* door1_Func(FILE* fp, int i, int bufferSize){

	if(fp == NULL){
		printf("FILE OPEN ERROR!");
		return "open error";
	}

	system("LED/on");

	//printf("buffer state:%s",buffer);
//	close(client_fd);
	return NULL;
}


