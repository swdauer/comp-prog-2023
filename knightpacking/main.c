#include <stdio.h>
#define BOARD_DIMS 1000

char placeKnight(char board[BOARD_DIMS][]) {
    return 0;
}

int main() {
    int boardSize;
    char board[BOARD_DIMS][BOARD_DIMS] = {};
    char currPlayer = 1;

    scanf(" %d", &boardSize);

    while (1) {
        if (!placeKnight(board)) break;
        currPlayer != currPlayer;
    }
    if (currPlayer) printf("first\n");
    else printf("second\n");
    return 0;
}