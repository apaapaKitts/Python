# Assn 1, Python
# COSC 2P03 @ Brock University
# Author: Andrew Pauls
# Date: December 23, 2022


# variables

greeting = "This program simulates the operations of a medical clinic."
closing  = "A clinic session has finished. See you soon!"
global start
start = ""
global end
end = ""
patients = list(range(16))


class Patient:
    def __init__(self, Name, Gender, Age, Occupation, HealthConditions, TofA):
        self.Name = Name
        self.Gender = Gender
        self.Age = Age
        self.Occupation = Occupation
        self.HealthConditions = HealthConditions
        self.TofA = TofA
        self.PriorityScore =0

    def printPatient(self):
        print("Name: ", self.Name, " Gender: ", self.Gender, " Age: ", self.Age, " Occupation: ", self.Occupation, " Health Conditions: ", self.HealthConditions, " Time of Arrival: ", self.TofA, " Priority Score: ", self.PriorityScore)
        
                                        


class theTime:
    def __init__(self, hours, mins, stringRepresentation):
        self.hours = hours
        self.mins = mins
        self.stringRepresentation = stringRepresentation

    
    def displayTime(self):
        print(self.stringRepresentation)

    def incrementTime(self):
  
    ## update the mins
        if self.mins == 59:
            self.mins = 0
            self.hours+=1
        else:
            self.mins+=1

        # hours
        stringHrs = str(self.hours)
        # minutes
        if self.mins < 10:
            stringMins = "0" + str(self.mins)
        else:
            stringMins = str(self.mins)

        # synthesize the string        
        s = stringHrs+":"+stringMins
        self.stringRepresentation = s

    
def computeStringRepresentation(h, min):
    strHour = str(h)
    if (min<10):
        strMin = "0" + str(min)
    else:
        strMin=min
    strMin = str(strMin)
    strRep = strHour+":"+strMin
    return strRep

def add15Mins(theT):
    NextHours = 0
    NextMins = 0
    
    if ( theT.mins <45 ):
        NextMins = theT.mins + 15
        NextHours = theT.hours
    else:
        NextMins = (theT.mins+15)%60
        NextHours = theT.hours+1
    strR = computeStringRepresentation(NextHours, NextMins)
    FifteenMinsLater = theTime(NextHours, NextMins, strR)
    return FifteenMinsLater
    
   

def readData():
    # reads provided text file, inserts items into 'Patient' Objects
    import csv
    with open("patients.txt", "r") as file:
        line_reader = csv.reader(file, delimiter='\t')
        i = 0
        for line in line_reader:
            patient = Patient(line[0], line[1], line[2], line[3], line[4], line[5])
            patients[i] = patient
            i = i + 1
        computePriorities()
        

           
def monitorClinic():     # this method can't see the next appointment time.


    print('retard')
    global nextAppointmentTime
    nextAppointmentTime.displayTime()
    print("we are here")
    global currentTime
    global examRoomOccupied
    global q

    for i in range (0, 300):
        currentTime.incrementTime()
        currentTime.displayTime()

        # check for any patients who have just arrived, add them to the queue
        for Patient in patients:
            if(Patient.TofA == currentTime.stringRepresentation):           # what kind of comparison are we doing here...we need string rep
                if (q.empty()):
                    nextAppointmentTime = add15Mins(currentTime)
                    print(nextAppointmentTime.stringRepresentation)
                q.put(Patient.PriorityScore, Patient)
                Patient.printPatient()
        print("is queue empty? ", q.empty())

        # at the start of the method... everything is empty
        if (examRoomOccupied == False & q.empty()): print("nobody in exam room, nobody waiting to be seen")


        # handle appointments that may have just finished
        if ( nextAppointmentTime.stringRepresentation == currentTime.stringRepresentation ):
            
            if( q.empty() == False):
                examRoomOccupied = False
                nextAppointmentTime = add15Mins(currentTime)
                print('the examination has finished for: +++++++++')
                p = q.get()
                print("the next person is being summoned from the queue to go into the exam room:")
                print(p)
                examRoomOccupied = True
                
        
    
        # next possible scenario: exam room empty, priority queue not empty
        if (examRoomOccupied == False & (q.empty() == False)):
            print("hi")
            examRoomOccupied = True
            print('bi')
            nextAppointmentTime = add15Mins(currentTime)
            nextAppointmentTime.displayTime()
            print('ok') 
        #    print(p.Name, " entered the exam room at: ", currentTime.stringRepresentation, " and exits @: ", nextAppointmentTime.stringRepresenation)
        if (examRoomOccupied == False & (q.empty() == True)):
            print('no work to be done at the clinic')
    
def computePriorities():
    for Patient in patients:
        priorityScore = 0
        if(Patient.Age == "Age"): pass
        else:
            if (int(Patient.Age) >= 60): priorityScore-=1
        if(Patient.Occupation == "Care Giver"): priorityScore-=1
        if(Patient.Occupation == "Nurse"): priorityScore-=1
        if(Patient.Occupation == "Teacher"): priorityScore-=1
        if(Patient.HealthConditions != "None"): priorityScore-=1
        Patient.PriorityScore = priorityScore
        Patient.printPatient()
        

# main    
print(greeting)
start = "9:00"
end   = "3:00"

examRoomOccupied = False


from queue import PriorityQueue
q = PriorityQueue()

currentTime = theTime(8, 59, "8:59")
nextAppointmentTime = theTime(9, 15, "9:15")

readData()
monitorClinic()

print(closing)
