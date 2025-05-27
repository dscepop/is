
def mod_pow(base, exp, mod):
    """Fast modular exponentiation: (base^exp) % mod"""
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result

def main():
    print("Diffie-Hellman Key Exchange")
    
    # Get public parameters
    p = int(input("Enter prime (p): "))
    g = int(input("Enter primitive root (g): "))
    
    # Get private keys
    a = int(input("Enter Alice's private key (a): "))
    b = int(input("Enter Bob's private key (b): "))
    
    # Calculate public keys
    A = mod_pow(g, a, p)
    B = mod_pow(g, b, p)
    print(f"\nPublic keys - Alice: {A}, Bob: {B}")
    
    # Calculate shared secret
    secret_a = mod_pow(B, a, p)
    secret_b = mod_pow(A, b, p)
    
    if secret_a == secret_b:
        print(f"Success! Shared secret: {secret_a}")
    else:
        print("Key exchange failed")

if __name__ == "__main__":
    main()


#output
Diffie-Hellman Key Exchange
Enter prime number (p): 13
Enter base number (g):5
Alice's secret number:6
Bob's secret number:15
