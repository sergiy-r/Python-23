"""
Для кожного слова підрахуйте
cкільки разів воно зустрічалось в цьому тексті.
Little girl, little girl Why are you crying? Inside your restless soul your heart is dying Little one, little one Your soul is purging Of love and razor blades Your blood is surging Runaway From the river to the street And find yourself with your face in the gutter Your a stray for the salvation army There is no place like home When you got no place to go Little girl, little girl Your life is calling The charlatans and saints of your abandon Little one little one The sky is falling The lifeboat of deception is now sailing In the wake all the way No rhyme or reason Your bloodshot eyes Will show your heart of treason Little girl little girl You dirty liar You're just a junkie Preaching to the choir Runaway To your lost tranquility And find yourself with your face in the gutter Your a stray for the dregs of humanity There is no place like home When you got no place to go The traces of blood Always follow you home Like the Mascara tears From your getaway Your walking with blisters And running with shears So unholy. Sister of grace. Runaway From the river to the street And find yourself with your face in the gutter You're a stray for the salvation army There is no place like home When you got no place to go
"""
import re

input_text = "Little girl, little girl Why are you crying? Inside your restless soul your heart is dying Little one, little one Your soul is purging Of love and razor blades Your blood is surging Runaway From the river to the street And find yourself with your face in the gutter Your a stray for the salvation army There is no place like home When you got no place to go Little girl, little girl Your life is calling The charlatans and saints of your abandon Little one little one The sky is falling The lifeboat of deception is now sailing In the wake all the way No rhyme or reason Your bloodshot eyes Will show your heart of treason Little girl little girl You dirty liar You're just a junkie Preaching to the choir Runaway To your lost tranquility And find yourself with your face in the gutter Your a stray for the dregs of humanity There is no place like home When you got no place to go The traces of blood Always follow you home Like the Mascara tears From your getaway Your walking with blisters And running with shears So unholy. Sister of grace. Runaway From the river to the street And find yourself with your face in the gutter You're a stray for the salvation army There is no place like home When you got no place to go"
clean_text =  re.sub(r'[^\w\s]', "", input_text).lower().split()
# print(clean_text)

my_dict = {}
counter = 0

for word in clean_text:
    my_dict[word] = my_dict.get(word,0) +1

my_key_list = sorted(my_dict, key=my_dict.get)

for el in my_key_list:
    print(el, my_dict[el])

new_dict = {}
for key, val in my_dict.items():
    if new_dict.get(val) == None:
        new_dict[val] = [key]
    else:
        new_dict[val].append(key)

print(new_dict)