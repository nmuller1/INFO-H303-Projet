import xml.etree.ElementTree as ET
from operator import methodcaller
output_file = "data.sql"
insert = ""

#Method should be used only in mecaniciens and registredUsers
def check_quote(word):
    result=False
    count=0
    while count < len(word) and result == False:
        if word[count]=="'":
            result=True
        else:
            count+=1
    return (result,count)
    

def new_word(word):
    if check_quote(word)==True:
        word==word_construct(word)
    return word

def word_construct(word):
    new_word=""
    count=0
    count1=check_quote(word)[1]
    while count<len(word):
        if count!=count1: 
            new_word+=word[count]
            count+=1
        else:
            new_word+="''"
            count+=1
    return new_word

tree = ET.parse('data2019/anonyme_users.xml')  
root = tree.getroot()
for elem in root:
    insert +="INSERT INTO user_ (id, pseudo,password, cardNum) VALUES "
    insert += "('"+elem[0].text+"','"+''+"','"+elem[1].text+"','"+elem[2].text+"')" + ";\n"

tree = ET.parse('data2019/mecaniciens.xml')  
root = tree.getroot()

for elem in root:

    insert +="INSERT INTO mechanic (id, lastname, firstname,password, phoneNum, road, roadNum, codePostal, commune, hireDate, cardNum) VALUES "
    insert += "('"+elem[0].text+"','"+elem[1].text+"','"+elem[2].text+"','"+elem[3].text+"','"+elem[4].text+"','"+elem[5][0].text+"','"+elem[5][1].text+"','"+elem[5][2].text+"','"+elem[5][3].text+"','"+elem[6].text+"','"+elem[7].text+"')" + ";\n"


tree = ET.parse('data2019/registeredUsers.xml')  
root = tree.getroot()

for elem in root:
    insert +="INSERT INTO user_ (id, pseudo,password, cardNum) VALUES "
    insert += "('"+elem[0].text+"','"+''+"','"+elem[3].text+"','"+elem[6].text+"')" + ";\n"
    riskElements=[elem[1].text,elem[2].text,elem[5][0].text,elem[5][2].text]
    noRiskElements=[]
    count=0
    while count<len(riskElements):
        if check_quote(riskElements[count])[0]==True:
            noRiskElements.append(word_construct(riskElements[count]))
        else:
            noRiskElements.append(riskElements[count])
        count+=1
    elem[1].text=noRiskElements[0]
    elem[2].text=noRiskElements[1]
    elem[5][0].text=noRiskElements[2]
    elem[5][2].text=noRiskElements[3]
    insert +="INSERT INTO CHARGER_USER (id,firstname,lastname,phoneNum,road,roadNum,codePostal,commune) VALUES "
    insert += "('"+elem[0].text+"','"+elem[2].text+"','"+elem[1].text+"','"+elem[4].text+"','"+elem[5][0].text+"','"+elem[5][1].text+"','"+elem[5][2].text+"','"+elem[5][3].text+"')" + ";\n"

whole_file=""
with open('data2019/reloads.csv', 'r') as f :
    whole_file=f.read()
dataList = whole_file.split("\n")[1:-1]

for elem in dataList:
    elem = elem.split(",")
    startTime = "to_timestamp('"+elem[8] +"', 'YYYY-MM-DD\"T\"HH24:MI:SS.ff3\"Z\"')"
    endTime = "to_timestamp('"+elem[9] +"', 'YYYY-MM-DD\"T\"HH24:MI:SS.ff3\"Z\"')"
    insert +="INSERT INTO reloads (scooter, user_id, initialLoad, finalLoad, sourceX, sourceY, destinationX, destinationY, startTime, endtime) VALUES "
    insert += "('"+elem[0]+"','"+elem[1]+"','"+elem[2]+"','"+elem[3]+"','"+elem[4]+"','"+elem[5]+"','"+elem[6]+"','"+elem[7]+"','"+startTime+"','"+endTime+"')" + ";\n"

whole_file=""
with open('data2019/reparations.csv', 'r') as f :
    whole_file=f.read()
dataList = whole_file.split("\n")[1:-1]

for elem in dataList:
    elem = elem.split(",")
    complainTime = "to_timestamp('"+elem[3] +"', 'YYYY-MM-DD\"T\"HH24:MI:SS.ff3\"Z\"')"
    repaireTime = "to_timestamp('"+elem[4] +"', 'YYYY-MM-DD\"T\"HH24:MI:SS.ff3\"Z\"')"
    insert +="INSERT INTO reparations (scooter, userID, mechanic, complainTime, repaireTime) VALUES "
    insert += "('"+elem[0]+"','"+elem[1]+"','"+elem[2]+"','"+elem[3]+"','"+elem[4]+"')" + ";\n"


whole_file=""
with open('data2019/scooters.csv', 'r') as f :
    whole_file=f.read()
dataList = whole_file.split("\n")[1:-1]

for elem in dataList:
    elem = elem.split(";")
    insert +="INSERT INTO scooters (numero, miseEnService, modele, plainte, charge) VALUES "
    insert += "('"+elem[0]+"','"+elem[1]+"','"+elem[2]+"','"+elem[3]+"','"+elem[4]+"')" + ";\n"

whole_file=""
with open('data2019/trips.csv', 'r') as f :
    whole_file=f.read()
dataList = whole_file.split("\n")[1:-1]

for elem in dataList:
    elem = elem.split(",")
    insert +="INSERT INTO trips (scooter, userID, sourceX, sourceY, destinationX, destinationY, startTime, endtime) VALUES "
    startTime = "to_timestamp('"+elem[6] +"', 'YYYY-MM-DD\"T\"HH24:MI:SS.ff3\"Z\"')"
    endTime = "to_timestamp('"+elem[7] +"', 'YYYY-MM-DD\"T\"HH24:MI:SS.ff3\"Z\"')"
    insert += "('"+elem[0]+"','"+elem[1]+"','"+elem[2]+"','"+elem[3]+"','"+elem[4]+"','"+elem[5]+"','"+startTime+"','"+endTime+"')" + ";\n"

with open(output_file, 'w') as f :
    f.write(insert)

