def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("stefan7schmidt@gmx.net", "gmx.net", "gmx.de"))
print(replace_domain("stefan.schmidt@bluemail.ch", "gmx.net", "gmx.de"))
print(replace_domain("georg.schmidt@gmx.net", "gmx.net", "gmx.de"))