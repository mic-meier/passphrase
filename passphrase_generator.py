import sys
from helpers import load_dict, generate_passphrase


def main():

    word_choices = load_dict('eff_large_wordlist.txt')

    if len(sys.argv) == 2:
        try:
            amount_of_words = int(sys.argv[1])
        except ValueError:
            print('Usage: integer expected')
            return 1

    elif len(sys.argv) > 2:
        print('Usage: Too many command line arguments')
        return 2

    else:
        while True:
            try:
                amount_of_words = abs(int(input('Of how many words should your passphrase consist? ')))
                break
            except ValueError:
                print('Please enter a positive whole number.')

    print(generate_passphrase(amount_of_words, word_choices))


if __name__ == '__main__':
    main()
