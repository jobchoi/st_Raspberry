CC = gcc
CFAGS = -W -Wall
TARGET = server
OBJECTS = server.o

all : $(TARGET)

$(TARGET) : $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^            

server.o: socketServer.c
	$(CC) $(CFLAGS)	-c -o server.o socketServer.c

clean :
	rm *.o server
