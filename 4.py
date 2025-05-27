import hashlib

print("SHA-256 Message Digest Calculator")
message = input("Enter your message: ")

hash_object = hashlib.sha256(message.encode())

hex_digest = hash_object.hexdigest()

print("\nInput Message:", message)
print("SHA-256 Digest:", hex_digest)
print("Length:", len(hex_digest), "characters")


#output

SHA-256 Message Digest Calculator
Enter your message: hello

Input Message: hello
SHA-256 Digest: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
Length: 64 characters


