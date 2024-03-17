import pickle
with open("TR_Model.pkl", "rb") as f:
  model=pickle.load(f)

a = int(input("Patient's Age\n=> "))
b = int(input("Gender : Male=0, Female=1\n=> "))
c = int(input("Type of Chest pain : (0-3)\n=> "))
d = int(input("Resting Blood Pressure : value in mmHg (94-200)\n=>"))
e = int(input("Cholestrol : value in mg/dl (126-564)\n=>"))
f = int(input("Fasting Blood sugar : value 0:<120mg/dl, 1:>120mg/dl\n=>"))
g = int(input("Resting ElectroCardioGraphy result : (0-1)\n=>"))
h = int(input("Maximum Heart Rate : (71-202)\n=>"))
i = int(input("Exercise included Agina : yes=1, No=0\n=>"))
j = float(input("Oldpeak value: ST depression from old peak (0.0-4.5)\n=>"))
k = int(input("Slope value: Slope of peak (0-2)\n=> "))
l = int(input("No. of Colored vessels : value (0-4)\n=> "))
m  = int(input("Thalassemia : Normal-1, Fixed defect-2, Reversable defect-3\n=>"))

input("\nPress ENTER to predict")

print("\nPrediction Result")
if model.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m]])[0] == 1:
  print("You have to take more care on your Heart health and visit your personal doctor as soon as possible..")

else:
  print("You have a Healthy Heart.. ")
