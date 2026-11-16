# Laboratory 4 - Two-Dimensional Lists
B = [
    [8, 3, 6],
    [2, 9, 4],
    [7, 5, 1]
]

print("Matrix B:")
print(B)

print("Element in first row, second column:", B[0][1])

total = sum(sum(row) for row in B)
print("Total sum:", total)

main_diagonal = B[0][0] + B[1][1] + B[2][2]
print("Main diagonal sum:", main_diagonal)

secondary_diagonal = B[0][2] + B[1][1] + B[2][0]
print("Secondary diagonal sum:", secondary_diagonal)

print("Row sums:")
for i, row in enumerate(B, start=1):
    print(f"Row {i}:", sum(row))

print("Column sums:")
for j in range(3):
    print(f"Column {j + 1}:", sum(B[i][j] for i in range(3)))

numbers = [number for row in B for number in row]
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

even_count = sum(1 for number in numbers if number % 2 == 0)
odd_count = sum(1 for number in numbers if number % 2 != 0)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

print("Arithmetic mean:", total / 9)

print("Elements greater than 5:")
for row in B:
    for number in row:
        if number > 5:
            print(number)

above_diagonal = B[0][1] + B[0][2] + B[1][2]
print("Sum above the main diagonal:", above_diagonal)

below_diagonal = B[1][0] + B[2][0] + B[2][1]
print("Sum below the main diagonal:", below_diagonal)
