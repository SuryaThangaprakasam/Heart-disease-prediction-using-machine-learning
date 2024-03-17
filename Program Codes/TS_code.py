import pickle
with open("TR_Model.pkl", "rb") as f:
  model=pickle.load(f)

a = int(input("Enter Value Of Age : "))
b = int(input("Enter Gender : "))
c = int(input("Enter Cp : "))
d = int(input("Enter Value Of trestbps : "))
e = int(input("Enter chol : "))
f = int(input("Enter fbs : "))
g = int(input("Enter Value Of restecg : "))
h = int(input("Enter thalach : "))
i = int(input("Enter exang : "))
j = float(input("Enter Value Of oldpeak : "))
k = int(input("Enter slope : "))
l = int(input("Enter ca : "))
m  = int(input("Enter thal :"))

if model.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m]])[0] == 1:
  print("Affected")

else:
  print("Not Affected")
