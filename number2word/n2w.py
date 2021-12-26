
numberMap = ("khong","mot","hai","ba","bon","nam","sau","bay","tam","chin","muoi")
my_map = {"1000000000" : "ty","1000000": "trieu", "1000" :"ngan","100":"tram","10":"muoi"}

def num2words(number):
    number = int(number)
    words = ""
    for key in my_map.keys():
        if ((number//int(key))>0):
            words += num2words(number//int(key)) + " " + my_map[key]
            number %= int(key)
    if(number<10 and number !=0):
        words += " " + numberMap[number]
    return words

def Number2Word(number):
    number = int(number)
    words = ""
    if ( (number//1000000000) > 0):
        words += Number2Word(number//1000000000) + " ty"
        number %= 1000000000
    if ( (number //1000000) >0):
        words += Number2Word(number//1000000) + " trieu"
        number %= 1000000
    if ( (number//1000) > 0):
        words += Number2Word(number//1000) + " ngan"
        number %= 1000
    if ((number//100)>0):
        words += Number2Word(number//100) +" tram"
        number %= 100
    if ((number//10)>0):
        words += Number2Word(number//10) + " muoi"
        number %= 10
    if(number<10 and number !=0):
        words += " " + numberMap[number]
    return words
def num2w(number):
    word = Number2Word(number)
    word = word.replace("mot muoi", "muoi")
    
def main():
    print(num2w(input()))

if __name__ == "__main__":
    main()
