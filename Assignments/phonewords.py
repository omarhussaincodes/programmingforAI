# Create a Python application that will convert a PhoneWord or Vanity Number
# (https://en.wikipedia.org/wiki/Phoneword) to a set of numbers. An example would be taking 1-800-HOLIDAY
# and getting 18004654329.

phoneword_dict = {
    ('a', 'b', 'c'): 2,
    ('d', 'e', 'f'): 3,
    ('g', 'h', 'i'): 4,
    ('j', 'k', 'l'): 5,
    ('m', 'n', 'o'): 6,
    ('p', 'q', 'r', 's'): 7,
    ('t', 'u', 'v'): 8,
    ('w', 'x', 'y', 'z'): 9
}

def get_magic_number(letter):
    for key, value in phoneword_dict.items():
        if (key.count(letter) != 0):
            return value
    return ""

def convert_phoneword(user_entered_input):
    result = ""
    for element in user_entered_input:
        if (element.isdigit()):
            result += element
        else:
            keypadnum = get_magic_number(element.lower())
            result += (str(keypadnum))
    return int(result)

user_entered_ph = input("Enter your phone number please:")

print("Phoneword:", convert_phoneword(user_entered_ph))
