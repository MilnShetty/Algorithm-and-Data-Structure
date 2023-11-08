import heapq

class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(characters, frequencies):
    heap = []
    for char, freq in zip(characters, frequencies):
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(root, code, huffman_codes):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = code
    build_huffman_codes(root.left, code + "0", huffman_codes)
    build_huffman_codes(root.right, code + "1", huffman_codes)

def huffman_encoding(data):
    if not data:
        return None, None

    # Count character frequencies
    char_freq = {}
    for char in data:
        char_freq[char] = char_freq.get(char, 0) + 1

    characters, frequencies = zip(*char_freq.items())

    # Build Huffman tree
    root = build_huffman_tree(characters, frequencies)

    # Build Huffman codes
    huffman_codes = {}
    build_huffman_codes(root, "", huffman_codes)

    # Encode the data
    encoded_data = "".join(huffman_codes[char] for char in data)

    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data or root is None:
        return None

    decoded_data = []
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = root

    return "".join(decoded_data)

if __name__ == "__main__":
    # Example usage
    data = "this is an example for huffman encoding"
    
    encoded_data, tree = huffman_encoding(data)
    print(f"Encoded data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"Decoded data: {decoded_data}")
