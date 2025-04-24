from syllable_converter import convert_to_ipa, split_ipa_into_units
from syllable_converter import closest_chars, syllable_map
from syllable_converter import full_conversion

from vai import vai_syllabary
from vai import closest_consonant_mapping, closest_vowel_mapping

def convert_to_vai(text):
    vai_text = full_conversion(text, closest_consonant_mapping, closest_vowel_mapping, vai_syllabary)
    return vai_text

if __name__ == "__main__":
    text = "Niko Ross"
    vai_text = convert_to_vai(text)
    print(vai_text)