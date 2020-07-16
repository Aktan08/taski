"""You are given a string.
In the first line, print the third character of this string.
In the second line, print the second to last character of this string.
In the third line, print the first five characters of this string.
In the fourth line, print all but the last two characters of this string.
In the fifth line, print all the characters of this string with even indices (На английском языке что бы Вы научились понимать remember indexing starts at 0, so the characters are displayed starting with the first).
In the sixth line, print all the characters of this string with odd indices (На английском языке что бы Вы научились понимать i.e. starting with the second character in the string).
In the seventh line, print all the characters of the string in reverse order.
In the eighth line, print every second character of the string in reverse order, starting from the last one.
In the ninth line, print the length of the given string."""
#1

first_string = "In the first line, print the third character of this string."
print(first_string[2])

#2

second_string = "In the second line, print the second to last character of this string."
print(second_string[-2])

#3
third_string = "In the third line, print the first five characters of this string."
print (third_string[:5])

#4 

fourth_string = "In the fourth line, print all but the last two characters of this string."
print (fourth_string[:-2])

#5

fivs_string = "In the fifth line, print all the characters of this string with even indices (На английском языке что бы Вы научились понимать remember indexing starts at 0, so the characters are displayed starting with the first)."
s = fivs_string[0]+fivs_string[2]+fivs_string[4]+fivs_string[8]+fivs_string[10]+fivs_string[12]+fivs_string[14]+fivs_string[16]+fivs_string[18]+fivs_string[20]+fivs_string[22]+fivs_string[24]+fivs_string[26]+fivs_string[28]+fivs_string[30]+fivs_string[32]+fivs_string[34]+fivs_string[36]+fivs_string[38]+fivs_string[40]+fivs_string[42]+fivs_string[44]+fivs_string[46]+fivs_string[48]+fivs_string[50]+fivs_string[52]+fivs_string[54]+fivs_string[58]+fivs_string[60]+fivs_string[62]+fivs_string[64]+fivs_string[66]+fivs_string[68]+fivs_string[70]+fivs_string[72]+fivs_string[74]+fivs_string[76]+fivs_string[78]+fivs_string[80]+fivs_string[82]+fivs_string[84]+fivs_string[86]+fivs_string[88]+fivs_string[90]+fivs_string[92]+fivs_string[94]+fivs_string[96]+fivs_string[98]+fivs_string[100]+fivs_string[102]+fivs_string[104]+fivs_string[108]+fivs_string[110]+fivs_string[112]+fivs_string[114]+fivs_string[116]+fivs_string[118]+fivs_string[120]+fivs_string[122]+fivs_string[124]+fivs_string[126]+fivs_string[128]+fivs_string[130]+fivs_string[132]+fivs_string[134]+fivs_string[136]+fivs_string[138]+fivs_string[140]+fivs_string[142]+fivs_string[144]+fivs_string[146]+fivs_string[148]+fivs_string[150]+fivs_string[152]+fivs_string[154]+fivs_string[156]+fivs_string[158]+fivs_string[160]+fivs_string[162]+fivs_string[164]+fivs_string[166]+fivs_string[168]+fivs_string[170]+fivs_string[172]+fivs_string[174]+fivs_string[176]+fivs_string[178]+fivs_string[180]+fivs_string[182]+fivs_string[184]+fivs_string[186]+fivs_string[188]+fivs_string[190]+fivs_string[192]+fivs_string[194]+fivs_string[196]+fivs_string[198]+fivs_string[200]+fivs_string[212]+fivs_string[214]
print (s)

#6

def six_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(six_string("In the sixth line, print all the characters of this string with odd indices (На английском языке что бы Вы научились понимать i.e. starting with the second character in the string)."))

#7

seven = "In the seventh line, print all the characters of the string in reverse order."
seven_string = seven[-1]+seven[-2]+seven[-3]+seven[-4]+seven[-5]+seven[-6]+seven[-7]+seven[-8]+seven[-9]+seven[-10]+seven[-11]+seven[-12]+seven[-13]+seven[-14]+seven[-15]+seven[-16]+seven[-17]+seven[-18]+seven[-19]+seven[-20]+seven[-21]+seven[-22]+seven[-23]+seven[-24]+seven[-25]+seven[-26]+seven[-27]+seven[-28]+seven[-29]+seven[-30]+seven[-31]+seven[-32]+seven[-33]+seven[-34]+seven[-35]+seven[-36]+seven[-37]+seven[-38]+seven[-39]+seven[-40]+seven[-41]+seven[-42]+seven[-43]+seven[-44]+seven[-45]+seven[-46]+seven[-47]+seven[-48]+seven[-49]+seven[-50]+seven[-51]+seven[-52]+seven[-53]+seven[-54]+seven[-55]+seven[-56]+seven[-57]+seven[-58]+seven[-59]+seven[-60]+seven[-61]+seven[-62]+seven[-63]+seven[-64]+seven[-65]+seven[-76]+seven[-67]+seven[-68]+seven[-69]+seven[-70]+seven[-71]+seven[-72]+seven[-73]+seven[-74]+seven[-75]+seven[-76]+seven[-77]
print(seven_string)

#8

def eighth_string(string):
  result = "" 
  for i in range(len(string)):
    if i % 2 == 0:
      result = result + string[-i]
  return result
print (eighth_string ( "In the eighth line, print every second character of the string in reverse order, starting from the last one.")[1:])

#9 

h = "In the ninth line, print the length of the given string."
print (len(h))