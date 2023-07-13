
from deep_translator import MyMemoryTranslator

def english_to_french(englishText):
    frenchText = MyMemoryTranslator("en-US", "fr-FR").translate(englishText, True)
    
    return frenchText

def french_to_english(frenchText):
    
    englishText = MyMemoryTranslator("fr-FR", "en-US").translate(frenchText, True)

    return englishText