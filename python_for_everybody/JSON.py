# JSON was "Discoverd by Douglas Crockford"
# Object literal notation in JavaScript
# Way to specify/pack data to be sent
# https://www.json.org/json-en.html
# JSON represents data as nested "lists" and "dictionaries"
# A collection of name/value pairs. In various languages, this is realized as an object, 
#   record, struct, dictionary, hash table, keyed list, or associative array.
# An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.

# In JSON - An object is an unordered set of name/value pairs. An object begins with {left brace and 
# ends with }right brace. Each name is followed by :colon and the name/value pairs are separated by ,comma.

# An array(In Python this is a List) is an ordered collection of values. An array begins with 
# [left bracket and ends with ]right bracket. Values are separated by ,comma.

# A value can be a string in double quotes, or a number, or true or false or null, 
# or an object or an array. These structures can be nested.

# A string is a sequence of zero or more Unicode characters, wrapped in double quotes,
#  using backslash escapes. A character is represented as a single character string. A string is 
# very much like a C or Java string.

# A number is very much like a C or Java number, except that the octal and hexadecimal formats are not used.

# Whitespace can be inserted between any pair of tokens. Excepting a few encoding details, 
# that completely describes the language.

# Using Python to process JSON
import json # below "data" would be data that is retrieved from somewhere, it is also all a script
# Also curly brace defines a dictionary
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl", 
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:' ,info["name"])
print('Hide:' ,info["email"]["hide"])

# import JSON # input is a list of 2 dictionaries
input = '''[ 
    { "id" : "001"
      "x" : "2",
      "name" : "Chuck"
    } , 
    { "id" : "009"
      "x" : "7",
      "name" : "Chuck"
    }
]'''

info = json.loads(input)
print('User count:' len(info))
for item in info:
    print('Name', item['name'])
    print('ID', item['id'])
    print('Attrribute', item['x'])

