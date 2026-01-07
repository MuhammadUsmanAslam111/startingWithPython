# task 2 to count word frequency in a string
input_string = input("Enter a string: ")
list1 = input_string.split()
word_count = {}
for word in list1:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)