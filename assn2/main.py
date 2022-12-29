## assn2 java --> python conversion
# december 24, 2022
# author, andrew pauls


# main class

## imports
from classes import DrugBank, Drug, BinaryNode



## instantiate what needs to be instantiated

db = DrugBank("hello")

## run what needs to be ran
db.readData()


## now lets add every single drug to the thing
db.factoryInsert()


## search for: DB14646
print("searching for: DB09394")
drugFound = db.search('DB09394')
print(drugFound.Data.drugBankID, ' was found')

print("searching for: DB08905")
drugFound2 = db.search('DB08905')
print(drugFound2.Data.drugBankID, ' was found')

print("searching for: DB13628")
drugFound3 = db.search('DB13628')
print(drugFound3.Data.drugBankID, ' was found')


print("searching for: DB00765")
drugFound4 = db.search('DB00765')
print(drugFound4.Data.drugBankID, ' was found')
