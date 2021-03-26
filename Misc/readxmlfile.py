from xml.etree.ElementTree import ElementTree


def get_child(element):
    for child in element:
        return child


def get_text(element):
    return element.text


tree = ElementTree()
tree.parse(r"D:\ProjectProject (3).aml")
#xpath = ".//Attribute[@Name='Selected Region']"
#element = tree.find(xpath)
#child = get_child(element)
#print(get_text(child))
xpath = ".//InternalElement"
elements  = tree.findall(xpath)
for element in elements:
    print(element.attrib)

xpath =".//InternalElement[@Name='DIAVH-IPC003103A']"
element = tree.find(xpath)
print(element.attrib)