# word_pattern_generator.py
# UNIQUE PROGRAM: WORD PATTERN GENERATOR ✨

def word_pattern(sentence):
    """
    Generates a staircase pattern for each word.
    Example:
    Input: 'hello world'
    Output:
    h
    he
    hel
    hell
    hello

    w
    wo
    wor
    worl
    world
    """
    words = sentence.split()

    for w in words:
        for i in range(1, len(w) + 1):
            print(w[:i])
        print()  # empty line between words


if __name__ == "__main__":
    print("✨ Word Pattern Generator ✨")
    print("----------------------------")

    text = input("Enter a sentence: ")
    word_pattern(text)
