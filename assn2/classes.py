# assn 2, java to python conversion
# andrew Pauls
# december 24, 2022


# class file



# class1, BinaryNode


class BinaryNode:
    def __init__(self, Drug, leftChild, rightChild):
        self.Data = Drug
        self.leftC = leftChild
        self.rightC = rightChild

    def displayNode():
        print("Drug: ", self.Data.genericName)
        
# class2, Drug
class Drug:
    def __init__(self, genName, smiles, dbID, url, dGroups, score):
        self.drugBankID = dbID
        self.genericName = genName
        self.SMILES = smiles
        self.url = url
        self.drugGroups = dGroups
        self.score = score

    def displayDrug(self):
        print("Generic Name: ", self.genericName, " dbID: ", self.drugBankID, " score: ", self.score)

a1 = Drug("", "donkey","","","","") 

# class3, DrugBank
class DrugBank:

        ## constructor?
    def __init__(self, msg):
        print(msg)
        

        
        
    
        
        
    ## methods

    # 1. delete(string dbID)

    # 2. depth1(string dbID) --- prints int for depth of node being searched for

    # 3. readData()


    def readData(self):
        drugs = list(range(1933))
       
        

       
        # 1. get text file
        import csv
        with open("dockedApproved.tab", "r") as file:
            line_reader = csv.reader(file, delimiter = '\t')
            i = 0
            print('value of i', i)
            global a1
            for line in line_reader:
        
                a1 = (line[0], line[1], line[2], line[3], line[4], line[5])
                drugs[i] = a1
                i = i + 1
        file.close()
        for i in range(0, 1933):
            d = drugs[i]
            print(i, "th drug. ", d[0], " is gen name.")
            
  
    
    # 4. inOrderTraverse()

    # 5. insert(drug d)

    # 6. boolean search(String dbID)

    
