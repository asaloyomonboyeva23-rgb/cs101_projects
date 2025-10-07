character_name = input("enter the character's name: " )
character_class = input("enter the character's class: ")
home_realm = input("enter the character's home: ")
special_ability = input("enter the character's ability: ")
choosen_weapon = input("enter the character's weapon : ")

if character_name == "":
    character_name = "Unknown Character"
if character_class == "":
    character_class = " Unknown class"
if home_realm == "":
    home_realm = " unkown home" 
if special_ability == "":
    special_ability = " Unknown ability"
if choosen_weapon == "":
    choosen_weapon = " Unknowb ability" 

print(
"  ========================================\n"
"-- CHARACTER CREATION COMPLETE --\n"
"==========================================\n"

"Name:     " + character_name + "\n"
"Class:    " + character_class + "\n"
"home_Realm:    " + home_realm + "\n"

"Title:  " + character_name + " the " + character_class + " of " + home_realm + "\n"

"-------------------------------------------"

"Weapon of Choice: " + choosen_weapon + "\n"
"Special Ability: " + special_ability + "\n"
"========================================")