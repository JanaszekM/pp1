import re

samogloski = ['a', 'e', 'i', 'y', 'o', 'u']
text = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."

def czestotliwosc():
    intext=[]
    for x in samogloski:
        
        intext= re.findall(x,text)
        print(f'samogloska {x} wystepuje w tekscie {len(intext)} razy. Czestotliwosc wynosi {len(intext)/len(text)} słów')
    
czestotliwosc()