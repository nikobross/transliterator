class Unit:
    def __init__(self, type, consonant="", vowel="", symbol=""):
        self.type = type
        self.consonant = consonant
        self.vowel = vowel
        self.symbol = symbol

    def is_CV(self):
        return self.type == "CV"
    
    def is_V(self):
        return self.type == "V"
    
    def is_C(self):
        return self.type == "C"
    
    def is_unique_symbol(self):
        return self.type == "unique symbol"
    
    def is_syllable(self):
        return self.type in ["CV", "C", "V"]

    def __str__(self):
        if self.type == "CV":
            return f"{self.consonant}{self.vowel}"
        elif self.type == "C":
            return self.consonant
        elif self.type == "V":
            return self.vowel
        else:
            return self.symbol