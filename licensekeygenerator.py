import random

class LicenseKey:
    partLength = 0 #The length of each part, Defaults to 5
    partAmount = 0 #The amount of parts, Defaults to 5
    divider = '' #The string that divides parts, Defaults to "-"

    def __init__(
        self,pLength=5,pAmount=5,div='-'): #Set values
        self.partLength = pLength
        self.partAmount = pAmount
        self.divider = div

    def generateKey(self):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" #Example character set, can be changed
        key = "" #Key to return
        
        for part in range(self.partAmount): #Loops partAmount times
            for onePart in range(self.partLength): #Loops partLength times
                key += random.choice(characters) #Adds random character from the characters string to key

            if (part != self.partAmount-1): #If it isnt the last part
                key += self.divider #Add a divider to the key
        return key

"""

Example Usage:

key = LicenseKey()
keyValue = key.generateKey()
print(keyValue)

>>Emgvk-Zpbbt-vLH4W-PbN9j-GYNjb



Customised Usage:

key = LicenseKey()
keyValue = key.generateKey(3,8,"--")
print(keyValue)

>>Emg--Zpb--vLH--PbN--GYN--bBt--6Sd--2bV

"""