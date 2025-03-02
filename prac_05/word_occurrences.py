"""
Word Occurrences
Estimate: 25 minutes
Actual:   29 minutes
"""

"""
function main()
    get text
    split text into words
    create empty dictionary word_count

    for each word in words
        if word is not in word_count
            add word to word_count with value 1
        else
            increment word_count[word] by 1

    sort word_count by word (keys)

    find max word length in sorted word_count for formatting

    for each word, count in sorted_word_count
        print word with max_word_length alignment, followed by count


"""

# Ask the user for input
text = input("Text: ")

# Split the text into words
words = text.split()

# Create a dictionary to store word counts
word_count = {}

# Count the occurrences of each word
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Sort the dictionary by word (keys)
sorted_word_count = sorted(word_count.items())

# Find the longest word length for formatting
max_word_length = max(len(word) for word, count in sorted_word_count)

# Print the word counts, aligned
for word, count in sorted_word_count:
    print(f"{word:{max_word_length}} : {count}")
