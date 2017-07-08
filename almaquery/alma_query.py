from astroquery.alma import Alma
from astropy import coordinates
from astropy import units as u
import time

import numpy as np
import pandas as pd
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup

# 3c279
#ra = 194.046527
#dec = -5.789312

ra = 194.046529167 
dec = -5.7893125

region = coordinates.SkyCoord(ra, dec, unit='deg')

data = Alma.query_object_async("QSO J1256-0547", 0.003*u.deg, science = False, public = True)

# data.txt is unicode
xmldata = BeautifulSoup(data.text, "lxml")

with open("xmldata.xml", 'w') as ofile:
    ofile.write(str(xmldata.contents[1]))


tree = ET.parse("xmldata.xml")

root = tree.getroot()



projects = []
for i, proj in enumerate(root[0][0][0][2][36][0]): # many child
    projects.append([])
    for data in proj:
        if data.text is None:
            projects[i].append('None')
        else:
            projects[i].append(data.text)

columns=['Project code', 'Source name', 'RA', 'Dec', 'Galactic longitude', 'Galactic latitude', \
         'Band', 'Spatial resolution', 'Frequency resolution', 'Array', 'Mosaic', 'Integration', \
         'Release date', 'Frequency support', 'Velocity resolution', 'Pol products', \
         'Observation date', 'PI name', 'SB name', 'Proposal authors', 'Line sensitivity (10 km/s)', \
         'Continuum sensitivity', 'PWV', 'Group ous id', 'Member ous id', 'Asdm uid', 'Project title', \
         'Project type', 'Scan intent', 'Field of view', 'Largest angular scale', 'QA2 Status',\
         'Pub', 'Science keyword', 'Scientific category', 'ASA_PROJECT_CODE']


df = pd.DataFrame(projects, columns=columns)

print df['Integration']