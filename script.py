import hanja

# Test a basic hanja to hangul conversion
hanja_text = "大韓民國"
hangul_text = hanja.translate(hanja_text, "substitution")

print(f"Original hanja: {hanja_text}")
print(f"Converted to hangul: {hangul_text}")

# Print the hanja module to see its attributes and methods
print("\nHanja module contents:")
print(hanja)
