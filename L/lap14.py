
text = "apple banana orange apple kiwi apple apple"

stg = input("찾을 문자열 입력: ")

word = ""
word_index = 0
count = 0
indices = []

i = 0
in_word = False

while i < len(text):
    char = text[i]
    
    if char != " ":
        word += char
        in_word = True
    else:
        if in_word:
            if word == stg:
                count +=1
                indices.append(word_index)
            word_index += 1
            word = ""
            in_word = False
    i += 1

    
    

    