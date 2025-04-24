from syllable_converter import convert_to_ipa, split_ipa_into_units
from syllable_converter import closest_chars, syllable_map
from syllable_converter import full_conversion

from vai import vai_syllabary
from vai import closest_consonant_mapping as closest_consonant_mapping_vai
from vai import closest_vowel_mapping as closest_vowel_mapping_vai
from vai import ipa_consonants_vai, ipa_vowels_vai
from vai import diphthongs_vai, consonant_clusters_vai

from cherokee import cherokee_syllabary
from cherokee import closest_consonant_mapping as closest_consonant_mapping_cherokee
from cherokee import closest_vowel_mapping as closest_vowel_mapping_cherokee
from cherokee import ipa_consonants_cherokee, ipa_vowels_cherokee
from cherokee import diphthongs_cherokee, consonant_clusters_cherokee

def convert_to_vai(text):
    vai_text = full_conversion(text, closest_consonant_mapping_vai, closest_vowel_mapping_vai, vai_syllabary, ipa_consonants_vai, ipa_vowels_vai, diphthongs_vai, consonant_clusters_vai)
    return vai_text

def convert_to_cherokee(text):
    cherokee_text = full_conversion(text, closest_consonant_mapping_cherokee, closest_vowel_mapping_cherokee, cherokee_syllabary, ipa_consonants_cherokee, ipa_vowels_cherokee, diphthongs_cherokee, consonant_clusters_cherokee)
    return cherokee_text


if __name__ == "__main__":
    text = "quotient"
    vai_text = convert_to_vai(text)
    print(vai_text)

    print()

    cherokee_text = convert_to_cherokee(text)
    print(cherokee_text)
