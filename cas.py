import streamlit as st 
from cassis import *

with open('small_typesystem.xml', 'rb') as f:
    typesystem = load_typesystem(f)

with open('small_cas.xmi', 'rb') as f:
    cas = load_cas_from_xmi(f, typesystem=typesystem)

for sentence in cas.select('cassis.Sentence'):
    for token in cas.select_covered('cassis.Token', sentence):
        st.write(token.get_covered_text())

        # Annotation values can be accessed as properties
        st.write('Token:  pos={3}'.format(token.begin, token.end, token.id, token.pos))