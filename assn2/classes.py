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


# class3, DrugBank
class DrugBank:


    
        ## constructor?
    def __init__(self, msg):
        print(msg)
        self.drugs = list(range(1933))
        self.a1 = Drug("","","","","","")
        self.root = BinaryNode(None, None, None)
        
        
    ## methods

    # 1. delete(string dbID)

    # 2. depth1(string dbID) --- prints int for depth of node being searched for

    # 3. readData()
    def readData(self):
        
        # 1. get text file
        import csv
        with open("dockedApproved.tab", "r") as file:
            line_reader = csv.reader(file, delimiter = '\t')
            i = 0
            print('value of i', i)
            global a1
            global drugs
            for line in line_reader:
        
                self.a1 = Drug(line[0], line[1], line[2], line[3], line[4], line[5])
                self.drugs[i] = self.a1
                i = i + 1
        file.close()
    
            
  
    # 4. inOrderTraverse()
    def inOrderTraverse(self,subT):
        if( subT is None ):
            return
        else:
            self.inOrderTraverse(subT.leftC)
            print(subT.Data.genericName, ", ID:", subT.Data.drugBankID)
            self.inOrderTraverse(subT.rightC)
                        
    # 5. insert(drug d)
    def insertDrug(self,drug2insert):
        current = self.root

        ## check if we have an empty tree
        if (current.Data == None):
            self.root.Data = drug2insert

        ## else, tree not empty
        else:
            while (True):
                if(drug2insert.drugBankID < current.Data.drugBankID):
                    if (current.leftC == None):
                        current.leftC = BinaryNode(drug2insert, None,None)
                        return
                    else:
                        current = current.leftC

                else:
                    if(current.rightC == None):
                        current.rightC = BinaryNode(drug2insert, None,None)
                        return
                    else:
                        current = current.rightC

    def factoryInsert(self):
        # for loop, for each line in drugs, insert into the BST
        for i in range(1, 1933):
            self.insertDrug(self.drugs[i])

    # search(root, key)
    
    def search(self, dbID):
        current = self.root
        print(current.Data.drugBankID)
        
        while(current.Data.drugBankID != dbID):
            

            if(int(dbID[2:6])  <  int(current.Data.drugBankID[2:6])):
                current = current.leftC
            else:
                current = current.rightC

            ## print out the current value
            print(current.Data.drugBankID, " is currents dbID")
            
            if(current is None):
                print("not found")
                return None
        return current

    
        
 
    
