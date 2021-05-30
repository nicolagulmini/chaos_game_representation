import matplotlib.pyplot as plt
from scipy.stats import uniform

def cgr(dna_translated):
    dna_x = dna_translated[0]
    dna_y = dna_translated[1]
    length = len(dna_x) # also y
    x = [uniform.rvs()]
    y = [uniform.rvs()]
    for i in range(length):
        x.append(x[i] + 0.5*(dna_x[i]-x[i]))
        y.append(y[i] + 0.5*(dna_y[i]-y[i]))
    return [x, y]

def translate_dna(dna):
    dna_x = []
    dna_y = []
    for i in range(len(dna)):
        if dna[i] == 'A': 
            dna_x.append(0)
            dna_y.append(0)
        elif dna[i] == 'C': 
            dna_x.append(0)
            dna_y.append(1)
        elif dna[i] == 'G': 
            dna_x.append(1)
            dna_y.append(0)
        elif dna[i] == 'T': 
            dna_x.append(1)
            dna_y.append(1)
    return [dna_x, dna_y]

def main():
    dna = []
    corona = 'NC_045512.2'
    name = corona
    text = '.txt'
    image = '.png'
    with open(name+text) as file:
        read = file.read()
        for i in read:
            el = i.upper()
            if el == 'A' or el == 'C' or el == 'G' or el == 'T':
                dna.append(el)
            elif el == 'N':
                print('Reading end.')
    chaos_game_data = cgr(translate_dna(dna))
    plt.plot(chaos_game_data[0], chaos_game_data[1], '.k', markersize=0.2)
    plt.axis('Equal')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.savefig(name+image, dpi=400, transparent=True)
    
main()