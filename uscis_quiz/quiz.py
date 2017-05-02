from itertools import cycle
from random import shuffle

from uscis_quiz.questions import questions


def get_command():
    return input('')


def display_question(item):
    print('-' * 20, '\n')
    print('Q:', item['q'])


def display_answers(item):
    print('A:')
    for answer in item['a']:
        print(answer)
    print()


def main():
    shuffle(questions)
    questions_cycle = cycle(questions)

    print('q for quit, anything else will continue the quiz')

    show_question = True
    item = None

    while True:
        command = get_command()
        if command == 'q':
            break

        if show_question:
            item = next(questions_cycle)
            display_question(item)
        else:
            display_answers(item)

        show_question = not show_question


if __name__ == '__main__':
    main()
