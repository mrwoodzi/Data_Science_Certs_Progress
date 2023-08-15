# XML and JSON
#

# XML - eXtensible Markup Language
    # primary pupose is to help information systems share structured data
    # started as a simplified subset of the Standard Generalized Markup Language(SGML), 
    # and is designed to be relatively human-legible

    # Tags - indicate the beginning and ending of elements
    # Attributes - Keyword/Value pairs on the opening tag of XML
    # Serialize/De-Serialize - Convert data in one program into a common format that can be stored 
        # and/or transmitted between systems in a programming language-independent manner

# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/web-services-xml

# Below is confusing rewatch video
    # Start Tag        - <person>
    # End Tag          -  <name>Michael</name>
    #                  -  <phone type="intl">
    # Text Content     -   +1 734 303 4456
    # Attribute        -  </phone>
    #                  -  <email hide="yes" />
    # Self Closing Tag - </person>


# This makes more sense to me
# XML as a Tree
# <a>
#   <b>X</b>
#    <c>
#      <d>Y</d>
#      <e>Z</e>
#    </c>
# </a>
#
#  XML Schema 
    # description of the legal format of an XML document
    # Expressed in terms of constraints on the structure and content of documents
    # Often used to specify a "contract" between systems - "My system will 
    #   only accept XML that conforms to this particular Schema"
    # If a particular piece of XML meets the specification of the Schema 
    #    it is said to "validate"
    # 
    # 
    # XSD - (W3C- World Wide Web Consortium) Schema specification for XML puts constraints on XML
    # XSD Structre
    # xs: complexType
    # xs: sequence
    # xs: element
    
    # example of XML
    # <person> 
    #  <lastname>Woods</lastname>
    #  <age>37</age>
    #  <dateborn>1892</dateborn>
    # </person>
    # 
    # 
    # ISO Date/Time Format
    # 2002-05-30T09:03:10Z // Z is time zone(Universal Time or Zulu Time, Grenitch )

# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/web-services-xml-schema

# import xml.etree.ElementTree as ET
#data = '''<person>
#    <name>Chuck</name>
#    <phone type="intl"
#    +1 734 303 4456
#    </phone>
#    <email hide="yes"/>
#</person>'''


# tree = ET.fromstring(data) # Tree is an object (data) is defined above
# print('Name:' ,tree.find('name').text) # call methods are extracting data from the tree above
# print('Attr:' ,tree.find('email').get(hide))


import xml.etree.ElementTree as ET
input = ''' <stuff>
    <users>
        <user x="2">
            <id>001</id<
            <name>Chuck</name>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
1st = stuff.findall('users/user')
print("User count:", len(1st))
for item in 1st:
    print('Name,', item.find('name').text)
    print('ID', item.find('id').text)
    print('Attribute', item.get("x"))