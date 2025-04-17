"""
A. Trippi Troppi

Trippi Troppi resides in a strange world. The ancient name of each country consists of three strings. The first letter of each string is concatenated to form the country's modern name.

Given the country's ancient name, please output the modern name.

Input
The first line contains an integer 𝑡
 – the number of independent test cases (1≤𝑡≤100
).

The following 𝑡
 lines each contain three space-separated strings. Each string has a length of no more than 10
, and contains only lowercase Latin characters.

Output
For each test case, output the string formed by concatenating the first letter of each word.

Example
Input
7
united states america
oh my god
i cant lie
binary indexed tree
believe in yourself
skibidi slay sigma
god bless america

Output
usa
omg
icl
bit
biy
sss
gba


"""

n = int(input())
for i in range(n):
    C_name = input()
    NameList = [x[0] for x in C_name.split()]
    print("".join(NameList))