# Thermal Matrix to Image Conversion script
This script is written using Python to convert thermal matrix to image to understand heat distribution on the surface
---


### Instructions
1. Clone this repository. \
`git clone https://github.com/sakshi-seth-17/ThermalMatrixToImage.git`

2. Travel to the parent project directory and install the required python packages. \
Create virtual environment – `python3 -m venv venv` \
`source venv/bin/activate` \
`pip3 install -r requirement.txt` \
Run – `python3 app.py` 

---
### Location details of the components:
1.	Application code path (on webserver - webserver@128.192.158.63) path: /var/www/aspendb/probesearch/ThermalMatrixToImage
2.  Database location - /var/www/aspendb/probesearch/SensorsData/Data-Store.db

---
### Technical details:
1. The application is built using Python.

---
### Folder Structure
- venv/
- app.py
- userdefined.py
- requirement.txt
- config.json

---
### Application Code Flow - app.py
1. Import all the necessary packages.
2. Load config.json to get all the queries for which we need to convert the thermal matrix to thermal images.
3. generateThermalImage() takes 3 input - thermal matrix as a string, fileName using which image will be saved, Image directory (if does not exist it will create one). 
