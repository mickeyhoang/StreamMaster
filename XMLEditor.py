import xml.etree.ElementTree as ET
from xml.dom import minidom

# Updates XML file for player tag, takes in player number and tag
def XMLPlayerUpdate(number, playercrew, playertag, playerscore):
    fileLocation = "XMLFiles/Player" + str(number) + ".xml"     # Open corresponding file

    root = ET.Element('root')                                   # Create Root and then info subelement
    info = ET.SubElement(root, 'info')

    ET.SubElement(info, 'PlayerCrew').text = playercrew
    ET.SubElement(info, 'PlayerTag').text = playertag           # Add in SubElement of playertag
    ET.SubElement(info, 'PlayerScore').text = playerscore

    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")  # Pretty Print XML
    with open(fileLocation, 'w') as f:
        f.write(xmlstr)
    f.close()

def XMLMatchUpdate(prefix, roundInfo, num, game, info1, info2):
    fileLocation = "XMLFiles/Match.xml"

    root = ET.Element('root')
    info = ET.SubElement(root, 'info')

    ET.SubElement(info, 'BracketSide').text = prefix
    ET.SubElement(info, 'Round').text = roundInfo
    ET.SubElement(info, 'Number').text = num
    ET.SubElement(info, 'Game').text = game
    ET.SubElement(info, 'Info1').text = info1
    ET.SubElement(info, 'Info2').text = info2

    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")  # Pretty Print XML
    with open(fileLocation, 'w') as f:
        f.write(xmlstr)
    f.close()