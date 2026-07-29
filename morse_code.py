morse = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",

}
choice = input("Do you need to translate your text into morse code or morse code to text?(text/morse): ")
if choice == "text":
    
    text = input("Your text: ").upper()
    text_to_morse = { v: k for k, v in morse.items()}
    for letter in text:
        if letter == " ":
            print("/", end=" ")
        else:
            print(text_to_morse[letter], end = " ")

elif choice == "morse":

    morse_code = input("Morse code: ")

    splitted_morse = morse_code.split()

    for letter in splitted_morse:
        print(morse[letter], end=" ")
