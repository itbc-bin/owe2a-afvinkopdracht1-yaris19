# Naam: Yaris van Thiel
# Datum: 15-11-2018
# Versie: 1.0


def main():
    try:
        bestand = "alpaca.fasta"
        headers, seqs = lees_inhoud(bestand)
        zoekwoord = input("Geef een zoekwoord op: ")
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:", headers[i])
                check_is_dna = Is_Dna(seqs[i])
                if check_is_dna:
                    print("Sequentie is DNA")
                    knipt(seqs[i])
                else:
                    print("Sequentie is geen DNA. Er is iets fout gegaan.")
        else:
            print('Het zoekwoord komt niet voor in de headers')
    except TypeError:
        print('Het bestand heeft het verkeerde formaat, gebruik ".fasta"')


def lees_inhoud(bestands_naam):
    try:
        bestand = open(bestands_naam)
        if bestands_naam.endswith('.fasta'):
            headers = []
            seqs = []
            seq = ""
            for line in bestand:
                line = line.strip()
                if line.startswith('>'):
                    if seq != "":
                        seqs.append(seq)
                        seq = ""
                    headers.append(line)
                else:
                    seq += line.strip()
            seqs.append(seq)
            return headers, seqs
    except FileNotFoundError:
        print('Het opgegeven bestand bestaat niet')


def Is_Dna(seq):
    try:
        dna = False
        a = seq.count("A")
        t = seq.count("T")
        c = seq.count("C")
        g = seq.count("G")
        total = a+t+c+g
        if total == len(seq):
            dna = True
        return dna
    except ZeroDivisionError:
        print('Er is gedeeld door 0 (nul), dit kan niet')


def knipt(alpaca_seq):
    bestand = open("enzymen.txt")
    for line in bestand:
        naam, seq = line.split(" ")
        seq = seq.strip().replace("^", "")
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")


main()
