###cache_score.csv라는 파일에서 데이터(특히 AutoDock_GPU와 AutoDock_Vina 열)를 읽어와 특정 통계 값들을 계산
###AutoDock_Vina의 데이터를 바탕으로 히스토그램을 생성


#!/usr/bin/env python
# coding: utf-8

# In[52]:

import seaborn as sns; sns.set()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

data = pd.read_csv('cache_score.csv',low_memory=False)
GPU = data['AutoDock_GPU']
VINA = data['AutoDock_Vina']

Gpu = GPU.describe()
Vina = VINA.describe()

#pro_describe = {'AutoDock-GPU' : Gpu, 'AutoDock-Vina' : Vina}
pro_describe = {'AutoDock-Vina' : Vina}
#pro_corr = {'AutoDock-GPU' : GPU, 'AutoDock-Vina' : VINA}
pro_corr = {'AutoDock-Vina' : VINA}

print(pro_describe)
#print(pro_corr)

for pro, corr in pro_corr.items():
    avg = pro_describe[pro][1]
    avg = avg.round(2)

    std = pro_describe[pro][2]
    std = std.round(2)

    fir_q = pro_describe[pro][6]
    fir_q = fir_q.round(2)

    sec_q = pro_describe[pro][5]
    sec_q = sec_q.round(2)

    thr_q = pro_describe[pro][4]
    thr_q = thr_q.round(2)

    plt.axvline(0, 0, 100, color='lightgray', linestyle='--', linewidth=0.7,)
    sns.histplot(corr, kde=True, color='royalblue', bins=18)
    plt.title(f'{pro}', fontsize=25)
    plt.xlim(-15,0)
    plt.xticks(fontsize=7.5)
    plt.yticks(fontsize=7.5)
    plt.ylim(0,150000)
    plt.xlabel('Docking score (kcal/mol)', fontsize=15)
    plt.text(-14.7,113000,f"Avg = {avg}\nStd = {std}\nQ1  = {fir_q}\nQ2  = {sec_q}\nQ3  = {thr_q}", fontsize = 11)
    plt.ylabel('Count', fontsize=15)
    plt.savefig(f'{pro}_hist.png')
    plt.close()

#In[]:
