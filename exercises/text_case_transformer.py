# Text Case Transformer

text = input("Enter some text: ")

# Uppercase
print("Uppercase:", text.upper())

# Lowercase
print("Lowercase:", text.lower())

# Alternatingcase
alt_text = "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text))
print("Alternating case:", alt_text)
