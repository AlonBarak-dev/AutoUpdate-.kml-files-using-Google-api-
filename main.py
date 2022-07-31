from simplekml import Kml
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# connect to drive 
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  
# kml files name
upload_file_list = ['LinkLine.kml']
# create the file pointer
# gfile = drive.CreateFile({'parents': [{'id': '1ID1ttd4ThKG_ABZ-Qu43jtqLmzVijz2R'}]})
gfile = drive.CreateFile({'id': '<ID>'})
# https://drive.google.com/file/d/<ID>/view?usp=sharing

# extract longitude, latitude info from the GPS csv info file
lon = []
lat = []
f = open('path.csv')
for line in f:
    fields = line.split(',')
    lon.append(fields[0])
    lat.append(fields[1])

# create a coordinates list of (lon, lat) tuples
coords = []
for i in range(len(lon)):
    coords.append((lon[i], lat[i]))
# create a KML file and add a line representing all the coordinates 
kml = Kml()
docs = kml.newdocument(name= 'LinkLine')
docs.newlinestring(name='PCBLine', coords=coords)
kml.save('LinkLine.kml')
 
# update the file content

for upload_file in upload_file_list:
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.


