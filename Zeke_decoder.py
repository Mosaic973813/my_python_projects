MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

MORSE_TO_TEXT = {v: k for k, v in MORSE_CODE.items()}

def encode(text):
    encoded_words = []
    for word in text.upper().split(" "):  # split by spaces between words
        encoded_letters = [MORSE_CODE[letter] for letter in word if letter in MORSE_CODE]
        encoded_words.append(" ".join(encoded_letters))  # join letters with single space
    return "   ".join(encoded_words)  # join words with triple space

def decode(morse):
    decoded_words = []
    for word in morse.split("   "):  # split into words
        decoded_letters = [MORSE_TO_TEXT[letter] for letter in word.split() if letter in MORSE_TO_TEXT]
        decoded_words.append("".join(decoded_letters))
    return " ".join(decoded_words)

choice = input("Type 'encode' to convert text to Morse or 'decode' to convert Morse to text: ").strip().lower()

if choice == "encode":
    text = input("Enter text: ")
    print("Morse code:", encode(text))
elif choice == "decode":
    morse = input("Enter Morse code (use spaces between letters and 3 spaces between words): ")
    print("Text:", decode(morse))
else:
    print("Invalid choice.")