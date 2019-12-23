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
void run(char* pdevName, char* pfileRead, char* getMsgClient);
 
int server_fd, client_fd;

int main(int argc, char *argv[])
{
	pid_t pid = 0;

	pid = fork();
	if(pid > 0){
		char buffer[BUF_LEN];
		struct sockaddr_in server_addr, client_addr;
		char temp[20];
		//server_fd, client_fd : . .. ..
		int len, msg_size, i = 0;
		char fileRead[20] = {0,};

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
			run(buffer, fileRead, buffer);

			memset(buffer, 0, sizeof(buffer));
			printf("Server : %s client closed.\n", temp);
		}
		close(server_fd);
	} else {
		puts("fork sucess");
		system("python3 door.py");
	}

    return 0;
} 


void run(char* pdevName, char* pfileRead, char* getMsgClient){

	FILE* fp = NULL;
	int po = 0, i = 0, linePo = 0;
	char test1[20] = {'\0',};
	char test2[20] = {'\0',};
	char test3[20] = {'\0',};

	puts("==================== start run ===================");
	printf("devName: %s\n", pdevName);

	if(!strcmp(pdevName, "door1")){
		printf("devName - run : %s\n", pdevName);

		fp = fopen("devState.txt","rw");
		if(!fp){
			perror("file open error");
			fclose(fp);
		}

		fseek(fp, 0, SEEK_SET); // 파일 포인터 위치를 이동
		po = ftell(fp); 
		fgets(test1,sizeof(test1), fp);

		if(test1[10] == '0'){
			char val = '1';
			fwrite(&val,sizeof(val) ,1 ,fp);
		} else {
			printf("e - result : %d\n", test1[9]);
		}
		printf("test1 : %s file pointer : %d  ", test1, po);
		printf("getMsgClient : %s\n", getMsgClient);

		close(client_fd);
	} else if(strcmp(pdevName, "door2") == 0){
		system("LED/off");

		fp = fopen("devState.txt","rw");
		if(!fp){
			perror("file open error");
			fclose(fp);
		}

		printf("door2 buffer : %s\n", pdevName);
		fseek(fp, 9, SEEK_SET);
		po = ftell(fp);
		fgets(test2,sizeof(test2), fp);

		if(test2[9] == '1'){
			printf("i - result : %c\n", test2[9]);
		} else if(test2[9] == '0'){
			printf("ei - result숫자 : %d\n", test2[9]);
		} else {
			printf("e - result : %c\n", test2[9]);
		}
		printf("test2 : %s file pointer : %d  ", test2, po);
		printf("getMsgClient : %s\n", getMsgClient);

		close(client_fd);
	} else if(!strcmp(pdevName, "requestHome")){
		fp = fopen("devState.txt","r");
		if(!fp){
			perror("file open error");
			fclose(fp);
		}
		printf("request buffer : %s  ", pdevName);
		printf("getMsgClient : %s\n", getMsgClient);

		fseek(fp, 21, SEEK_SET);
		po = ftell(fp);
		fgets(test3,sizeof(test3), fp);
		printf("test3 : %s file pointer : %d\n", test3, po);
		close(client_fd);
	}
	puts(" =========================== ");

    memset(test1, '\0', sizeof(test1));
    memset(test2, '\0', sizeof(test2));
    memset(test3, '\0', sizeof(test3));
}

void rileRW(FILE* fp){
}



char* door1_Func(FILE* fp, int i, int bufferSize){

	if(fp == NULL){
		printf("FILE OPEN ERROR!");
		return "open error";
	}

	system("LED/on");
	fp = fopen("devState.txt","r");

	//printf("buffer state:%s",buffer);
//	close(client_fd);
	return NULL;
}


