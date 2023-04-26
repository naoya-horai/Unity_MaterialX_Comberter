import pathlib
import xml.etree.ElementTree as ET
from unityparser import UnityDocument
import materialx as mx
def main():
        docmx = ET.parse('TestMaterial_MaterialX.mtlx')
        root = docmx.getroot()
        for child in root:
                for gild in child:
                        if gild.get('name') == "base_color":
                                basecolor = gild.get('value')
                                basecolor = [x.strip() for x in basecolor.split(',')]
                                #print(basecolor)
                        elif gild.get('name') == "metalness":

                                metalness = gild.get('value')
         
                        elif gild.get('name') == "specular":

                                specular = gild.get('value')

#print(root)
        doc = UnityDocument.load_yaml("TestMaterial_Unity.mat")
        material = doc.entry
        color = material.m_SavedProperties['m_Colors'][0]['_Color']
        metallic = material.m_SavedProperties['m_Floats'][7]
        glossiness = material.m_SavedProperties['m_Floats'][5]
        color['r'] = basecolor[0]
        color['g'] = basecolor[1]
        color['b'] = basecolor[2]
        metallic['_Metallic'] = metalness
        glossiness['_Glossiness'] = specular
        doc.dump_yaml()

import time
starttime = time.perf_counter()
main()
print(time.perf_counter()-starttime)