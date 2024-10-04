import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arrayOfNumbers")
args = parser.parse_args()

with open(args.arrayOfNumbers, 'r') as file:
    arrayOfNumbers = file.read().split(' ')
    arrayOfNumbers = [int(number) for number in arrayOfNumbers]


def minimalCount(arrayOfNumbers):
    arrayOfNumbers.sort()
    mediana = arrayOfNumbers[len(arrayOfNumbers) // 2]
    minimum = sum(abs(number - mediana) for number in arrayOfNumbers)
    return minimum


print("Минимальное количество ходов: ", minimalCount(arrayOfNumbers))