SRC = src/main.cpp src/log.cpp src/dispatcher.cpp
INC = inc/dispatcher.hpp inc/log.hpp
OBJ = build/main.o build/log.o build/dispatcher.o
NAME = dispatcher
CC = g++
CFLAGS = -Wall -Wextra -Werror -ggdb -O1 -pthread

all: build $(NAME)

build/%.o: src/%.cpp
	$(CC) $< $(CFLAGS) -c -o $@

build:
	if [ ! -d "build/" ]; then \
		mkdir build; \
	fi

$(NAME): $(OBJ) $(INC)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)

clean :
	rm -rf build/

fclean : clean
	rm -rf $(NAME)

re : fclean all

.SILENT: build fclean clean
