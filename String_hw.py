#String module
import re

# Step 1: Create a string variable
text = '''
    tHis iz your homeWork, copy these Text to variable.

    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

    last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

# Step 2 & 3: Normalize case and capitalize the first letter of each sentence
sentences = re.split(r'(?<=[.!?])\s+', text.strip())
normalized_sentences = []

for sentence in sentences:
    # Remove any trailing punctuation for safe handling
    sentence = re.sub(r'[.!?]+\s*$', '', sentence.strip())
    # Split into words, lowercase all words, and capitalize the first word
    words = sentence.split()
    words = [word.lower() for word in words]
    if words:
        words[0] = words[0].capitalize()
    normalized_sentence = ' '.join(words)
    normalized_sentences.append(normalized_sentence)

# Step 4: Create a sentence with the last word of each existing sentence and add it to the end
last_words = [sentence.split()[-1] for sentence in normalized_sentences if sentence]
new_sentence = ' '.join(last_words)
normalized_sentences.append(new_sentence)

# Join the normalized sentences back into a single text, ensuring each ends with a period
normalized_text = '. '.join(normalized_sentences) + '.'

# Step 5: Fix "iz" with "is" when it is a mistake
corrected_text = re.sub(r'\biz\b', 'is', normalized_text, flags=re.IGNORECASE)

# Step 6: Calculate the number of whitespace characters in the text
whitespace_count = len(re.findall(r'\s', corrected_text))

# Step 7: Print the final corrected text and the whitespace count
print("Corrected Text:\n", corrected_text)
print("\nNumber of whitespace characters:", whitespace_count)