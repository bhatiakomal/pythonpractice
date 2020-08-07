sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
remove_Keys=['name','salary']
for x in remove_Keys:
    sampleDict.pop(x)
print(sampleDict)