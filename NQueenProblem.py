n = int(input())

ans = 0
row = [0] * n
row2 = [0] * n

print("The few arrangements are: ")

def print_queens():
    for i in range(n):
        for j in range(n):
            if row[i] == j:
                row2[j] = 1
        print(row2)
        for i in range(n):
            row2[i] = 0
    print('\n')

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        if(ans < 5):
            print_queens()
        return

    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print("Total possible arrangements: ",ans)