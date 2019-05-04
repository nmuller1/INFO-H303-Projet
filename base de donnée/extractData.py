import xml.etree.ElementTree as ET
output_file = "data.sql"


tree = ET.parse('data2019/anonyme_users.xml')  
root = tree.getroot()
insert = ""
for elem in root:
    insert +="INSERT INTO user_ (id, pseudo,password, cardNum) VALUES "
    insert += "('"+elem[0].text+"','"+''+"','"+elem[1].text+"','"+elem[2].text+"')" + ";\n"

tree = ET.parse('data2019/mecaniciens.xml')  
root = tree.getroot()

for elem in root:
    insert +="INSERT INTO charger_user (id, lastname, firstname,password, phoneNum, road, roadNum, codePostal, commune, hireDate, cardNum) VALUES "
    insert += "('"+elem[0].text+"','"+elem[1].text+"','"+elem[2].text+"','"+elem[3].text+"','"+elem[4].text+"','"+elem[5][0].text+"','"+elem[5][1].text+"','"+elem[5][2].text+"','"+elem[5][3].text+"','"+elem[6].text+"','"+elem[7].text+"')" + ";\n"


tree = ET.parse('data2019/registeredUsers.xml')  
root = tree.getroot()

for elem in root:
    insert +="INSERT INTO user_ (id, pseudo,password, cardNum) VALUES "
    insert += "('"+elem[0].text+"','"+''+"','"+elem[3].text+"','"+elem[6].text+"')" + ";\n"

    insert +="INSERT INTO user_ (id,firstname,lastname,phoneNum,road,roadNum,codePostal,commune) VALUES "
    insert += "('"+elem[0].text+"','"+elem[2].text+"','"+elem[1].text+"','"+elem[4].text+"','"+elem[5][0].text+"','"+elem[5][1].text+"','"+elem[5][2].text+"','"+elem[5][3].text+"')" + ";\n"
with open(output_file, 'w') as f :
    f.write(insert)
