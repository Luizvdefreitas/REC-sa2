
pergunta = int(input("Digite a quantidade de horas que deseja converter em segundos:"))

horas_segundos = pergunta * (3600)

if pergunta > 0:

    print("R:", pergunta, "hora tem", horas_segundos, "segundos")

else:
    print("Número inválido")