#!/usr/bin/env python3

import numpy as np

TargetSum = [
    7.2000000000e+00,
    4.1378689100e-01,
    1.3411245310e-01,
    7.7893888630e-01,
    9.2182543220e-01,
    2.2472205680e-01,
    1.2874154910e+00,
    1.5988006300e-01,
    5.0845877390e-01,
    2.2360063000e-01,
    5.1770867170e-01,
    2.6388310150e+00,
    2.8416494690e-01]

data = np.loadtxt("eccentricities_evo_eta_-0.5_0.5.dat")
ResSum = np.sum(abs(data), axis=0)

Nfailed = 0
for i, val_i in enumerate(TargetSum):
    if abs(val_i - ResSum[i]) > 1e-8:
        print("eccentricities_evo: Diff: ", val_i, ResSum[i])
        Nfailed += 1

TargetSum = [
    7.2000000000e+00,
    1.4323939960e+01,
    1.6930512028e+00,
    9.5527826500e+00,
    2.6242441660e+00]

data = np.loadtxt("inverse_Reynolds_number_eta_-0.5_0.5.dat")
ResSum = np.sum(abs(data), axis=0)

Nfailed = 0
for i, val_i in enumerate(TargetSum):
    if abs(val_i - ResSum[i]) > 1e-8:
        print("inverseReynoldsNumbers: Diff: ", val_i, ResSum[i])
        Nfailed += 1

TargetSum = [
    7.2000000000e+00,
    2.5942807710e-01,
    5.5521879130e-02,
    5.0768989900e-02,
    1.3220156732e-02,
    4.6510548130e-02,
    1.3067411065e-02,
    9.8801770270e-01,
    4.2395180420e-01,
    9.0055768070e-01,
    4.1781155060e-01,
    9.0589301460e-01,
    4.2159863140e-01,
    1.7925897327e-01,
    1.3762513451e-01,
    1.6402716434e-01,
    1.3738494165e-01,
    1.6709324576e-01,
    1.4706236236e-01]

data = np.loadtxt("momentum_anisotropy_eta_-0.5_0.5.dat")
ResSum = np.sum(abs(data), axis=0)

Nfailed = 0
for i, val_i in enumerate(TargetSum):
    if abs(val_i - ResSum[i]) > 1e-8:
        print("momentum_anisotropy_evo: Diff: ", val_i, ResSum[i])
        Nfailed += 1

TargetSum = [
    7.2000000000e+00,
    2.2911828260e+04,
    5.6667823340e+03,
    4.6828341370e+02,
    8.9168491220e+01]

data = np.loadtxt("meanpT_estimators_eta_-0.5_0.5.dat")
ResSum = np.sum(abs(data), axis=0)

Nfailed = 0
for i, val_i in enumerate(TargetSum):
    if abs(val_i - ResSum[i]) > 1e-8:
        print("meanpTEstimators_evo: Diff: ", val_i, ResSum[i])
        Nfailed += 1

exit(Nfailed)
