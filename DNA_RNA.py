class RNA:
    def __init__(self, seq: str):
        self.seq = seq.upper()
        for base in self.seq:
            if base == 'T':
                raise Exception('RNA does not contain T, only DNA does')
            elif base not in ['A', 'T', 'G', 'C', 'U']:
                raise Exception('This is not nucleic acid')
            self.complement = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}

    def gc_content(self):
        c = self.seq.count('C')
        g = self.seq.count('G')
        return (c + g)/len(self.seq) * 100

    def reverse_complement(self):
        reverse = [el for el in self.seq[::-1]]
        for base in range(len(reverse)):
            reverse[base] = self.complement[reverse[base]]
        return ''.join(reverse)

    def __iter__(self):
        return self


class DNA:
    def __init__(self, seq: str):
        self.seq = seq.upper()
        for base in self.seq:
            if base == 'U':
                raise Exception('DNA does not contain U, only RNA does')
            elif base not in ['A', 'T', 'G', 'C', 'U']:
                raise Exception('This is not nucleic acid')
            self.complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    def gc_content(self):
        c = self.seq.count('C')
        g = self.seq.count('G')
        return (c + g)/len(self.seq) * 100

    def reverse_complement(self):
        reverse = [el for el in self.seq[::-1]]
        for base in range(len(reverse)):
            reverse[base] = self.complement[reverse[base]]
        return ''.join(reverse)

    def transcribe(self):
        transcription = self.seq.replace('T', 'U')
        return RNA(transcription)
        # транскрипция последовательности оригинального объекта

    def __iter__(self):
        return self


