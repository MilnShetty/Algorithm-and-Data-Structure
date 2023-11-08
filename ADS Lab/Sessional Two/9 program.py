def rabin_karp(text, pattern):
    def hash_string(s):
        # A simple hash function that returns the ASCII sum of characters
        return sum(ord(char) for char in s)

    def recompute_hash(old_hash, old_char, new_char, pattern_length):
        # Recompute the hash value of a new window of the same length
        return old_hash - ord(old_char) + ord(new_char)

    text_length = len(text)
    pattern_length = len(pattern)
    pattern_hash = hash_string(pattern)
    text_hash = hash_string(text[:pattern_length])

    matches = []

    for i in range(text_length - pattern_length + 1):
        if text_hash == pattern_hash and text[i:i+pattern_length] == pattern:
            matches.append(i)

        if i < text_length - pattern_length:
            text_hash = recompute_hash(text_hash, text[i], text[i + pattern_length], pattern_length)

    return matches

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABC"
matches = rabin_karp(text, pattern)

if matches:
    print(f"Pattern '{pattern}' found at positions: {matches}")
else:
    print(f"Pattern '{pattern}' not found in the text.")
