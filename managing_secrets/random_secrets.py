import os,secrets,string
# Return a bytestring of size -> cryptographic use.
print(os.urandom(100))



secrets.token_bytes(16) #Return a random byte string containing nbytes
secrets.token_hex(16) #   Return a random text string, in hexadecimal
#Return a Base64 encoded random URL-safe text string
url = 'https://example.com/reset=' + secrets.token_urlsafe()

secrets.token_urlsafe(16)
# Generate a hard-to-guess temporary URL containing a security token suitable for password recovery applications:


# Generate an eight-character alphanumeric password
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))
print(password)

# Generate a ten-character alphanumeric password with at least one lowercase character, at least one uppercase character, and at least three digits:
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break
# Generate an XKCD-style passphrase:
import secrets
# On standard Linux systems, use a convenient dictionary file.
# Other platforms may need to provide their own word-list.
with open('/usr/share/dict/words') as f:
    words = [word.strip() for word in f]
    password = ' '.join(secrets.choice(words) for i in range(4))

