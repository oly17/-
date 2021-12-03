import matplotlib.pyplot as plt

DnipryankaTO_activity=[2797552.00,1665429.00,2861819.00]
DnipryankaVD_activity=[231711.50,288496.70,553434.90]
DnipryankaRVD_activity=[8.30,17.30,19.30]
DnipryankaVOB_activity=[199979.40,201597.40,469761.10]
DnipryankaRVOB_activity=[7.20,12.10,16.40]
DnipryankaBPR_activity=[36778.70,91621.20,89377.60]
DnipryankaRRN_activity=[1.30,5.50,3.10]
Yniversam22TO_activity=[79280.50,486088.80,464588.00]
Yniversam22VD_activity=[6612.00,86523.80,91429.00]
Yniversam22RVD_activity=[8.35,17.80,19.68]
Yniversam22VOB_activity=[5026.40,35922.00,51211.00]
Yniversam22RVOB_activity=[6.35,7.39,11.02]
Yniversam22BPR_activity=[1815.50,32013.00,25584.00]
Yniversam22RRN_activity=[2.00,6.52,5.38]
year = ['basovuy','poperedniy','potochniy'] 

plt.plot(year,DnipryankaTO_activity,label="ДніпрянкаTO")
plt.plot(year,DnipryankaVD_activity,label="ДніпрянкаVD")
plt.plot(year,DnipryankaRVD_activity,label="ДніпрянкаRVD")
plt.plot(year,DnipryankaVOB_activity,label="ДніпрянкаVOB")
plt.plot(year,DnipryankaRVOB_activity,label="ДніпрянкаRVOB")
plt.plot(year,DnipryankaBPR_activity,label="ДніпрянкаBPR")
plt.plot(year,DnipryankaRRN_activity,label="ДніпрянкаRRN")
plt.plot(year,Yniversam22TO_activity,label="Універсам22TO")
plt.plot(year,Yniversam22VD_activity,label="Універсам22VD")
plt.plot(year,Yniversam22RVD_activity,label="Універсам22RVD")
plt.plot(year,Yniversam22VOB_activity,label="Універсам22VOB")
plt.plot(year,Yniversam22RVOB_activity,label="Універсам22RVOB")
plt.plot(year,Yniversam22BPR_activity,label="Універсам22BPR")
plt.plot(year,Yniversam22RRN_activity,label="Універсам22RRN")
plt.xlabel("Рік")
plt.ylabel("Діяльність")
plt.legend()
plt.grid(True)

def showplot():
    plt.show()

