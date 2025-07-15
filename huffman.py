class Node:
    """
    A node in the Huffman tree.
    Can be either a leaf node (contains a character) or internal node (contains two children).
    """
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char        # The character (None for internal nodes)
        self.freq = freq        # Frequency of this character/subtree
        self.left = left        # Left child node
        self.right = right      # Right child node
    
    def is_leaf(self):
        """Check if this node is a leaf (has no children)"""
        return self.left is None and self.right is None
    
    def __str__(self):
        """String representation for debugging"""
        if self.is_leaf():
            display_char = 'SPACE' if self.char == ' ' else self.char
            return f"Leaf('{display_char}': {self.freq})"
        else:
            return f"Internal({self.freq})"
    
    def __lt__(self, other):
        """Less than comparison for priority queue (needed for heapq)"""
        return self.freq < other.freq


def count_frequencies(text):
    """
    Count the frequency of each character in the text.
    
    Args:
        text (str): The input text to analyze
        
    Returns:
        dict: A dictionary where keys are characters and values are their frequencies
    """
    frequency = {}
    
    # Go through each character in the text
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency


# Test the function
if __name__ == "__main__":
    # Test with a simple string
    test_text = "hello world"
    freq = count_frequencies(test_text)
    
    print("Character frequencies:")
    for char, count in freq.items():
        # Show space character as 'SPACE' for clarity
        display_char = 'SPACE' if char == ' ' else char
        print(f"'{display_char}': {count}")
    
    print(f"\nTotal characters: {len(test_text)}")
    print(f"Unique characters: {len(freq)}")
    
    # Test creating nodes
    print("\n--- Testing Node Creation ---")
    
    # Create leaf nodes for each character
    nodes = []
    for char, count in freq.items():
        node = Node(char, count)
        nodes.append(node)
        print(f"Created: {node}")
    
    # Create an internal node by combining two nodes
    if len(nodes) >= 2:
        # Combine first two nodes
        left_node = nodes[0]
        right_node = nodes[1]
        combined_freq = left_node.freq + right_node.freq
        internal_node = Node(freq=combined_freq, left=left_node, right=right_node)
        
        print(f"\nCombined nodes:")
        print(f"  Left: {left_node}")
        print(f"  Right: {right_node}")
        print(f"  Result: {internal_node}")
        print(f"  Is leaf? {internal_node.is_leaf()}")