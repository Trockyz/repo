def chessboard(n):
    for i in range(n):
        row = ''
        for j in range(n):
            
            if (i + j) % 2 == 0:
                row += '1'
            else:
                row += '0'
        print(row)
if __name__ == "__main__":
    chessboard(3)
    print()
    chessboard(6)
