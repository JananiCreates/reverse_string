# Reverse words or entire string – user's choice

def reverse_string(text, by_word=False):
    if by_word:
        words = text.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words
    else:
        return text[::-1]

text = input("Enter a string: ")
choice = input("Reverse whole string or word-by-word? (type: string/words): ").strip().lower()

if choice == "words":
    result = reverse_string(text, by_word=True)
else:
    result = reverse_string(text)

print("Reversed Output:", result)
