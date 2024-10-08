def snake_to_camel(string):
    words = string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

print(snake_to_camel("hello_world_example"))  
