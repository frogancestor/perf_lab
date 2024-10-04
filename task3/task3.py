import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("testsFilePath")
parser.add_argument("valuesFilePath")
parser.add_argument("reportsFilePath")
args = parser.parse_args()

with open(args.testsFilePath) as testsFile:
    tests = json.load(testsFile)

with open(args.valuesFilePath) as valuesFile:
    values = json.load(valuesFile)

testsArray = tests["tests"]
valuesArray = values["values"]


def recursion(testList, valueList):
    for test in testList:
        for value in valueList:
            if test["id"] == value["id"]:
                test["value"] = value["value"]
        values = test.get('values', [])
        if values:
            recursion(values, valueList)


recursion(testsArray, valuesArray)
print(tests)
with open(args.reportsFilePath, 'w') as reportFile:
    reportFile.write(json.dumps(tests))