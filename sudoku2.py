def is_valid(grid, row, col, num):
    """
    (row, col) に num を置いてよいか判定する関数
    よい場合は True、置けない場合は False を返す
    """

    # 行のチェック
    for i in range(9):
        if grid[row][i] == num:
            return False

    # 列のチェック
    for i in range(9):
        if grid[i][col] == num:
            return False

    # 3×3 ブロックのチェック
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)

    for i in range(3):
        for j in range(3):
            if grid[start_row+i][start_col+j] == num: # here
                return False

    return True


def solve(grid):
    """
    数独を解く関数
    解が見つかった場合は True を返し、
    grid は解の状態に書き換わる。
    解が見つからない場合は False を返す。
    """

    for row in range(9):
        for col in range(9):

            # 空いているマスを見つける
            if grid[row][col] == 0:

                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        # from here
                        grid[row][col]=num
                        if solve(grid):
                            return True
                        else:
                            grid[row][col]=0
                        # to here

                              # num をそのマスに入れる
                              # 再帰的に探索し、
                              # 解が見つかったら True を返す
                              # 解が見つからなかった場合は元に戻す
                        
                # 1～9 のどの数字も入らなかった場合
                return False

    # すべてのマスが埋まった場合
    return True


# 盤面データ（問題で与えられている）
grid = [
    [0, 1, 0, 3, 0, 2, 0, 0, 7],
    [5, 0, 2, 0, 1, 0, 0, 6, 0],
    [0, 7, 0, 4, 0, 0, 5, 0, 0],
    [2, 0, 4, 0, 0, 3, 0, 0, 1],
    [0, 3, 0, 0, 2, 0, 0, 8, 0],
    [7, 0, 0, 1, 0, 0, 2, 0, 6],
    [0, 0, 3, 0, 0, 4, 0, 7, 0],
    [0, 4, 0, 0, 6, 0, 3, 0, 5],
    [1, 0, 0, 5, 0, 7, 0, 4, 0]
]


# プログラムの実行・解の表示
if solve(grid):
    for row in grid:
        print(row)
else:
    print("解が見つかりませんでした")