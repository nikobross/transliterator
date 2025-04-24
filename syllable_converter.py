import eng_to_ipa as ipa
import re

ipa_consonants = ["p", "b", "t", "d", "k", "g", "θ", "ð", "f", "v", "s", "z", "ʃ", "ʒ", "tʃ", "dʒ", "w", "ɫ", "m", "n", "ŋ", "ɹ", "j", "h", "l"]
ipa_vowels = ["i", "u", "ɪ", "ʊ", "ə", "ɛ", "ɝ", "ɔ", "æ", "ɑ", "eɪ", "aɪ", "aʊ", "ɔɪ", "oʊ"]

def convert_to_ipa(text):
    ipa_text = ipa.convert(text)
    return ipa_text

def split_ipa_into_units(ipa_text):
    diphthongs = ["eɪ", "aɪ", "aʊ", "ɔɪ", "oʊ"]
    units = []
    i = 0
    while i < len(ipa_text):
        # Check for diphthongs
        if i < len(ipa_text) - 1 and ipa_text[i:i + 2] in diphthongs:
            units.append(ipa_text[i:i + 2])  # Add the diphthong as a single unit
            i += 2  # Skip the next character
        else:
            units.append(ipa_text[i])  # Add the single character
            i += 1
    return units

def convert_ipa_to_syllables(ipa_units):
    ipa_text = re.sub(r"ˈ", "", ipa_text)  # Remove primary stress markers

    syllables = []
    current_syllable = ""

    for unit in ipa_units:
        if unit in ipa_consonants:  # If the unit is a consonant
            if current_syllable:  # Finalize the current syllable
                syllables.append(current_syllable)
                current_syllable = ""
            current_syllable += unit  # Start a new syllable with the consonant
        elif unit in ipa_vowels:  # If the unit is a vowel
            current_syllable += unit  # Add the vowel to the current syllable
            syllables.append(current_syllable)  # Finalize the syllable
            current_syllable = ""  # Reset for the next syllable
        else:  # For spaces, punctuation, or other characters
            if current_syllable:  # Finalize any existing syllable
                syllables.append(current_syllable)
                current_syllable = ""
            syllables.append(unit)  # Add the unit as its own syllable

    # Add any remaining syllable
    if current_syllable:
        syllables.append(current_syllable)

    return syllables
