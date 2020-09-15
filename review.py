def alphabetize(string):
    """Returns alphabetized version of the string."""
    return "".join(sorted(string.lower()))


def find_anagrams(words):
    """
    Returns a dictionary with keys that are alphabetized words and values
    that are all words that, when alphabetized, match the key.
    Example:
    {'dgo': ['dog'], 'act': ['cat', 'act']}
    """

    anagrams = {}
    for word in words:
        # setdefault() -> Inserts a key and sets a default value
        # make each word a key
        anagrams.setdefault(alphabetize(word), [])
        # If the word is not a value
        if word not in anagrams[alphabetize(word)]:
            # Go through individual keys' value -> Append word into
            #   empty list
            anagrams[alphabetize(word)].append(word)
    return anagrams
