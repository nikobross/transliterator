import eng_to_ipa as ipa
import re
from unit import Unit

ipa_consonants = ["p", "b", "t", "d", "k", "g", "θ", "ð", "f", "v", "s", "z", "ʃ", "ʒ", "tʃ", "dʒ", "w", "ɫ", "m", "n", "ŋ", "ɹ", "j", "h", "l", "r"]
ipa_vowels = ["i", "u", "ɪ", "ʊ", "ə", "ɛ", "ɝ", "ɔ", "æ", "ɑ", "eɪ", "aɪ", "aʊ", "ɔɪ", "oʊ"]

def convert_to_ipa(text):
    ipa_text = ipa.convert(text)
    # remove ˈ
    ipa_text = re.sub(r"ˈ", "", ipa_text)
    return ipa_text

def split_ipa_into_units(ipa_text):
    """
    Splits IPA text into individual characters, diphthongs, and consonant clusters.
    """
    diphthongs = ["eɪ", "aɪ", "aʊ", "ɔɪ", "oʊ"]
    consonant_clusters = ["tʃ", "dʒ", "ŋg", "ndʒ", "kp", "gb"]  # Add other clusters as needed
    units = []
    i = 0
    while i < len(ipa_text):
        # Check for consonant clusters
        if i < len(ipa_text) - 1 and ipa_text[i:i + 2] in consonant_clusters:
            units.append(ipa_text[i:i + 2])  # Add the consonant cluster as a single unit
            i += 2  # Skip the next character
        # Check for diphthongs
        elif i < len(ipa_text) - 1 and ipa_text[i:i + 2] in diphthongs:
            units.append(ipa_text[i:i + 2])  # Add the diphthong as a single unit
            i += 2  # Skip the next character
        else:
            units.append(ipa_text[i])  # Add the single character
            i += 1
    return units

def convert_ipa_to_syllables(ipa_units):
    syllables = []
    
    i = 0
    while i < len(ipa_units):
        unit = ipa_units[i]
        
        if unit in ipa_consonants:  # If the unit is a consonant
            consonant = unit
            vowel = None
            
            if i + 1 < len(ipa_units) and ipa_units[i + 1] in ipa_vowels:  # Check for a following vowel
                vowel = ipa_units[i + 1]
                syllable_type = "CV"
                i += 1  # Skip the vowel since it's part of this syllable
            else:
                syllable_type = "C"
            
            syllables.append(Unit(syllable_type, consonant, vowel, unit))
        elif unit in ipa_vowels:  # If the unit is a vowel
            syllables.append(Unit("V", None, unit, unit))
        elif unit == " ":  # If the unit is a space
            syllables.append(Unit("unique symbol", None, None, unit))
        else:  # For punctuation or other unique symbols
            syllables.append(Unit("unique symbol", None, None, unit))
        
        i += 1

    return syllables

def closest_chars(units, consonant_map, vowel_map):
    for unit in units:
        if unit.is_CV():
            unit.consonant = consonant_map.get(unit.consonant, unit.consonant)
            unit.vowel = vowel_map.get(unit.vowel, unit.vowel)
        elif unit.is_C():  # Convert C units to CV units
            unit.consonant = consonant_map.get(unit.consonant, unit.consonant)
            unit.vowel = "a"  # Assign the vowel 'a'
            unit.type = "CV"  # Update the type to CV
        elif unit.is_V():
            unit.vowel = vowel_map.get(unit.vowel, unit.vowel)

    return units

def syllable_map(units, syllable_mapping):
    text = ""
    for unit in units:
        if unit.is_syllable():
            text += syllable_mapping[unit.consonant][unit.vowel]
        else:
            text += unit.symbol

    return text

def full_conversion(text, consonant_map, vowel_map, syllable_mapping):
    ipa_text = convert_to_ipa(text)
    ipa_units = split_ipa_into_units(ipa_text)
    syllables = convert_ipa_to_syllables(ipa_units)
    closest_chars(syllables, consonant_map, vowel_map)
    final_text = syllable_map(syllables, syllable_mapping)
    return final_text
