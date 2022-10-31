#define a string with atleast 3 words

string = "I love typing"
print(string[0])
print(string[-1])

my_str = "I love typing"
word_list = my_str.split()  # list of words

# first word and last word
word_list[0], word_list[-1]


my_str = "I love typing"
word_list = my_str.split()  

# first word and last word
print(word_list[0], word_list[-1])


str = "This sentence has 27 chars."

for c in str:
    print(f"({c})", end = "")


str = " This sentence has 27 chars."


"""
for i in range (5):
    print(str[i])
for i in range(7):
    print(str[i])
    
for i in range (1, 7):
    print(str[i])
"""
print (range(len(str)))

print ()

for i in range (0, 27):
    print(str[i], end = "")


# using a for loop
str = "This sentence has 27 chars." [::-1]

for i in str:
    print(i, end = "")

#using a function
def reverse (i):
    return i[::-1]

str = reverse ("This sentence has 27 chars.")
print(f"{str}")

#negative indexing
str = "This sentence has 27 chars."
print (str [::-1])

#join method
str = "This sentence has 27 chars."
reversedstr = "".join(reversed(str))
print(reversedstr)

for i in range(20):
    #print ("X"*i)
    #print ("X"*(2*i))
    #print ("X"*i+"O"*i)
    print("X" * i)
    print("X" * (2 * i))
    print("X" * i + "o" * i)

# Define the list to try and find certain elements
std = ["Ali", 1, 2.5, "Elif", 2, 3.0]
print(std[0])

print(std[-1])

print(type(std[2]))

print(std[3])

print(std[3][2])

print(std[0 + 3])


def name_digit():
    num = int(input( "Enter a number between 0-9 : "))
    num_digits = ("zero", "One", "Two", "Three", "Four", "Five",
                  "six", "Seven", "Eight", "Nine")
    print (f"The name of digit {num} is {num_digits[num]}")
    

name_digit()


def phrase():
    
    sentence = input("Enter your phrase:")
    words = sentence.split()
   
    for i in words:
        print(f"{i} =>", {len(i)})

phrase()

def main():

    for i in range(255 +1):
        print (f" {i} =>", chr(i))

main()











