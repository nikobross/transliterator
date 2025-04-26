cherokee_syllabary = {
    "":     {"a": "Ꭰ", "e": "Ꭱ", "i": "Ꭲ", "o": "Ꭳ", "u": "Ꭴ", "ə̃": "Ꭵ"},
    "g":    {"a": "Ꭶ", "e": "Ꭸ", "i": "Ꭹ", "o": "Ꭺ", "u": "Ꭻ", "ə̃": "Ꭼ"},
    "k":    {"a": "Ꭷ", "e": "Ꭸ", "i": "Ꭹ", "o": "Ꭺ", "u": "Ꭻ", "ə̃": "Ꭼ"},
    "h":    {"a": "Ꭽ", "e": "Ꭾ", "i": "Ꭿ", "o": "Ꮀ", "u": "Ꮁ", "ə̃": "Ꮂ"},
    "l":    {"a": "Ꮃ", "e": "Ꮄ", "i": "Ꮅ", "o": "Ꮆ", "u": "Ꮇ", "ə̃": "Ꮈ"},
    "m":    {"a": "Ꮉ", "e": "Ꮊ", "i": "Ꮋ", "o": "Ꮌ", "u": "Ꮍ", "ə̃": "Ᏽ"},
    "n":    {"a": "Ꮎ", "e": "Ꮑ", "i": "Ꮒ", "o": "Ꮓ", "u": "Ꮔ", "ə̃": "Ꮕ"},
    "hn":   {"a": "Ꮏ"},
    "nah":  {"a": "Ꮐ"},
    "qu":   {"a": "Ꮖ", "e": "Ꮗ", "i": "Ꮘ", "o": "Ꮙ", "u": "Ꮚ", "ə̃": "Ꮛ"},
    "s":    {"": "Ꮝ", "a": "Ꮜ", "e": "Ꮞ", "i": "Ꮟ", "o": "Ꮠ", "u": "Ꮡ", "ə̃": "Ꮢ"},
    "d":    {"a": "Ꮣ", "e": "Ꮥ", "i": "Ꮧ", "o": "Ꮩ", "u": "Ꮪ", "ə̃": "Ꮫ"},
    "t":    {"a": "Ꮤ", "e": "Ꮦ", "i": "Ꮨ", "o": "Ꮩ", "u": "Ꮪ", "ə̃": "Ꮫ"},
    "dl":   {"a": "Ꮬ", "e": "Ꮮ", "i": "Ꮯ", "o": "Ꮰ", "u": "Ꮱ", "ə̃": "Ꮲ"},
    "tl":   {"a": "Ꮭ", "e": "Ꮮ", "i": "Ꮯ", "o": "Ꮰ", "u": "Ꮱ", "ə̃": "Ꮲ"},
    "ts":   {"a": "Ꮳ", "e": "Ꮴ", "i": "Ꮵ", "o": "Ꮶ", "u": "Ꮷ", "ə̃": "Ꮸ"},
    "w":    {"a": "Ꮹ", "e": "Ꮺ", "i": "Ꮻ", "o": "Ꮼ", "u": "Ꮽ", "ə̃": "Ꮾ"},
    "y":    {"a": "Ꮿ", "e": "Ᏸ", "i": "Ᏹ", "o": "Ᏺ", "u": "Ᏻ", "ə̃": "Ᏼ"},
}

closest_consonant_mapping = {
    "θ": "t",     # voiceless dental approximated by "t"
    "ð": "d",     # voiced dental approximated by "d"
    "f": "h",     # voiceless labiodental approximated by "h"
    "v": "w",     # voiced labiodental approximated by "w"
    "z": "s",     # voiced alveolar fricative approximated by "s"
    "ʃ": "s",     # voiceless postalveolar fricative approximated by "s"
    "ʒ": "s",     # voiced postalveolar fricative approximated by "s"
    "tʃ": "ts",   # affricate already has Cherokee syllable: "ts"
    "dʒ": "ts",   # voiced affricate approximated by "ts"
    "ɫ": "l",     # velarized "l" approximated by plain "l"
    "ŋ": "n",     # velar nasal approximated by "n"
    "ɹ": "l",     # American English 'r' approximated by "l" or "d"
    "r": "l",     # American English 'r' approximated by "l" or "d"
    "j": "y",     # palatal glide matches Cherokee "y"
    "ʧ": "ts",  # voiceless postalveolar affricate approximated by "ts"
    "ʤ": "ts",  # voiced postalveolar affricate approximated by "ts"
    "b": "d",     # voiced bilabial approximated by "p"
    "p": "t",     # voiceless bilabial approximated by "t"
}

closest_vowel_mapping = {
    "ɪ": "i",     # lax i approximated by "i"
    "ʊ": "u",     # lax u approximated by "u"
    "ə": "ə̃",     # schwa approximated by Cherokee "v"
    "ɝ": "ə̃",     # rhotacized schwa approximated by "v"
    "ɔ": "o",     # open-mid back rounded approximated by "o"
    "æ": "a",     # near-open front unrounded approximated by "a"
    "ɑ": "a",     # open back unrounded approximated by "a"
    "eɪ": "e",    # diphthong approximated by "e"
    "aɪ": "a",    # diphthong approximated by "a"
    "aʊ": "a",    # diphthong approximated by "a"
    "ɔɪ": "o",    # diphthong approximated by "o"
    "oʊ": "o",    # diphthong approximated by "o"
    "ɛ": "e",     # open-mid front unrounded approximated by "e"
}

ipa_consonants_cherokee = ["p", "b", "t", "d", "k", "g", "θ", "ð", "f", "v", "s", "z", "ʃ", "ʒ", "tʃ", "dʒ", "w", "ɫ", "m", "n", "ŋ", "ɹ", "j", "h", "l", "r", "hn", "nah", "qu", "dl", "tl", "ts", "ʧ", "ʤ", "y"]
ipa_vowels_cherokee = ["i", "u", "ɪ", "ʊ", "ə", "ɛ", "ɝ", "ɔ", "æ", "ɑ", "eɪ", "aɪ", "aʊ", "ɔɪ", "oʊ", "a", "e"]
diphthongs_cherokee = ["eɪ", "aɪ", "aʊ", "ɔɪ", "oʊ"]
consonant_clusters_cherokee = ["tʃ", "dʒ", "hn", "nah", "qu", "dl", "tl", "ts"]