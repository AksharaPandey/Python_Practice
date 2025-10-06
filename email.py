#Simple email slicer
email = input("Enter your email address: ").strip()
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]
print(f"Username: {username}")
print(f"Domain: {domain}")