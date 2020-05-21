
# ///- remove punctuation
#/normalize all words to lowercase
#/remove "stop words" -- words used so frequently they are ignored
# go through the file word by word and keep a count of how often each word is used ///#


#how to comment out using///
#using the class material alone, watching the videos, reading material provided, I cant complete or barely understand what to do here even though I understood the class


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', #I dont know what this means///
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
def to_lowercase(input):
    ...     return input.lower()


#///i dont understand what goes inside parenthesis, dont i have to define what the list is

    def remove_from_list("!@#$%^&*_+{}:"?><") 


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(  #i dont understand why this is here or what it is for#
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)


#I don't know how to use the terminal it never works for me