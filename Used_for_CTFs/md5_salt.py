import string
import hashlib
import itertools

def md5_zero_gen(prefix_salt, chars):
    word_len = 1
    while True:
        for i in itertools.permutations(chars, word_len):
            word = "".join(i)
            text = prefix_salt + word
            hash = hashlib.md5(text.encode()).hexdigest()
            if hash[:2] == "0e" and hash[2:].isdecimal():
                return word
        word_len += 1

chars = string.ascii_lowercase + "0123456789"
hash = "0e902564435691274142490923013038"
salt = "f789bbc328a3d1a3"

print(f"Generating an MD5 with prefix salt '{salt}' that evaluates to '0' as a scientific notation...")
passwd = md5_zero_gen(salt, chars)
print(f"Valid password: {passwd}")