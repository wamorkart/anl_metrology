import argparse
from statistics import mean
import numpy as np
import glob
import os


parser = argparse.ArgumentParser()
# parser.add_argument("-i", "--inputFile", type=str, help = "input txt file")
parser.add_argument("-j", "--inputFileJig", type=str, help = "input jig txt file", default = "Jig_SQ.txt" )
parser.add_argument("-m", "--measurement", type=str, help = "measurement type")

args = parser.parse_args()

# infile = args.inputFile
infile_jig = args.inputFileJig

measurement = args.measurement
print (measurement)
if (measurement == "flex"):
    infile = max(glob.iglob("flex_SQ_*"), key=os.path.getctime)
    print ("Module input file: ", infile)
elif (measurement == "dummyBM"):
    infile = max(glob.iglob("dummyBM_SQ*"), key=os.path.getctime)
    print ("Module input file: ", infile)
    infile_jig = "dummyBMJig_SQ.txt"
elif (measurement == "assembly"):
    # infile = "AssembledModule_SQ_20230519133123.txt"
    infile = max(glob.iglob("AssembledModule_SQ*"), key=os.path.getctime)
    print ("Module input file: ", infile)
    infile_jig = "AssembledModuleJig_SQ.txt"
# 

len_Y = []
len_X = []
len_Z_Laser = []
len_Z_Optical = []
pickup_1 = []
pickup_2 = []
pickup_3 = []
pickup_4 = []
PC_1 = []
PC_2 = []
PC_3 = []
HV = []
pickup = []
PC = []
HV = []
dummy_thickness = []
jig_dummy_thickness = []

jig_pickup_1 = []
jig_pickup_2 = []
jig_pickup_3 = []
jig_pickup_4 = []

jig_PC_1 = []
jig_PC_2 = []
jig_PC_3 = []
jig_HV = []



if (measurement == "flex"):

    with open(infile_jig) as jig_file:
        for line in jig_file:
            if "Pickup1" in line and "Laser" not in line:
                jig_pickup_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup2" in line and "Laser" not in line:
                jig_pickup_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
            if "Pickup3" in line and "Laser" not in line:
                jig_pickup_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))            
            if "Pickup4" in line and "Laser" not in line:
                jig_pickup_4.append(float((line.split()[1].replace('Z|','')).replace('|','')))        

            if "PC_1" in line and "Laser" not in line:
                jig_PC_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "PC_2" in line and "Laser" not in line:
                jig_PC_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))        
            if "PC_3" in line and "Laser" not in line:
                jig_PC_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))

            if "HV" in line and "Laser" not in line:
                jig_HV.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
                    

    with open(infile) as file:
        for line in file:
            if "Pickup1" in line and "Laser" not in line:
                pickup_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup2" in line and "Laser" not in line:
                pickup_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup3" in line and "Laser" not in line:
                pickup_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
            if "Pickup4" in line and "Laser" not in line:
                pickup_4.append(float((line.split()[1].replace('Z|','')).replace('|','')))

            if "PC_1" in line and "Laser" not in line:
                PC_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "PC_2" in line and "Laser" not in line:
                PC_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))        
            if "PC_3" in line and "Laser" not in line:
                PC_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))    

            if "HV" in line and "Laser" not in line:
                HV.append(float((line.split()[1].replace('Z|','')).replace('|','')))


            if "distance_X" in line:
                print ("X: ", float((line.split()[1].replace('DX|','')).replace('|','')))
            if "distance_Y" in line:
                print ("Y: ", float((line.split()[1].replace('DY|','')).replace('|','')))


    pickup_1_z =  (np.subtract(jig_pickup_1, pickup_1))
    pickup_2_z =  (np.subtract(jig_pickup_2, pickup_2))
    pickup_3_z =  (np.subtract(jig_pickup_3, pickup_3))
    pickup_4_z =  (np.subtract(jig_pickup_4, pickup_4))
    print ("Pickup 1: ", abs(np.mean(pickup_1_z)), "   ", np.std(pickup_1_z))
    print ("Pickup 2: ", abs(np.mean(pickup_2_z)), "   ", np.std(pickup_2_z) )
    print ("Pickup 3: ", abs(np.mean(pickup_3_z)), "   ", np.std(pickup_3_z))
    print ("Pickup 4: ", abs(np.mean(pickup_4_z)), "   ", np.std(pickup_4_z))
    print ("Avg pickup thickness:  ", abs(np.mean([np.mean(pickup_1_z), np.mean(pickup_2_z), np.mean(pickup_3_z), np.mean(pickup_4_z)])))
    print ("Std Dev pickup thickness: ", np.std([np.mean(pickup_1_z), np.mean(pickup_2_z), np.mean(pickup_3_z), np.mean(pickup_4_z)]))

    PC_1_z =  (np.subtract(jig_PC_1, PC_1))
    PC_2_z =  (np.subtract(jig_PC_2, PC_2))
    PC_3_z =  (np.subtract(jig_PC_3, PC_3))

    print ("Average PC height:  ", abs(np.mean([np.mean(PC_1_z), np.mean(PC_2_z), np.mean(PC_3_z)])))

    HV_z = np.subtract(jig_HV, HV)
    print ("Avg HV height: ", abs(np.mean(HV_z)) )

