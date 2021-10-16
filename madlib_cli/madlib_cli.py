import re

def welcome_func():
    print(
        """
                                 Welcome to madlib game !
after this messege a story will appear to you, the app will ask you to give some words and adjectives, we will make your own story
    
"""
    )

def read_template(path):
    with open(path) as file:
        text=file.read()
        stripped_text=text.strip()
    return stripped_text


def parse_template(string):
    spilt_file_list=re.findall(r"\{(.*?)\}",string)
    # print(spilt_file_list)
    spilt_string=re.sub(r"\{(.*?)\}","{}",string)
    # print(spilt_string)
    return spilt_file_list,spilt_string


def merge(bare_string,reg):
    print(bare_string)
    print(reg)
    merged=str(bare_string).format(*reg)
    return reg


if __name__=="__main__":
    string=read_template("/home/ms/madlib-cli/assets/dark_and_stormy_night_template.txt")
    
    user_input=[]
    bare_string,word_list=parse_template(string)
    # print(word_list)
    # print(word_list)
    for word in bare_string:
        u_input=str(input(f"Give me a {word} >"))
        user_input.append(u_input)
    print(user_input)
    print(merge(string,user_input))
