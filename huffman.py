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
    test_text = "Anupama Abeyrathna"
    freq = count_frequencies(test_text)
    
    print("Character frequencies:")
    for char, count in freq.items():
        # Show space character as 'SPACE' for clarity
        display_char = 'SPACE' if char == ' ' else char
        print(f"'{display_char}': {count}")
    
    print(f"\nTotal characters: {len(test_text)}")
    print(f"Unique characters: {len(freq)}")
    #end