CC=gcc
CFLAGS=-c -Wall

all: main

main: main.o decode.o execute.o fetch.o
	$(CC) main.o decode.o execute.o fetch.o -o main -lm
main.o: core/main.c core/main.h core/decode.h
	$(CC) $(CFLAGS) core/main.c

decode.o: core/decode.c core/decode.h
	$(CC) $(CFLAGS) core/decode.c

execute.o: core/execute.c core/execute.h
	$(CC) $(CFLAGS) core/execute.c

fetch.o: core/fetch.c core/fetch.h
	$(CC) $(CFLAGS) core/fetch.c

clean:
	rm -rf *o main

