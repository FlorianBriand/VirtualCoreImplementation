cmake_minimum_required(VERSION 3.24)
project(untitled1 C)

set(CMAKE_C_STANDARD 11)

add_executable(untitled1 core/main.c core/main.h core/decode.c core/decode.h core/fetch.c core/fetch.h core/execute.c core/execute.h)
