## assn2 java --> python conversion

""" This is a learning experience. I have challenged myself to write my
2nd year Data Structures Course Assignments in python. Originally, the assignments
were written in java
"""


# december 24, 2022
# author, andrew pauls


# main class

## imports
from classes import DrugBank, Drug, BinaryNode




db = DrugBank()
db.readData()
db.factoryInsert()
db.inOrderTraverse(db.root)

print("searching for: DB01050")
drugFound2 = db.search('DB01050')
print(drugFound2.Data.drugBankID, ' was found')


db.delete(db.root, 'DB01065')

