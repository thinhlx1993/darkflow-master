from xml.dom import minidom
import xml.etree.ElementTree as ET
import os

train_folder = '/home/deeplearningcv/darkflow/darkflow-master/train/annotations'
for file_ in os.listdir(train_folder):
    if file_.endswith('xml'):
        file_name = '{}/{}'.format(train_folder, file_)
        # parse an xml file by name
        tree = ET.parse(file_name)  
        root = tree.getroot()

        # changing a field text
        for elem in root.iter('folder'):  
            elem.text = 'annotations'


        # changing a field text
        for elem in root.iter('path'):  
            text = elem.text
            current_path = "C:\\Users\\thinh\Pictures\\"
            text = text.replace(current_path, '/home/deeplearningcv/darkflow/darkflow-master/train/images/')
            print(text)
            elem.text = text 

        # create a new XML file with the results
        tree.write(file_name)   
