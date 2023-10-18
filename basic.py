class BasicStringFunctions:

    @staticmethod
    def string_length(input_string):
        length = 0
        for character in input_string:
            length += 1
        return length
    
    @staticmethod  #give a substring from string. Start from 0 to until it found a delimeter.
    def substring_extractor_till_delimeter(string, delimeter): 
        substring = ''
        for index in range(BasicStringFunctions.string_length(string)):
            if string[index] == delimeter:
                return substring
            substring += string[index]


class BasicListFunctions:
    @staticmethod
    def length_of_list(list_name):
        length = 0
        for _ in list_name:
            length += 1
        return length
        