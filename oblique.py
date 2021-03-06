import random

def blank_line(card_width, repeats=1):
    ''' Print one or more blank lines to console'''
    for repeat in range(repeats):
        print('')

def card_vert_edge(card_width, repeats=1):
    ''' Print one or more vertical card edges '''
    for repeat in range(repeats):
        print('|{}|'.format(' ' * card_width))

def card_horz_edge(card_width):
    ''' Print one or more horizontal card edges '''
    print('+{}+'.format('-' * card_width))

def display(card, card_width=40):
    '''Display a card on the console'''
    blank_line(card_width, repeats=4)
    card_horz_edge(card_width)
    card_vert_edge(card_width, repeats=3)

    # print the message
    for line in card:
        print('|{}|'.format(str.center(line, card_width)))
    if len(card) == 1:
        card_vert_edge(card_width)

    card_vert_edge(card_width, repeats=3)
    card_horz_edge(card_width)
    blank_line(card_width, repeats=5)

def draw_card(text_width=30):
    '''Draw a card from the deck.'''
    with open('strategies.txt', 'r') as f:
        rows = f.readlines()
    cards = [row.strip() for row in rows]

    # Set up empty card.
    # It will become an array of strings to print on the card.
    # e.g. ['This is first line,', 'and this is second']
    card = []
    line = ''

    # get a random line of words
    words = random.choice(cards).split(' ')
    # turn the raw words into rows
    while words:
        word = words.pop(0)
        # check that it's a word
        if not word.strip():
            continue
        newline = line + ' ' + word
        # break line if too long or starts with certain character
        if len(newline) > text_width or word[0] in ['(', '-']:
            card.append(line.strip())
            line = word
        else:
            line = newline.strip()
        # break line if ends with certain character
        if word[-1] in ['?', ';', ',', '.', '(']:
            card.append(line.strip())
            line = ''

    card.append(line)

    return card

def draw_many(draws=3):
    '''Draw multiple cards'''
    for counter in range(draws):
        print('{} of {}'.format(counter + 1, draws))
        card = draw_card()
        display(card)


def main():
    card = draw_card()
    display(card)

if __name__ == '__main__':
    main()
    #draw_many(draws=3)