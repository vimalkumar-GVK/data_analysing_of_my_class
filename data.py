import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data ={
    "ID":['RACS2024BIT001','RACS2024BIT002','RACS2024BIT004','RACS2024BIT005',
          'RACS2024BIT006','RACS2024BIT007','RACS2024BIT010','RACS2024BIT011',
          'RACS2024BIT012','RACS2024BIT013','RACS2024BIT014','RACS2024BIT016',
          'RACS2024BIT017','RACS2024BIT018','RACS2024BIT019','RACS2024BIT020',
          'RACS2024BIT021','RACS2024BIT022','RACS2024BIT023','RACS2024BIT024',
          'RACS2024BIT025','RACS2024BIT026','RACS2024BIT027','RACS2024BIT028',
          'RACS2024BIT029','RACS2024BIT030','RACS2024BIT031','RACS2024BIT032',
          'RACS2024BIT033','RACS2024BIT034','RACS2024BIT035','RACS2024BIT036',
          'RACS2024BIT038','RACS2024BIT040','RACS2024BIT041','RACS2024BIT042',
          'RACS2024BIT043','RACS2024BIT044','RACS2024BIT045','RACS2024BIT046',
          'RACS2024BIT048','RACS2024BIT049','RACS2024BIT050','RACS2024BIT051',
          'RACS2024BIT052','RACS2024BIT053','RACS2024BIT054','RACS2024BIT056',
          'RACS2024BIT057','RCAS2024BIT901'],
    "NAME":['Punith.B','Murali krishnan','Ajay venkatesh','Mohan Raj',
            'Madhavan','Samuthra','Vignesh','Adithya','Musa Mustafa Elhaj Elamin',
             'Harini','Gowtham sri','Bharathi','Santhosh','Sabarivel','Monith','Lokesh karthick',
             'Vishnu','Sharmila','Vishal','Rajakumaran','Naveen','Mukilan','Muneeshwaran'
             ,'Suvetha','Antony Jesu  Allwin','Sanjay','Thivin kumar','Lavanya gowri',
             'Keerthana','Jaishree','Mohamed Arsath','Naren Aravind','Anshad','Gokilam',
             'Navaneethan','Saran sri','Mathivanan','Kishore','Yousf','Paramesh',
             'Vimal Kumar','Syed Abudahir','Mohammed Tarik','Karan','Girinath','Mohammed Raneesh',
             'Mohammed Altaf','Sheriff Ezz El-Din','Ahmed Aasin Babiker Elzubair','Mohammed zain'],
    "Tamil":[87, 45, 92, 61, 74, 38, 99, 56, 81, 27,
         68, 95, 43, 77, 52, 89, 34, 71, 100, 58,
         24, 83, 47, 90, 63, 76, 41, 85, 29, 72,
         54, 97, 36, 79, 66, 88, 22, 73, 49, 94,
         80, 57, 31, 69, 96, 44, 75, 53, 91, 62],
    "English":[78, 55, 89, 42, 97, 64, 31, 86, 73,
     50, 92, 27, 81, 46, 99, 58, 35, 74, 88, 23, 67, 
     95, 40, 79, 52, 84, 29, 91, 61, 38, 100, 71, 44,
      87, 56, 25, 93, 69, 48, 82, 33, 76, 59, 98, 
      41, 85, 62, 30, 90, 54],
      "Maths":[65, 88, 47, 93, 28, 76, 54, 81, 39, 97, 
      62, 45, 84, 31, 90, 58, 72, 24, 99, 67, 41, 86, 53
      , 79, 36, 95, 60, 43, 82, 27, 91, 55, 74, 33, 100,
       69, 48, 87, 25, 77, 52, 94, 38, 83, 61, 29, 89, 57, 71, 44],
       "ML":[54, 97, 36, 79, 66, 88, 22, 73, 49, 94,
         80, 57, 31, 69, 96, 44, 75, 53, 91, 62,
        24, 83, 47, 90, 63, 76, 41, 15, 29, 72,
        87, 45, 92, 61, 74, 38, 99, 56, 81, 27,
        68, 95, 43, 77, 52, 89, 34, 71, 110, 58,]
}
df = pd.DataFrame(data)
print(df)
df.to_excel("student.xlsx",index=True)
print("File is created")
# print(df)
df["Total"]=df[["Tamil","English","Maths","ML"]].sum(axis=1)
df["Average"]=df[["Tamil","English","Maths","ML"]].mean(axis=1)
df["median"]=df["Total"].median()
subjects = ["Tamil", "English", "Maths", "ML"]

x = np.arange(len(df))  # Student positions
width = 0.2

plt.figure(figsize=(15, 8))

plt.bar(x - 1.5*width, df["Tamil"], width, label="Tamil")
plt.bar(x - 0.5*width, df["English"], width, label="English")
plt.bar(x + 0.5*width, df["Maths"], width, label="Maths")
plt.bar(x + 1.5*width, df["ML"], width, label="ML")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of All Students by Subject")

plt.xticks(x, df["NAME"], rotation=80)
plt.legend()

plt.tight_layout()
plt.show()
#overall total student performace 
plt.figure(figsize=(15,8))
plt.bar(df["NAME"],df["Total"])
plt.title("Total Marks chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation = 90)
plt.tight_layout()
plt.show()
#student performance based on the particular student


student = df.loc[df["NAME"] == "Vimal Kumar", subjects].iloc[0]

plt.figure(figsize=(15, 9))
plt.plot(subjects, student.values, marker='o')
plt.title("Particular Student Performance")
plt.xlabel("Subjects")
plt.ylabel("Marks of Vimal")
plt.grid(True)
plt.show()

#editing the xlse file
df=pd.read_excel("student.xlsx")
df.loc[df["NAME"]=="Punith.B","ID"]="BIT001"
df.to_excel("student.xlsx",index=False)
print("The xlsx file is edited")
print(df.head())
