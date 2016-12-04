#-*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:38:23 2016

@author: Cosmin
"""
#f = open('../datasets/Crimes_-_2001_to_present.csv', 'a')

import random

def buildCrimeDegreeDictionary():
    cdd = {}
    cdd["ARSON"] = 32
    cdd["ASSAULT"] = 95
    cdd["BATTERY"] = 96
    cdd["BURGLARY"] = 51
    cdd["CONCEALED CARRY LICENSE VIOLATION"] = 52
    cdd["CRIM SEXUAL ASSAULT"] = 100
    cdd["CRIMINAL DAMAGE"] = 50
    cdd["CRIMINAL TRESPASS"] = 23
    cdd["DECEPTIVE PRACTICE"] = 25
    cdd["DOMESTIC VIOLENCE"] = 45
    cdd["GAMBLING"] = 17
    cdd["HOMICIDE"] = 99
    cdd["HUMAN TRAFFICKING"] = 100
    cdd["INTERFERENCE WITH PUBLIC OFFICER"] = 15
    cdd["INTIMIDATION"] = 63
    cdd["KIDNAPPING"] = 97
    cdd["LIQUOR LAW VIOLATION"] = 1
    cdd["MOTOR VEHICLE THEFT"] = 65
    cdd["NARCOTICS"] = 55
    cdd["NON - CRIMINAL"] = 3
    cdd["NON-CRIMINAL (SUBJECT SPECIFIED)"] = 3
    cdd["NON-CRIMINAL"] = 3
    cdd["OBSCENITY"] = 40
    cdd["OFFENSE INVOLVING CHILDREN"] = 93
    cdd["OTHER NARCOTIC VIOLATION"] = 21
    cdd["OTHER OFFENSE"] = 5
    cdd["PROSTITUTION"] = 35
    cdd["PUBLIC INDECENCY"] = 40
    cdd["PUBLIC PEACE VIOLATION"] = 18
    cdd["RITUALISM"] = 60
    cdd["ROBBERY"] = 58
    cdd["SEX OFFENSE"] = 75
    cdd["STALKING"] = 28
    cdd["THEFT"] = 70
    cdd["WEAPONS VIOLATION"] = 72
    return cdd

def generateCrime(cdd):
    crimes = []
    for crime in cdd.keys():
        crimes.append(crime)
    choicec = random.choice(crimes)
    return choicec

def generateLatitutde():
    num = random.randint(00000000,99999999)
    lst = ['6', '7', '8', '9']
    dig = random.choice(lst)
    lat = "41." + dig + str(num)
    return lat

def generateLongitude():
    num = random.randint(00000000,99999999)
    lst = ['4', '5', '6', '7']
    dig = random.choice(lst)
    lat = "-87." + dig + str(num)
    return lat
i = 0
lines = []
while i <= 10000000:
    crime = generateCrime(buildCrimeDegreeDictionary())
    latitude = generateLatitutde()
    longitude = generateLongitude()
    idd = "10956"
    CaseNum = "12419575"
    date = "12334/5135/6332"
    block = "124566"
    iucr = "3667"
    ptype = crime
    descr = "asfagag"
    locdescr = "adgadgfshg"
    arrest = "sdgsfh"
    domestic = "sdhfhgjd"
    beat = "dfhdfjgdj"
    district = "5"
    ward = "4"
    community = "38"
    FBI = "3asfasf"
    x = "3455662"
    y = "1341353564"
    year = "124152"
    updated = "1531/1351/161"
    lat = latitude
    long = longitude
    location = "qsfasfasgtqwtgqwgfqwr"
    l = idd + "," + CaseNum + "," + date + "," + block + "," + iucr + "," + ptype + "," + descr + "," + locdescr + "," + arrest + "," + domestic + "," + beat + "," + district + "," + ward + "," + community + "," + FBI + "," + x + "," + y + "," + year + "," + updated + "," + lat + "," + long + "," + location
    lines.append(l)
    if (i % 100000 == 0):
        f = open('../datasets/Crimes_-_2001_to_present_copia.csv', 'a')
        for line in lines:
            f.write(line + "\n")
        lines = []
    i += 1
f.close()
