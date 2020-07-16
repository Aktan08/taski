"""
Write a script that takes
in a string and prints its length.
HINT:
Question: What do you mean by length?
Answer: The character count of a string.
Ex: 'hello!' # --> 6
"""

def prints_its_length(str):
    if str  == str[:1]:
        print(1)
    elif str  == str[:2]:
        print(2)
    elif str  == str[:3]:
        print(3)
    elif str  == str[:4]:
        print(4)
    elif str  == str[:5]:
        print(5)
    elif str  == str[:6]:
        print(6)
    elif str  == str[:7]:
        print(7)
    elif str  == str[:8]:
        print(8)
    elif str  == str[:9]:
        print(9)
    elif str  == str[:10]:
        print(10)
    elif str  == str[:11]:
        print(11)
    elif str  == str[:12]:
        print(12)
    elif str  == str[:13]:
        print(13)
    elif str  == str[:14]:
        print(14)
    elif str  == str[:15]:
        print(15)
    elif str  == str[:16]:
        print(16)
    else :
        print("toobig")
#input your letter
prints_its_length("a")

#second metod
def prints_its_length_second(string):
    print(len(string))
#input your second letter 
prints_its_length_second("asdf")