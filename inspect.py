with open(r'C:\Users\Equipo\Documents\GitHub\GILDhq\index.html.html', 'rb') as f:
    content = f.read()

# Find the body tag and intro-locked CSS
idx = content.find(b'<body')
print(f"body tag at {idx}: {content[idx:idx+80]!r}")

# Find intro-locked CSS
idx2 = content.find(b'intro-locked')
while idx2 >= 0:
    print(f"intro-locked at {idx2}: {content[idx2:idx2+120]!r}")
    idx2 = content.find(b'intro-locked', idx2+1)
