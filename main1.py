
import streamlit as st
import spacy
from annotated_text import annotated_text


@st.cache(show_spinner=False, allow_output_mutation=True, suppress_st_warning=True)

def load_models():
    
    english_model = spacy.load("./models/en/")
    deutsch_model= spacy.load("./models/de")
    models = {"en": english_model, "de": deutsch_model}
    return models


def process_text(doc, selected_entities):
    tokens = []
    for token in doc:
        if (token.ent_type_ == "PERSON") & ("PER" in selected_entities):
            tokens.append((token.text, "Person", "#faa"))
        
        elif (token.ent_type_ in ["GPE", "LOC"]) & ("LOC" in selected_entities):
            tokens.append((token.text, "Location", "#fda"))
       
        elif (token.ent_type_ == "ORG") & ("ORG" in selected_entities):
            tokens.append((token.text, "Organization", "#afa"))
        
        else:
            tokens.append(" " + token.text + " ")

def part_of(doc, part_of_speech):
    postag = []
    for token in doc: 
        if (token.pos__ == "VERB") & ("VERB" in part_of_speech):
            postag.append((token.text, "Verb", "#8ef"))

        elif (token.pos__ == "NOUN") & ("NOUN" in part_of_speech):
            postag.append((token.text, "noun", "#aaaaff"))
        
        elif (token.pos_ == "PRON") & ("PRON" in part_of_speech):
            postag.append((token.text, "PRON", "#C0FF3E"))

        elif (token.pos__ == "AdJ") & ("ADJ" in part_of_speech):
            postag.append((token.text, "ADJ", "#a6b1e1"))    
        else:
            postag.append(" " + token.text + " ")




models = load_models()


selected_language = st.sidebar.selectbox("Select a language", options=["en", "de"])

selected_entities = st.sidebar.multiselect(
    "Select the entities you want to detect",
    options=["LOC", "PER", "ORG"],
    default=["LOC", "PER", "ORG"],
)


part_of_speech = st.sidebar.multiselect(
    "Select the entities you want to detect",
    options=["VERB", "ADJ", "NOUN","PRON"],
    default=["VERB", "ADJ", "NOUN","PRON"],
)
selected_model = models[selected_language]

text_input = st.text_area("Type a text ")

uploaded_file = st.file_uploader("or Upload a file", type=["doc", "docx", "pdf", "txt"])
if uploaded_file is not None:
    text_input = uploaded_file.getvalue()
    text_input = text_input.decode("utf-8")

doc = selected_model(text_input)
tokens = process_text(doc, selected_entities)
postag = part_of(doc, part_of_speech)

annotated_text(*tokens, *postag)
