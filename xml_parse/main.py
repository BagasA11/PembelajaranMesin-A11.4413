import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    # <tag attr:"" />
    # tag{attr : val}
    for val in child.attrib.values():
        print(val)
    print()

    for attr in child.attrib:
        print(attr)
    print("\n")

print(root[0][1].text) #print 2008
print(root[0][2].text) #print 141100

# print continent attribute of Liechenstein
print("liechenstein: ", root[0].attrib["continent"])

# get all data in specific tag
# Element has some useful methods that help iterate recursively over all the sub-tree below it 
# (its children, their children, and so on). 
# For example, Element.iter():
print("\n get all data in specific tag \n")
for n in root.iter("neighbor"):
    print(n.attrib)

# Element.findall() finds only elements with a tag which are direct children of the current element. 
# Element.find() finds the first child with a particular tag, and Element.text accesses the element’s text content. 
# Element.get() accesses the element’s attributes:

print("\n findall \n")
for country in root.findall("country"):
    rank = country.find("rank").text #find element's child tag
    name = country.get("name") #find element's attr
    print("  ", name, rank)
