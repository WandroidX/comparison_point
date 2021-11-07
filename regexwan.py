def regular(text):
    alfa=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o", "p", "q", "r", "s", "t", "u", "v", "w","x","y","z",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L',"M", 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',0] 

    alfanum=[alfa+["1","2","3","4","5","6","7","8","9"]]
    numeric=["1","2","3","4","5","6","7","8","9"]
    divtext=[]
    wordsearch=[]

    for n in range(0,len(text)):
        divtext.append(text[n])
    
    #comprobar si text es solo letras o alfa
    for y in range(0,len(divtext)):
        for x in range(0,len(alfa)):
            if divtext[y]==alfa[x]:
                wordsearch.append(1)
                break
            elif x==54:
                wordsearch.append(0)



regular("hello35alv4")
