print('lista zakupow')
lista_zakupow = {
    'piekarnia': ['chleb', 'bułki', 'pączek'],
    'warzywniak': ['marchew', 'seler', 'rukola'],
    'metalowy': ['śrubki', 'młotek']
    'kiosk': ['gazeta', 'papierosy']
}
count = 0
for sklep, towar in lista_zakupow.items():
    print('Idę do sklepu:', sklep.title(), 'i kupuję:', str.title((' '.join(towar))))
    if isinstance(towar, list):
        count += len(towar)
print('W sumie kupuję', count, 'produktów')
print("Łubu dubu, łubu dubu, niech nam żyje prezes naszego klubu")
