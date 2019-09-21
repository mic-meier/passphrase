def load_dict(file):
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
