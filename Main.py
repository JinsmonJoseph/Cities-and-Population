import csv
import matplotlib.pyplot as plt

csv_cityList=[["City","Population"]]
city=""
print("Enter the city names and corresponding population ")
print("-------------------------------------------")
while(city!="0"):
    temp=[]
    city=input("Enter the city name : (enter 0 to stop) : ")
    if(city!="0"):
        temp.append(city)
        population=input("Population : ")
        temp.append(population)
        csv_cityList.append(temp)
    else: break
with open ('Cities.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_cityList)
print("CSV File created..")
file.close()
citynames=[]
populations=[]
with open ('Cities.csv', 'r', newline='') as file:
    for line in file.readlines():
        row=line.split(",")
        citynames.append(row[0])
        populations.append(row[1])
file.close()
citynames=citynames[1:]
populations=populations[1:]
populations=[int(p) for p in populations]
plt.scatter(citynames,populations)
plt.xlabel("Cities")
plt.ylabel("population")
plt.show()
plt.bar(citynames, populations, color ='blue',width = 0.5)
plt.xlabel("Cities")
plt.ylabel("population")
plt.show()



    