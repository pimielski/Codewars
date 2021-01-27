def valid_solution(board):
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = 0
    
    for b in range(0, 9):
        if sorted_list == sorted(board[b]):
            a += 1
    
        list = []
        for c in range(0, 9):
            list.append(board[c][b])
            if sorted_list == sorted(list):
                a += 1
    
    for b in [0, 3, 6]:
        list_1 = []
        list_2 = []
        list_3 = []
        for c in range(0, 3):
            for d in range(0, 3):
                list_1.append(board[c+b][d])
            for d in range(3, 6):
                list_2.append(board[c+b][d])
            for d in range(6, 9):
                list_3.append(board[c+b][d])
        if sorted_list == sorted(list_1) and sorted_list == sorted(list_2) and sorted_list == sorted(list_3):
            a += 3
            
    return a == 27

solution = ([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]])

print(valid_solution(solution))