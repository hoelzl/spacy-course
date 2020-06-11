def test():
    import spacy.tokens
    import spacy.lang.de

    assert isinstance(
        nlp, spacy.lang.de.German
    ), "L'objet nlp doit être une instance de la classe German."
    assert isinstance(
        doc, spacy.tokens.Doc
    ), "As-tu traité le texte avec l'objet nlp pour créer un doc ?"
    assert "print(doc.text)" in __solution__, "As-tu affiché doc.text ?"

    __msg__.good("Sehr gut! :)")
