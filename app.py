'''
    Import necessary packages
'''
import cv2
import numpy as np
import os
import sqlite3
import pandas as pd
from userdefined import *

'''
    Load config file
'''

configData = readJson("config.json")
path = "/var/www/aspendb/probesearch/SensorsData"

'''
    convert thermal matrix to image
'''
def generateThermalImage(data, fileName, directory):
    thermalMatrix = []
    thermalMatrixStr = data.replace("[","").split("]")
    for row in thermalMatrixStr:
        row = row.replace("\n","")
        if row!="":    
            for l in row:
                temp = [float(i) for i in row.split(" ") if i!=""]
            thermalMatrix.append(temp)
            
    thermal_matrix = np.asarray(thermalMatrix)
    
    # Normalize the temperature values to fit within the range 0-255
    normalized_matrix = cv2.normalize(thermal_matrix, None, 0, 255, cv2.NORM_MINMAX)
    
    # Apply a color map to the normalized matrix to create a color image
    color_image = cv2.applyColorMap(normalized_matrix.astype(np.uint8), cv2.COLORMAP_HOT)
    
    imagePath = "/var/www/aspendb/probesearch/ThermalMatrixToImage"
    directory_path = imagePath+"/"+directory+"_Thermal"
    
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_path):
        
        os.mkdir(directory_path)
        
    # Save the image to a file
    cv2.imwrite(directory_path+"/"+fileName+".jpg", color_image)
    
    
    
for item in configData["Queries"]:
    count = 0
    query = configData["Queries"][item].format("2023-04-29 00:00:00") #change the date as required
    df = readSqlite(query,path+"/Data-Store.db")
    thermalMatrixList = list(df["Thermal"])
    imageRefList = list(df["DATE_"])
    for i in range(len(thermalMatrixList)):
        try:
            generateThermalImage(thermalMatrixList[i], imageRefList[i].replace(":","-"), item)
            count += 1
        except:
            pass
    print(item + ": "+ str(count) + " thermal images generated")