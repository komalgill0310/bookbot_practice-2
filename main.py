import string

def file_path(): 
  return "books/frankenstein.txt"

def read_contents(path): 
  with open(path) as f: 
    file_contents = f.read()
    return file_contents
  
def count_words(text): 
  words = text.split()
  return len(words)

def count_characters(text): 
  lowercase_text = text.lower()
  alphabet_list = list(string.ascii_lowercase)
  ch_dict = {}
  for ch in lowercase_text: 
    if ch in alphabet_list:
      if ch in ch_dict: 
        ch_dict[ch] += 1
      else: 
        ch_dict[ch] = 1
  return ch_dict

def sort_dict(characters): 
  return dict(sorted(characters.items(), key=lambda ch: ch[1], reverse=True))

def get_report(sorted_dict,total_words): 
  print(f"--- Begin report of books/frankenstein.txt ---")
  print(f"{total_words} words found in the document")

  for key, value in sorted_dict.items(): 
    print(f"The '{key}' character was found {value} times")

  print(f"--- End report ---")

def main(): 
  path = file_path()
  contents = read_contents(path)
  total_words = count_words(contents)
  count_character = count_characters(contents)
  sort_characters = sort_dict(count_character)
  print_report = get_report(sort_characters, total_words)
  print(print_report)

main()