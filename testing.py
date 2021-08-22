import mysql.connector
import hashlib


mydb = mysql.connector.connect(host="115.146.85.12", user="bijay2", passwd="7482Rita", database="gid_sc")

mycursor = mydb.cursor()
mycursor.execute("SELECT gin_hash FROM gid_hash")
gid = mycursor.fetchall()
gid1 = [x[0] for x in gid]

myblood = mydb.cursor()
myblood.execute("SELECT bloodType FROM blood")
blood = myblood.fetchall()
blood1 = [y[0] for y in blood]

myeyes = mydb.cursor()
myeyes.execute("SELECT eyesColor FROM eyesColor")
eye = myeyes.fetchall()
eye1 = [z[0] for z in eye]

print("PLEASE ENTER THE VALUES IN LOWER CASE.")
print("PLEASE ENTER THE DATE IN 'YYYY-MM-DD' FORMAT: FOR EXAMPLE '1996-02-25'")
print("PLEASE PRESS 'ENTER' IF YOU DO NOT KNOW THE VALUE")
print("PLEASE press 'SPACE' IF THERE IS GAP BETWEEN TWO LETTERS: FOR EXAMPLE 'NORTH AMERICA'")
print("")

first_name = input("Please enter the victims first name: ")
sure_name = input("Please enter the victims sure name: ")
medical_number = input("Please enter the victims medical number: ")
gender = input("Please enter the victims gender: ")
father_name = input("Please enter the victims father name: ")
mother_name = input("Please enter the victims mother name: ")
mother_ethinicity = input("Please enter the victims mother ethnicity: ")
date_of_birth = input("Please enter the victims date of birth: ")
place_of_birth = input("Please enter the victims place of birth: ")
country_of_origin = input("Please enter the victims country of origin: ")
eyes_color = input("Please enter the victims eye color: ")
skin_color = input("Please enter the victims skin color: ")
ethnicity = input("Please enter the victims ethnicity: ")
blood_type = input("Please enter the victims blood type: ")
mother_tongue = input("Please enter the victims mother tongue: ")
religion = input("Please enter the victims religion: ")

counter = 0
for b in blood1:
    for e in eye1:
        final = medical_number + gender + first_name + sure_name + father_name + mother_name + mother_ethinicity + date_of_birth + place_of_birth + country_of_origin + str(e) + skin_color + ethnicity + str(b) + mother_tongue + religion
        #print("Generating a gid: " + final)
        hash_output = hashlib.sha256(final.encode('ascii')).hexdigest()
        #print(hash_output)
        #counter+= 1
        for hash in gid1:
            counter+= 1
            if (hash_output == hash):
                print("")
                print("Match Found")
                print("")
                print("The value was found after following number of trials: " + str(counter))
                print("")
                print("The Global Identifier is: " + hash_output)
                break

