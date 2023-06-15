from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """translates an english string to french"""
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
   
    return french_text

def french_to_english(french_text):
    """#translates a french string to english"""
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    
    return english_text



