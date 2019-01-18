import urllib

def read_file_text(file_path="G:\\Python27\\some_quotes.txt") :
    quotes = open(file_path)
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_be_checked) :
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_be_checked)
    output = connection.read()
    print(output)
    connection.close()

file_path="G:\\Python27\\some_quotes.txt"
read_file_text(file_path)    
