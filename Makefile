CC=gcc
CFLAGS=-c -Wall

all: main

main: main.o decode.o
	$(CC) main.o decode.o -o main

main.o: core/main.c core/main.h core/decode.h
	$(CC) $(CFLAGS) core/main.c

decode.o: core/decode.c core/decode.h
	$(CC) $(CFLAGS) core/decode.c

clean:
	rm -rf *o main

