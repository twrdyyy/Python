#!/usr/bin/env python

import sys
import time
import random


# Implementacja gry w zycie w konsoli. Dla ciekawskich: https://pl.wikipedia.org/wiki/Gra_w_%C5%BCycie
# Spojrz do glownej funkcji programu i wykonuj poszczegolne etapy.
# Do poprawnego wykonania kazdego z etapow wymagane jest zaimplementowanie odpowiednich funkcji (oznaczone jako Zadanie N)
# Plansza powinna byc przechowywana w zmiennej zawierajacej tablice dwuwymiarowa (lista list)


# Dlugosc boku planszy
#   18 to minimum aby pentadecathlon i pulsar dzialaly poprawnie
#   50 to minimum aby glider-gun dziaal poprawnie
BOARD_SIZE = 70
# Ile komorek powinno zostac wylosowanych przy losowaniu planszy
RANDOMIZATION_SIZE = int(BOARD_SIZE * BOARD_SIZE * 0.4)

# Ile rund maksymalnie ma byc obliczonych
MAX_ROUNDS = 500
# Co ile czasu nastepuje kolejna runda (w sekundach)
ROUND_INTERVAL = 0.1

# Znak oznaczajacy zywa komorke
ALIVE_CELL_CHAR = '*'
# Znak oznaczajacy martwa komorke
DEAD_CELL_CHAR = ' '

# Znak oznaczajacy zywa komorke w pliku wejsciowym
ALIVE_CELL_CHAR_FROM_FILE = '*'

# Znak oznaczajacy martwa komorke w pliku wejsciowym
DEAD_CELL_CHAR_FROM_FILE = '-'

# Przy jakiej liczbie sasiadow zywa komorka przezyje
CELL_SURVIVES = [2, 3]
# Przy jakiej liczbie sasiadow martwa komorka ozyje
CELL_COMES_ALIVE = [3]


# TODO Zadanie 1
# Tworzy PUSTA plansze (bez zywych komorek)
# Zwraca plansze
def create_board():
    x = []
    for j in range(BOARD_SIZE):
        x.append([])
        for i in range(BOARD_SIZE):
            x[j].append(False)
    # TODO plansza powinna byc kwadratem o boku BOARD_SIZE
    # TODO martwa komorka oznaczana jest False
    return x


# TODO Zadanie 2
# Wypisuje plansze board na ekran
# Plansza 4x4 ze znakami '*' dla zywych i ' ' dla martwych komorek powinna wygladac tak
#   (uzyj znakow '-' '|' '#' do ramki planszy):
#
#         #----#
#         |  * |
#         |**  |
#         |    |
#         |  * |
#         #----#
#
def print_board(board):
    # TODO uzyc znakow ALIVE_CELL_CHAR i DEAD_CELL_CHAR do zaznaczenia martwych/zywych komorek
    # TODO przydatna funkcja to
    #       sys.stdout.write(string)
    # ktora wypisuje zadany ciag bez znaku konca linii.
    # Nalezy pamietac, aby wywolac sys.stdout.flush(), zeby znaki zostaly wypisane na konsole
    # (wypisze wszystko co zostalo zgromadzone od ostatniego flush)
    sys.stdout.write('#')
    for j in range(BOARD_SIZE):
        sys.stdout.write('-')
    sys.stdout.write('#')
    sys.stdout.write('\n')
    for j in range(BOARD_SIZE):
        sys.stdout.write('|')
        for i in range(BOARD_SIZE):
            if board[j][i]:
                sys.stdout.write(ALIVE_CELL_CHAR)
            else:
                sys.stdout.write(DEAD_CELL_CHAR)
        sys.stdout.write('|')
        sys.stdout.write('\n')

    sys.stdout.write('#')
    for j in range(BOARD_SIZE):
        sys.stdout.write('-')
    sys.stdout.write('#')
    sys.stdout.write('\n')

    sys.stdout.flush()

