6 numbers are the input numbers used (which would have been chosen by the candidate) and 1
number is the target. The objective is to use the 6 numbers input and using only addition,
subtraction, multiplication or division, to generate the target or generate as close as possible to
either side of the target.

Each input number may only be used once. You can assume the target number and input
numbers will always be under 1024.

Write a program which takes 7 numbers as arguments. The first six numbers are the input
numbers described above with the 7th number being the target. The output of the program
should be a solution required to generate the target from those six numbers or the closest
possible solution either side of the target number.

Only one correct solution is required to be output, if multiple solutions are available.
e.g.

./program 1 2 3 4 5 6 12
2 * 6 = 12

./program 5 8 6 25 13 87 390
13 * 6 * 5 = 390