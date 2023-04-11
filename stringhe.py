# String exercises
nome = "Mario"
print(nome.upper())
print(nome.replace("o", "a"))
frase = "ciao come stai?"
parole_frase = frase.split()
# print(parole_frase)
# print(parole_frase.__len__())
# print("la frase inizia con \"ciao\"?", end=" ")
# print(frase.startswith("ciao"))
cognome = "Rossi"
nome_completo = nome + " " + cognome
anni = 45
greetings = " ciao {}, {} anni, come stai?"
print(greetings.strip().format(nome_completo, str(anni)))
print(frase[-2].upper())
print(frase[-2:])
print(frase[3:6])
meta_frase = int(frase.__len__() / 2)
print(frase[:meta_frase])
print(frase[meta_frase:])