# TODO Zadanie 3
# Losuje stan poczatkowy planszy
# Wartosc zwracana nie jest istotna, plansza board powinna byc zmodyfikowana przez te funkcje
def randomize_board(board):
    # TODO nalezy wylosowac zywe komorki i zanaczyc je w board
    # TODO losowanie jednej komorki nalezy powtorzyc RANDOMIZATION_SIZE razy
    for i in range(RANDOMIZATION_SIZE):
        x = random.randint(0, BOARD_SIZE-1)
        y = random.randint(0, BOARD_SIZE-1)
        board[x][y] = True


# TODO Zadanie 4
# Liczy sasiadow komorki o wspolrzednych (x, y) na planszy board
# Zwraca wyliczona liczbe sasiadow
def count_neighbours(board, x, y):
    # TODO uwaga na warunki brzegowe!
    z = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            if i < 0 or j < 0 or i >= BOARD_SIZE or j >= BOARD_SIZE:
                continue
            if board[i][j]:
                z += 1
    return z

# TODO Zadanie 5
# Wylicza jedna runde Gry w Zycie
# Zwraca NOWA plansze board na podstawie starej, podanej przez argument
def live(board):
    plansza = create_board()
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            x = count_neighbours(board,i,j)
            if x in CELL_COMES_ALIVE and not board[i][j]:
                plansza[i][j] = True
            if x in CELL_SURVIVES and board[i][j]:
                plansza[i][j] = True

    # TODO czy mozemy aktualizowac te sama plansze w ktorej liczymy sasiadow?
    # TODO uzyc CELL_SURVIVES dla zywych komorek zeby stwierdzic czy przezyly
    # TODO uzyc CELL_COMES_ALIVE dla martwych komorek zeby stwierdzic czy ozyly
    return plansza


# TODO Zadanie 6
# Wczytuje stan poczatkowy z pliku do danej planszy
# 1) jesli plansza w pliku jest mniejsza od board, wczytuje od lewego gornego naroznika
# 2) jesli plansza w pliku jest wieksza od board, wczytuje tylko to co sie miesci
# Wartosc zwracana nie jest istotna, plansza board powinna byc zmodyfikowana przez te funkcje
def import_board_from_file(board, file_path):
    # TODO nalezy uzyc ALIVE_CELL_CHAR_FROM_FILE i/lub DEAD_CELL_CHAR_FROM_FILE
    file = open(file_path)
    x = 0
    y = 0
    for i in file:
        if y >= BOARD_SIZE:
            break
        for j in i:
            if x >= BOARD_SIZE:
                break
            if j == ALIVE_CELL_CHAR_FROM_FILE:
                board[y][x] = True
            x += 1
        y += 1
        x = 0


# Glowna funkcja programu
if __name__ == '__main__':
    # TODO etap 1) Stworz pusta plansze i wypisz ja na ekran (zad 1+2)
    board = create_board()
    if len(sys.argv) > 1:
        import_board_from_file(board, sys.argv[1])
    else:
        randomize_board(board)
    print_board(board)

    for i in range(MAX_ROUNDS):
        print("\n\n\n")
        print("Runda: " + str(i))
        print_board(board)
        board = live(board)
        time.sleep(ROUND_INTERVAL)

    # TODO etap 2) Stworz plansze, wylosuj jej stan poczatkowy, wypisz na ekran (zad 3)

    # TODO etap 3) Stworz plansze, wylosuj jej stan poczatkowy, nastepnie w petli: (zad 4+5)
    #                           wypisz kilka pustych linii, aby bylo czytelniej
    #                           wypisz numer rundy (np. 'RUNDA: 13')
    #                           wypisz plansze
    #                           wylicz kolejna runde i zaktualizuj plansze
    #                           poczekaj chwile ( time.sleep(ilosc_sekund) )
    #                           powtorz
    # TODO          uzyj MAX_ROUNDS aby ograniczyc ilosc rund symulacji
    # TODO          uzyj ROUND_INTERVAL aby okreslic ile czasu czekac miedzy rundami

    # TODO etap 4) Dopisz obsluge przerwania Ctrl+C, ktore wypisze 'Koniec!' i zakonczy program

    # TODO etap 5) Dopisz mozliwosc importu z pliku (zad 6)
    # TODO           jesli podamy nazwe pliku jako argument, wczytujemy z pliku
    # TODO           jesli nic nie podamy, losujemy plansze