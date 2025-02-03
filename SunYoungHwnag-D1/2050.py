str_sentence = list(input())

def convert_to_num(sen):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    results = [str(alphabets.index(w)+1) for w in sen if w in alphabets]
    return " ".join(results)
 
print(convert_to_num(str_sentence))