# Get user input
user_input = input("Enter the sentence or Paragraph:")

def count_words(text):
  """
  Counts the number of words in a given sentence or paragraph.

  Args:
      text: The text to count words from (string).

  Returns:
      The number of words in the text (integer).
  """

  # Split the text into words using whitespace as separators
  words = text.split()

  # Check for empty input (no words)
  if not words:
      return 0
  
  # Return the number of words (length of the list)
  return len(words)

# Count words
word_count = count_words(user_input)

# Display result
if word_count > 0:
    print("The sentence or paragraph contains", word_count, "words.")
    
else:
    print("You entered an empty string. There are no words to count.")

