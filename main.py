import dns.resolver

# Read the wordlist file
with open("dns_wordlist.txt", "r") as archive:
    lines = archive.read().splitlines()

# Input domain from the user
domain = input("Type a domain: ")

for subdomain in lines:
    # Combine the subdomain and domain to create the full hostname
    request = f"{subdomain}.{domain}"
    
    # Make the subdomain request
    try:
        resultados = dns.resolver.resolve(request, "A")
        for resultado in resultados:
            print(f"{request} {resultado}")

    except:
        pass