import re
while True :
    input_text = input("enter something to extract from or click 'q' to quit: ")
    if input_text == "q" :
        break
    else:
        a = re.findall(r'\w+@\w+.\w+', input_text)
        print("here are your emails: ")
        for i in a :
            print(i)