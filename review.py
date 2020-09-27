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


def main(args):
    # run find_anagrams() on first argument filename
    if len(args) < 1:
        print("Please specify a word file!")
        sys.exit(1)

    # Open the file that was placed an argument
    #   when invoked
    #   Ex: python anagrams.py words/short.txt
    with open(args[0]) as f:
        # Read each line of the file and
        #   split the words up
        # Ex: able -> ["a", "b", "l", "e"]
        words = f.read().split()
    # Use the find_anagrams function to place
    #   the sorted word as a key and the
    #   anagram words as a value
    #   Ex: ('abel': ['abel', 'able'])
    anagram_dict = find_anagrams(words)
    for k, v in anagram_dict.items():
        print(k, v)
