from typing import List
import random
import sys


class Quick(object):
    def particao(self, a, ini, fim):
        pivo = a[fim-1]
        start = ini
        end = ini
        for i in range(ini, fim):
            if a[i] > pivo:
                end += 1
            else:
                end += 1
                start += 1
                a[i], a[start-1] = a[start-1], a[i]
        return start-1

    def quickSort(self, a, ini, fim):
        if ini < fim:
            pp = self.randparticao(a, ini, fim)
            self.quickSort(a, ini, pp)
            self.quickSort(a, pp+1, fim)
        return a

    def randparticao(self, a, ini, fim):
        rand = random.randrange(ini, fim)
        a[rand], a[fim-1] = a[fim-1], a[rand]
        return self.particao(a, ini, fim)


class Parameter:
    total_digits: int
    erased_digits: int
    digits: str


def readInput(inputParams: List[Parameter]):
    inputData = sys.stdin.readline().split()
    if (inputData[0] == '0' and inputData[1] == '0'):
        return inputParams
    parameter: Parameter = Parameter()
    parameter.total_digits = int(inputData[0])
    parameter.erased_digits = int(inputData[1])
    parameter.digits = sys.stdin.readline()
    parameter.digits = parameter.digits[0:parameter.total_digits]
    inputParams.append(parameter)
    readInput(inputParams)


inputParams: List[Parameter] = list()
readInput(inputParams)
sorter = Quick()
result: str = ''
for parameter in inputParams:
    orderedList = sorter.quickSort(
        list(parameter.digits), 0, parameter.total_digits)
    for index in range(0, parameter.erased_digits):
        parameter.digits = parameter.digits.replace(orderedList[index], '', 1)
    result += parameter.digits + '\n'
print(result)
