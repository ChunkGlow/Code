class MyString:

    my_str = input("Enter a string: ")
    
    def __init__(self, str):
        self.str = str
        reversed_word = MyString.my_str[::-1]
     

stringText = MyString.my_str
reversedText = MyString.my_str[::-1]

for MyString.my_str in stringText:
    print(f"Original String: {stringText}")
    print(f"Reversed String: {reversedText}")



