from base64 import b64decode

def decode(file):
    data = open(file, "r").read()
    bytes = b64decode(data, validate=True)
    with open('file.pdf', 'wb') as file:
        file.write(bytes)

if __name__ == "__main__":
    decode("Encoded File.b64")