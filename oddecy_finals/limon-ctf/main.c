#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_NOTES 20

char *notes[MAX_NOTES];
int sizes[MAX_NOTES];

void setup() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int get_int() {
    char buf[16];
    read(0, buf, 15);
    return atoi(buf);
}

void allocate() {
    printf("Index (0-%d): ", MAX_NOTES - 1);
    int idx = get_int();
    if (idx < 0 || idx >= MAX_NOTES || notes[idx]) {
        puts("Invalid index");
        return;
    }

    printf("Size: ");
    int size = get_int();
    
    if (size <= 0 || size > 0x1000) {
        puts("Invalid size");
        return;
    }
    notes[idx] = malloc(size);
    sizes[idx] = size;
}

void edit() {
    printf("Index (0-%d): ", MAX_NOTES - 1);
    int idx = get_int();
    if (idx < 0 || idx >= MAX_NOTES || !notes[idx]) {
        puts("Invalid index or empty note");
        return;
    }

    printf("Data: ");
    gets(notes[idx]);
    puts("Done.");
}

void show() {
    printf("Index (0-%d): ", MAX_NOTES - 1);
    int idx = get_int();
    if (idx < 0 || idx >= MAX_NOTES || !notes[idx]) {
        puts("Invalid index or empty note");
        return;
    }

    printf("Content: ");
    write(1, notes[idx], sizes[idx]);
    puts("");
}

void menu() {
    puts("1. Allocate");
    puts("2. Edit");
    puts("3. Read");
    printf("> ");
}

int main() {
    setup();
    
    while(1) {
        menu();
        int choice = get_int();
        
        switch(choice) {
            case 1: allocate(); break;
            case 2: edit(); break;
            case 3: show(); break;
            default: return;
        }
    }
}
