def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(f"Number of words: {count_words(file_contents)}")
        print()
        
        count_dict = count_letters(file_contents)
 
        num_list = []
        for char in count_dict:
            num_list.append(count_dict[char])
            num_list.sort(reverse=True)

        for num in num_list:
            for char in count_dict:
                if count_dict[char] == num:
                    print(f"'{char}' was used {num} times")
            
            



def count_words(passage):
    output = 0
    words = passage.split()
    for word in words:
        output += 1
    return output
        
def count_letters(passage):
    output = {}
    for char in passage:
        if char.isalpha():
            char = char.lower()
            if char in output:
                output[char] += 1
            else:
                output[char] = 1
    return output 

main()