elif (measurement == "dummyBM"):
    print (infile_jig)
    with open(infile_jig) as jig_file:
        for line in jig_file:
            if ("Z" in line):
                jig_dummy_thickness.append(float((line.split()[1].replace('Z|','')).replace('|','')))

    with open(infile) as file:
        for line in file:
            if ("Z" in line):
                dummy_thickness.append(float((line.split()[1].replace('Z|','')).replace('|','')))                

    Z_dummy =  (np.array(dummy_thickness) - jig_dummy_thickness)
    print ("BM thickness average: ", mean(Z_dummy))  
    print ("BM thickness std dev: ", np.std(Z_dummy))  

if (measurement == "assembly"):

    with open(infile_jig) as jig_file:
        for line in jig_file:
            if "Pickup1" in line and "Laser" not in line:
                jig_pickup_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup2" in line and "Laser" not in line:
                jig_pickup_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
            if "Pickup3" in line and "Laser" not in line:
                jig_pickup_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))            
            if "Pickup4" in line and "Laser" not in line:
                jig_pickup_4.append(float((line.split()[1].replace('Z|','')).replace('|','')))        

            if "PC_1" in line and "Laser" not in line:
                jig_PC_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "PC_2" in line and "Laser" not in line:
                jig_PC_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))        
            if "PC_3" in line and "Laser" not in line:
                jig_PC_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))

            if "HV" in line and "Laser" not in line:
                jig_HV.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
                    

    with open(infile) as file:
        for line in file:
            if "Pickup1" in line and "Laser" not in line:
                pickup_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup2" in line and "Laser" not in line:
                pickup_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "Pickup3" in line and "Laser" not in line:
                pickup_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))    
            if "Pickup4" in line and "Laser" not in line:
                pickup_4.append(float((line.split()[1].replace('Z|','')).replace('|','')))

            if "PC_1" in line and "Laser" not in line:
                PC_1.append(float((line.split()[1].replace('Z|','')).replace('|','')))
            if "PC_2" in line and "Laser" not in line:
                PC_2.append(float((line.split()[1].replace('Z|','')).replace('|','')))        
            if "PC_3" in line and "Laser" not in line:
                PC_3.append(float((line.split()[1].replace('Z|','')).replace('|','')))    

            if "HV" in line and "Laser" not in line:
                HV.append(float((line.split()[1].replace('Z|','')).replace('|','')))


            if "distance_X" in line:
                print ("X: ", float((line.split()[1].replace('DX|','')).replace('|','')))
            if "distance_Y" in line:
                print ("Y: ", float((line.split()[1].replace('DY|','')).replace('|','')))


    pickup_1_z =  (np.subtract(jig_pickup_1, pickup_1))
    pickup_2_z =  (np.subtract(jig_pickup_2, pickup_2))
    pickup_3_z =  (np.subtract(jig_pickup_3, pickup_3))
    pickup_4_z =  (np.subtract(jig_pickup_4, pickup_4))
    print ("Pickup 1: ", abs(np.mean(pickup_1_z)), "   ", np.std(pickup_1_z))
    print ("Pickup 2: ", abs(np.mean(pickup_2_z)), "   ", np.std(pickup_2_z) )
    print ("Pickup 3: ", abs(np.mean(pickup_3_z)), "   ", np.std(pickup_3_z))
    print ("Pickup 4: ", abs(np.mean(pickup_4_z)), "   ", np.std(pickup_4_z))
    print ("Avg pickup thickness:  ", abs(np.mean([np.mean(pickup_1_z), np.mean(pickup_2_z), np.mean(pickup_3_z), np.mean(pickup_4_z)])))
    print ("Std Dev pickup thickness: ", np.std([np.mean(pickup_1_z), np.mean(pickup_2_z), np.mean(pickup_3_z), np.mean(pickup_4_z)]))

    PC_1_z =  (np.subtract(jig_PC_1, PC_1))
    PC_2_z =  (np.subtract(jig_PC_2, PC_2))
    PC_3_z =  (np.subtract(jig_PC_3, PC_3))

    print ("Average PC height:  ", abs(np.mean([np.mean(PC_1_z), np.mean(PC_2_z), np.mean(PC_3_z)])))

    HV_z = np.subtract(jig_HV, HV)
    print ("Avg HV height: ", abs(np.mean(HV_z)) )
