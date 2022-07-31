# AutoUpdate .kml files for Google Earth pro engine
AutoUpdate KML files using a Network Link on Google Drive using the Google-client api. 

## Pre-requestes: <br>
  - Google Drive account
  - Google Earth Pro
  - client_secrets.json from Drive
  - .csv file with longitude and latitude values
#### Note: Tested on Linux Ubuntu 20.04 <br>

## How to use: <br>
  - Make sure to update the <ID> attribute that it will be compaitable to your Drive path's ID. <br>
  - Update the .csv file name on the code to your .csv file name. <br>
  - Locate your client_secrets.json on the same folder with this repo. <br>
  - Make sure to create a Network Link on your Google Earth pro that contain the link of the .kml file from your drive account. <br>
  - run:
  ```ruby 
  python3 main.py
  ```
  

