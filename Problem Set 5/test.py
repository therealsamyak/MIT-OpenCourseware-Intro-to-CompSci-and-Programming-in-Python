import string


phrase = "hi           jeff!"
phrase = phrase.split()
phrase = " " +  " ".join(phrase)
print(phrase)




def is_phrase_in(text):
    phrase = "purple cow"
    phrase = phrase.lower()
    new_phrase = ""
    text = text.lower()
    new_text = ""

    for character in phrase:
        if character in string.punctuation:
            new_phrase += " "
        else:
            new_phrase += character
    
    for character in text:
        if character in string.punctuation:
            new_text += " "
        else:
            new_text += character

    print((new_phrase, new_text))
    new_phrase = new_phrase.split()
    new_phrase = " ".join(new_phrase) + " "
    new_text = new_text.split()
    new_text = " ".join(new_text) + " "

    return (new_phrase, new_text)

print(is_phrase_in("purple$^%&%&$*#(*cow"))