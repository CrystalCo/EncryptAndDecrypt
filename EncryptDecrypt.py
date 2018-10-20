import random, json 

def encrypt_file(filename):
    'Encrypts a txt file'

    file_in = open(filename, 'r', encoding='utf-8')
    file_content = file_in.read()
    file_in.close()

    # Creates a set of all the distinct characters in file_content
    char_set = set()
    for a_char in file_content:
        if a_char not in char_set:
            char_set.add(a_char)

    # Turns character set into 2 lists and randomizes the latter
    char_list = list(char_set)
    scramble_list = list(char_set)
    random.shuffle(scramble_list)

    # Creates an encryption dictionary
    encrypt_dict = dict()
    for a_char in char_list:
        value = scramble_list.pop(0)
        encrypt_dict[a_char] = value
    print('Encryption Dictionary: ' + str(encrypt_dict) + '     Encryption Dictionary Length: ' + str(len(encrypt_dict)))

    # Outputs 2 new files: One with the original file encrypted and one with the Encryption Dictionary
    output_file = open(('{}.enc'.format(filename)), 'w')
    for a in file_content:
        output_file.write('{}'.format(encrypt_dict.get(a)))
    output_file.close()

    other_file = open(('{}.dict'.format(filename)), 'w')
    other_file.write(json.dumps(encrypt_dict))
    other_file.close()


def decrypt_file(dict_filename, enc_filename):
    'Decrypts an encrypted file.'

    dict_in = open(dict_filename)
    orig_dict = json.load(dict_in)

    # Reverses the Encrypted Dictionary
    decrypt_dict = dict()
    for x in orig_dict:
        decrypt_dict[orig_dict.get(x)] = x
    print('Decryption Dictionary Length: {}.    Decryption Dictionary: {}'.format(str(len(decrypt_dict)), decrypt_dict))

    enc_in = open(enc_filename)
    file_content = enc_in.read()
    enc_in.close()

    # Outputs a decrypted file of the original encrypted file
    output_file = open(('{}.dec'.format(enc_filename[:-4])), 'w')
    for a in file_content:
        output_file.write('{}'.format(decrypt_dict.get(a)))
    output_file.close()


source_file = "MobyDick.txt" 

print("Encrypting input file: " + source_file)
encrypt_file(source_file)

print("-"*20)

print("Decrypting input file: " + source_file) 
decrypt_file(source_file + ".dict", source_file + ".enc")


def top_word(filename):
    'Returns the top word in file'

    # Constants
    special_char = [',', '$', '*', ';', '.', '&', '!', '(', '-', ')', '"', '?', '—'] # txt files have a different '—' symbol. Removing both.

    file_in = open(filename, 'r', encoding='utf-8')
    orig_file = file_in.read()  
    orig_file = orig_file.replace('\n', ' ')        # New lines were giving problems
    for i in range(len(special_char)):
        orig_file = orig_file.replace(special_char[i], '')
    word_list = orig_file.split(' ')
    file_in.close()
    
    # Word Counter
    inventory = dict()
    max_count = 0
    max_item = ''

    for x in word_list:
        if x not in inventory:
            inventory[x] = 1
        else:
            inventory[x] += 1
    
    for key in inventory:
        if inventory[key] > max_count:
            max_count = inventory[key]
            max_item = key

    d_word = 'Top Word: {} '.format((max_item, inventory[max_item]))
    # As a tuple # return((max_item, inventory[max_item]))
    print(inventory.keys())
    return d_word

print(top_word("MobyDick.txt"))
