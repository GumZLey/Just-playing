import speech_recognition as sr
import timeit
start = timeit.default_timer()
#---------------------------------------------
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Say something")
    audio = r.listen(source)
my_string = r.recognize_google(audio, None, 'th')
print(my_string)
'''
operator_con = ["+", "-", "*", "/", ]
operator = ""
container = list(my_string).copy()
try :
    for i in container:
        if i in operator_con:
            newcon = my_string.split(i)
            operator = i
except:
    pass

newcon = list(map(int, newcon))
'''
###############

container = my_string.split(" ")
num1 = int(container[0])
num2 = int(container[2])
if container[1] == "+":
    print(num1 + num2)
elif container[1] == "-":
    print(num1 - num2)
elif container[1] == "*":
    print(num1 * num2)
elif container[1] == "/":
    print(num1 / num2)




################
'''
if operator == "+":
    print(newcon[0] + newcon[1])
elif operator == "-":
    print(newcon[0] - newcon[1])
elif operator == "*":
    print(newcon[0] * newcon[1])
elif operator == "/":
    print(newcon[0] / newcon[1])

'''


#---------------------------------------------
stop = timeit.default_timer()
print(stop - start)
