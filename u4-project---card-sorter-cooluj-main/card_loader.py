import csv
 
def get_cards():
    cards = []

    with open("clashcards.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            card = {}
            index = 0
            for field_index in range(len(fields)):
                if len(fields[field_index]) > 0:
                    card[fields[field_index]] = row[index]
                index += 1
            cards.append(card)
    return cards