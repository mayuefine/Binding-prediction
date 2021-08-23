#! /usr/bin/python3

# sklearn version = 0.22.2

import numpy as np
from sklearn.externals import joblib

forld = "./"
model_name = np.loadtxt("models_name.txt", dtype=str)
mn = list(model_name)
P_20 = np.loadtxt(forld+"20/seq_20fet_values.csv", delimiter = ",")
P20 = P_20[:, 0:20]
P_24 = np.loadtxt(forld+"24/seq_24fet_values.csv", delimiter = ",")
P24 = P_24[:, 0:24]
P_117 = np.loadtxt(forld+"117/seq_117fet_values.csv", delimiter = ",")
P117 = P_117[:, 0:117]

def prediction(P, n, nu):
    svm = joblib.load("./" + str(int(nu)) + "/ml/svm_" + n + ".pkl")
    dt = joblib.load("./" + str(int(nu)) + "/ml/dt_" + n + ".pkl")
    ada = joblib.load("./" + str(int(nu)) + "/ml/ada_" + n + ".pkl")
    rf = joblib.load("./" + str(int(nu)) + "/ml/rf_" + n + ".pkl")
    gbrt = joblib.load("./" + str(int(nu)) + "/ml/gbrt_" + n + ".pkl")
    d = []
    svm = svm.predict(P)
    d.append(svm)
    dt = dt.predict(P)
    d.append(dt)
    ada = ada.predict(P)
    d.append(ada)
    rf = rf.predict(P)
    d.append(rf)
    gbrt = gbrt.predict(P)
    d.append(gbrt)
    sd = sum(d)
    return sd
  
al = []
j = 1
for i in mn:
    all_sum = []
    n20 = i[0]
    n117 = i[1]
    n24 = i[2]
    all_sum.append(prediction(P20, n20, 20))
    all_sum.append(prediction(P24, n24, 24))
    all_sum.append(prediction(P117, n117, 117))
    al.append(sum(all_sum))
    j = j + 1
    #np.savetxt("./20_"+n20+"_117_"+n117+"_24_"+n24+".csv", np.transpose(all_sum), fmt = "%d" , delimiter = ",")
j = j - 1

asl = sum(al)/(j*15)
sequence_name = np.loadtxt(forld + "test_name.txt", dtype = str)
sn = list(sequence_name)
print("Sequnece_Name,Prediction_Scores")
for i in range(0,len(sn)):
    print(sn[i] + "," + str(asl[i]))
