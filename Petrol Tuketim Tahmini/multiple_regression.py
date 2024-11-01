#kütüphaneleri içeri aktarma
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as seabornInstance
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import tkinter as tk

#veri okuma ve görüntüleme
veri=pd.read_csv(r"petrol_tüketimi.csv", encoding="ISO-8859-1")
veri.head()

#veri setinin boyutunu öğrenme
veri.shape

#tanımlayıcı istatistikler
pd.set_option("display.max_columns", None)
veri.describe()

#eksik veri kontrolü
veri.isnull()

#korelasyonlara bakalım
# plt.figure()
cor=veri.corr()
# sns.heatmap(cor)
# plt.show()

#scotter plot'lar (serpilme grafikleri)
sns.pairplot(veri)

#Hedef ve Öznitelikleri Tanımla
x=veri[['Petrol_vergi', 'Ortalama_gelir', 'Asvalt_Otoban', 'Ehliyet_orani']]
y=veri['Petrol_Tuketimi']



#öğrenme ve test verisi ayırımı
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=42)



#Eğititm ve model oluşturma
model=LinearRegression()
model.fit(x_train, y_train)

#modelin intercept ve coefficient'ını görme

print(f"Intercept:{model.intercept_}")
print(f"Coefficents{model.coef_}")

root=tk.Tk()
canvas1=tk.Canvas(root,width=400,height=400)
canvas1.pack(padx=10,pady=10)

label1=tk.Label(root,text="Petrol Vergi:")
canvas1.create_window(100,100,window=label1)
entry1=tk.Entry(root)
canvas1.create_window(200,100,window=entry1)

label2=tk.Label(root,text="Ortalama Gelir:")
canvas1.create_window(90,120,window=label2)
entry2=tk.Entry(root)
canvas1.create_window(200,120,window=entry2)

label3=tk.Label(root,text="Asvalt Otoban:")
canvas1.create_window(80,140,window=label3)
entry3=tk.Entry(root)
canvas1.create_window(200,140,window=entry3)

label4=tk.Label(root,text="Ehliyet Orani:")
canvas1.create_window(80,160,window=label4)
entry4=tk.Entry(root)
canvas1.create_window(200,160,window=entry4)


def values():
    global Petrol_Vergi
    Petrol_Vergi=float(entry1.get())
    global Ortalama_Gelir
    Ortalama_Gelir=float(entry2.get())
    global Asvalt_Otoban
    Asvalt_Otoban=float(entry3.get())
    global Ehliyet_Orani
    Ehliyet_Orani=float(entry4.get())
    Prediction_result=('Petrol Tuketimi(TL):',(model.predict([[Petrol_Vergi,Ortalama_Gelir,Asvalt_Otoban,Ehliyet_Orani]])) )
    label_prediction=tk.Label(root,text=Prediction_result,bg='lawngreen')
    canvas1.create_window(200,220,window=label_prediction)

button1=tk.Button(root,text="Hesapla",command=values,bg='orange')
canvas1.create_window(200,190,window=button1)
root.mainloop()
                       