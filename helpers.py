from dice import D6


def load_dict(file):
    """
    Loads a file with key - word combinations into a dict.
    :param file: file path
    :type file: .txt file with key and word separated by a tab
    :return: dictionary with keys and words as values
    :rtype: dict
    """
    phrases = {}

    with open(file) as word_list:
        for line in word_list:
            # Strip lines of newline character
            line = line.rstrip('\n')
            # Split lines at tab character
            words = line.split('\t')
            # Add to dict
            phrases[words[0]] = words[1]

    return phrases


def dice_throw(n):
    """
    Generates dictionary key by throwing n dice
    :param n: Amount of dice to be thrown
    :type n: int
    :return: dice throw result, usable as dictionary key
    :rtype: str
    """
    key = []
    for i in range(n):
        die = D6()
        key.append(str(die.value))
    return ''.join(key)


def generate_passphrase(n, word_choices):
    """
    Generates passphrase, consisting of n words
    :param n: Number of words the passphrase should consist of
    :type n: int
    :param word_choices: Dictionary of possible words
    :type word_choices: dict
    :return: Passphrase
    :rtype: str
    """
    pass_phrase_list = []

    for i in range(n):
        key = dice_throw(5)
        word = word_choices[key]
        pass_phrase_list.append(word)

    pass_phrase = ' '.join(pass_phrase_list)

    return pass_phrase
