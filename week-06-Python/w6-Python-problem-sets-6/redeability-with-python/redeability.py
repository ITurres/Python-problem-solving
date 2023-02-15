def main():
    user_text = input("Text: ")
    text_length = len(user_text)
    letters = count_letters(text_length, user_text)
    words = count_words(text_length, user_text)
    sentences = count_sentences(text_length, user_text)
    grade = formula(letters, words, sentences)

    if grade >= 16:
        print("Grade 16+")
    elif grade <= 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


def count_letters(text_length, text):
    n_letters = 0
    for char in range(text_length):
        if not text[char].isspace() and text[char].isalpha():
            # printf(text[char])
            n_letters += 1
    # print(f"n_letters {n_letters}")
    return n_letters


def count_words(text_length, text):
    n_words = 1
    for char in range(text_length):
        if text[char].isspace():
            n_words += 1
    # print(f"n_words {n_words}")
    return n_words


def count_sentences(text_length, text):
    n_sentences = 0
    for char in range(text_length):
        if text[char] == "." or text[char] == "!" or text[char] == "?":
            n_sentences += 1
    # print(f"n_sentences {n_sentences}")
    return n_sentences


def formula(letters, words, sentences):
    # print(f"letters: {letters}, words: {words}, sentences: {sentences}")
    L = float(letters) / float(words) * 100
    S = float(sentences) / float(words) * 100
    # print(f"L = {L}")
    # print(f"S = {S}")
    return round(0.0588 * L - 0.296 * S - 15.8)


if __name__ == "__main__":
    main()
