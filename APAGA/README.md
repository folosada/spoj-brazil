## DELETE - Erasing and Winning

Juliano is a fan of the Erasing and Winning Auditorium program, a program in which participants are selected through a draw and receive cash prizes for participating.

In the program, the presenter writes a number of N digits on a slate. The participant must then erase exactly D digits from the number on the board; The number formed by the remaining digits is then the participant's prize.

Juliano was finally selected to participate in the program, and asked you to write a program that, given the number the presenter wrote on the board, and how many digits Juliano has to erase, determines the value of the largest prize Juliano can win.

### Input
The input contains several test cases. The first line of each test case contains two integers N and D (1 <= D <N <= 10 ^ 5), indicating how many digits of the number the presenter wrote on the board and how many digits should be erased. The next line contains the number written by the presenter, which does not contain leading zeros.

The end of the entry is indicated by a line containing only two zeros, separated by a blank space.

### Output
For each input test case your program should print a single line on the output, containing the highest prize Juliano can win.

### Example

```
Input:
4 2                
3759               
6 3                
123123
7 4
1000000
0 0

Output:
79
323
100
```