### adding annotations 

from dkpro cassis documentation 


from cassis import *

with open('small_typesystem.xml', 'rb') as f:
    typesystem = load_typesystem(f)



############ what is file cas.xml ? 
#### where should I add xmi file?
with open('cas.xml', 'rb') as f:     
    cas = load_cas_from_xmi(f, typesystem=typesystem)

Token = typesystem.get_type('cassis.Token')


#### #####in the xml file the type sytem is cassis.Token with features id and pos
##from Where are these values determined for Pos, begin, and end has been?
##from xmi file ?? 
 


tokens = [
    Token(begin=0, end=3, id='0', pos='NNP'), 
    Token(begin=4, end=10, id='1', pos='VBD'),
    Token(begin=11, end=14, id='2', pos='IN'),
    Token(begin=15, end=18, id='3', pos='DT'),
    Token(begin=19, end=24, id='4', pos='NN'),
    Token(begin=25, end=26, id='5', pos='.'),
]

for token in tokens:
    cas.add(token)