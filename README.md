# Data Structures (datatype conversion) Conversion package

<sup> current data-structure supported: List, Dictionary, Tuple, Set  </sup>

##Installation
Run the following to install:
'''python
pip install disconv'''


##Usage
'''python
import disconv as foo

#Conversion to int
foo.tonum(data)

#Conversion to float
foo.tofloat(data)

#Conversion to int
foo.tostr(data)

#data refers to a variable of any of the supported datastructure types 
'''




##Methods:
### tonum() : converts values in supported datastructures to int type
	conversions: source_type:output_type => int:int, float:int, str: list of ASCII, bool: {True:1,False:0}

### tostr() : converts values in supported datastructures to str type

### tofloat() : converts values in supported datastructures to float type
	conversions: source_type:output_type => int:float, float:float, str: list of ASCII values in float, bool: {True:1.0,False:0.0}

Note_1: Conversion of dict type data-structures convert the datatype of the values of the dictionary

# Developing disconv

To install disconv, along with the tools you need to develop and run tests, run the following in your virtualenv:
'''bash
$ pip install -e .[dev]
'''

Note_2: This is a work in progress. Do feel free to contact me with any suggestions, improvements or bugs you find at you have at: leejohnsdecarmel@gmail.com




