from random import randrange


class Alpha():

    def foo(self):
        return 'bar'


def roll_dice(rolls, line_break):
    """
        Simulates the rolling of a dice
        in a nicely formatted, tabular output.
    """
    for i in range(1, rolls + 1):
        face = randrange(1, 7)

        # Print newline every `line_break` rolls.
        if i % line_break != 0:
            print(face, end=' | ')
        else:
            print(face)


print('Invoking foo():', Alpha().foo(), end='\n\n')

roll_dice(25, 5)