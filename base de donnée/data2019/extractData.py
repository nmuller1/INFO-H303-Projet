import xml.etree.ElementTree as ET


tree = ET.parse('anonyme_users.xml')  
root = tree.getroot()

for elem in root:
    print("id :" + elem[0].text)  
    print("password :" + elem[1].text) 
    print("bankaccount :" + elem[2].text)
    print("") 

tree = ET.parse('mecaniciens.xml')  
root = tree.getroot()

for elem in root:
    print("mechanicID :" + elem[0].text)  
    print("lastname :" + elem[1].text) 
    print("firstname :" + elem[2].text)
    print("password :" + elem[3].text)
    print("phone :" + elem[4].text)
    print("address, city :" + elem[5][0].text +", cp:" + elem[5][1].text +", street :"+ elem[5][2].text+", number :"+ elem[5][3].text)
    print("hireDate :" + elem[6].text)
    print("bankaccount :" + elem[7].text)
    print("")


tree = ET.parse('registeredUsers.xml')  
root = tree.getroot()

for elem in root:
    print("ID :" + elem[0].text)
    print("lastname :" + elem[1].text)
    print("firstname :" + elem[2].text)
    print("password :" + elem[3].text)
    print("phone :" + elem[4].text)
    print("address, city :" + elem[5][0].text +", cp:" + elem[5][1].text +", street :"+ elem[5][2].text+", number :"+ elem[5][3].text)
    print("bankaccount :" + elem[6].text)
    print("")


