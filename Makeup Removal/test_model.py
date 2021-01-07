# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 00:53:01 2020

@author: AEGEAN
"""
import os

i = 5
while i <= 100:
    print(i)
    nameD = '_net_D.pth'
    nameG = '_net_G.pth'
    nameGi = str(i) + nameG
    nameDi = str(i) + nameD
    targetA = 'latest_net_G.pth'
    targetB = 'latest_net_D.pth'
    aG = r'./checkpoints/makeup/' + nameGi
    bG = r'./checkpoints/makeup/' + targetA
    aD = r'./checkpoints/makeup/' + nameDi
    bD = r'./checkpoints/makeup/' + targetB
    
    os.rename(aG, bG)
    os.rename(aD ,bD)
    
    os.mkdir('./results/' + str(i))
    
    result_dir = ' --results_dir ' + './results/' + str(i) + '/'
    
    os.system('python test.py --dataroot "./datasets/makeup/"  ' + result_dir + ' --name makeup --model test --netG unet_256 --direction BtoA --norm batch')
    
    os.rename(bG, aG)
    os.rename(bD ,aD)
    i = i + 5