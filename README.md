# Surrounding-element-of-Numpy-array
Get matrix of surrounding elements of Numpy array's element.
Here are some example on how code works.

Example:1

Input Numpy Array:\
0&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;4\
5&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;7&nbsp;&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;&nbsp;&nbsp;9\
10 11 12 13 14\
15 16 17 18 19\
20 21 22 23 24

Enter element row number: 2
Enter element column number: 3
Enter order of matrix: 3

Output Numpy Array:\
[7  8  9]\
[12 13 14]\
[17 18 19]\


Example:2

Input Numpy Array:\
[ 0  1  2  3  4]\
[ 5  6  7  8  9]\
[10 11 12 13 14]\
[15 16 17 18 19]\
[20 21 22 23 24]

Enter element row number: 0
Enter element column number: 4
Enter order of matrix: 5

Output Numpy Array:\
[ 0  0  0  0  0]\
[ 0  0  0  0  0]\
[ 2  3  4  0  0]\
[ 7  8  9  0  0]\
[12 13 14  0  0]
