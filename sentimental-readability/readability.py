from cs50 import get_string



def main():
      text_sen = get_string("Text: ")

      letters = count_letters(text_sen)
      words = count_words(text_sen)
      sentences = count_sentences(text_sen)
      level = calculate_colemanLaiuIndex(letters, words, sentences)

      if level < 1:
          print("Before Grade 1")
      elif level > 16:
          print("Grade 16+")
      else:
          print(f"Grade {round(level)}")


# coleman laiu index calculator
def calculate_colemanLaiuIndex(l, w, s):
    index = float(0.0)
    L = float(l / w * 100.0)
    S = float(s / w * 100.0)
    index = round((0.0588 * L) - (0.296 * S) - 15.8)
    return float(index)


# count letters
def count_letters(s):
    counter = 0
    for char in s:
        if char.isalpha():
            counter += 1
    return counter


# count words
def count_words(s):
    counter = 0
    for char in s:
        if char == " ":
            counter += 1
    if counter > 0:
        counter += 1
    return counter


# counts sentences
def count_sentences(s):
    counter = 0
    counter += s.count('!')
    counter += s.count('.')
    counter += s.count('?')

    return counter


main()
