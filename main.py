def printBaord():
    print(f"0 | 1 | 2 ")
    print(f"..|...|...")
    print(f"3 | 4 | 5 ")
    print(f"..|...|...")
    print(f"6 | 7 | 8 ")


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for x and 0 for o
    print("Welcome to Tic Tac Toe")
    print('Xs chance')
    printBaord()
