import streamlit as st 
from cassis import *

with open('TypeSystem.xml', 'rb') as f:
    typesystem = load_typesystem(f)

with open('essay_en.txt.xmi', 'rb') as f:
    cas = load_cas_from_xmi(f, typesystem=typesystem)

for sentence in cas.select('de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Sentence'):
    for token in cas.select_covered('de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Token', sentence):
        st.write(token.get_covered_text())

        # Annotation values can be accessed as properties
        st.write('Token: id= {}, lemma={}, pos={}'.format(token.begin, token.end, token.id, token.pos,token.lemma, token.stem))
