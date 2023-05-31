import re
import random
import string

def Vigenere_cipher(message: str, key: str) -> str:
    """
    Apply the Vigenere cipher to a given message using a specific key.

    Parameters:
        message (str): The message to be ciphered.
        key (str): The key used in the Vigenere cipher.

    Returns:
        str: The ciphered message.
    """
    key_length = len(key)
    cipher = [chr((ord(message[i]) + ord(key[i % key_length])) % 256) for i in range(len(message))]
    return ''.join(cipher)


def generate_unique_key(swap_dict: dict) -> str:
    """
    Generate a random key which doesn't exist in the swap dictionary.

    Parameters:
        swap_dict (dict): The dictionary to be checked.

    Returns:
        str: A unique key.
    """
    while True:
        key = ''.join(random.choices(string.ascii_lowercase, k=random.randint(6, 10)))
        if key not in swap_dict:
            break
    return key


def calculate_indentation(line: str) -> str:
    """
    Calculate the indentation of a given line.

    Parameters:
        line (str): The line whose indentation is to be calculated.

    Returns:
        str: The indentation of the line.
    """
    return ''.join(ch for ch in line if ch == " ")


def cipher_dictionary_keys(dictionary: dict) -> tuple:
    """
    Cipher the keys of a given dictionary.

    Parameters:
        dictionary (dict): The dictionary whose keys are to be ciphered.

    Returns:
        tuple: A tuple containing the ciphered dictionary and the key to decipher.
    """
    key = "".join(random.choices(string.ascii_lowercase, k=16))
    return {k: Vigenere_cipher(v, key) for k, v in dictionary.items()}, key


def obfuscate_code(code: str) -> str:
    """
    Obfuscate a given code.

    Parameters:
        code (str): The code to be obfuscated.

    Returns:
        str: The obfuscated code.
    """
    swap_dict = {}
    obfuscated_code = []
    for line in code:
        obfuscated_line = []
        for word in line.split():
            if word not in swap_dict:
                swap_dict[word] = generate_unique_key(swap_dict)
            obfuscated_line.append(swap_dict[word])
        obfuscated_code.append(calculate_indentation(line) + ' '.join(obfuscated_line) + "\n")

    # Avoid duplicate keys.
    swap_key, code_key = generate_unique_key(swap_dict), generate_unique_key(swap_dict)
    while code_key == swap_key:
        code_key = generate_unique_key(swap_dict)

    # Reverse keys and values ​​in swap_dict + cipher the dictionary values
    swap_dict, dict_key = cipher_dictionary_keys({v: k for k, v in swap_dict.items()})

    return (
        f"import re\n"
        f"{swap_key} = (lambda cipher_dict, key: {{k: ''.join([chr((ord(v[i]) - ord(key[i % len(key)])) % 256) for i in range(len(v))]) for k, v in cipher_dict.items()}})({swap_dict}, '{dict_key}')\n"
        f"{code_key} =  '''{''.join(obfuscated_code)}'''\n"
        f"(lambda: exec(re.compile('|'.join(map(re.escape, {swap_key}.keys()))).sub(lambda match: {swap_key}[match.group(0)], {code_key})))()"
    )
