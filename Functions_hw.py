#Collections refactored
import random
import string


def generate_random_dict():
    """Generates a dictionary with random keys and random integer values."""
    num_keys = random.randint(1, 5)  # Random number of keys per dictionary (1 to 5 for simplicity)
    keys = random.sample(string.ascii_lowercase, num_keys)  # Random unique keys from a-z
    return {key: random.randint(0, 100) for key in keys}


def create_list_of_dicts():
    """Creates a list of dictionaries with random entries."""
    num_dicts = random.randint(2, 10)  # Random number of dictionaries between 2 and 10
    return [generate_random_dict() for _ in range(num_dicts)]


def combine_dicts(list_of_dicts):
    """Combines a list of dictionaries into one dictionary with unique keys."""
    common_dict = {}
    for idx, d in enumerate(list_of_dicts):
        for key, value in d.items():
            if key in common_dict and value > common_dict[key][0]:
                common_dict[key] = (value, idx + 1)
            elif key not in common_dict:
                common_dict[key] = (value, idx + 1)
    return common_dict


def format_final_dict(common_dict, list_of_dicts):
    """Formats the keys of the combined dictionary based on their origin."""
    return {f"{key}_{val[1]}" if list_of_dicts.count(key) > 1 else key: val[0] for key, val in common_dict.items()}


def main():
    list_of_dicts = create_list_of_dicts()
    common_dict = combine_dicts(list_of_dicts)
    final_dict = format_final_dict(common_dict, list_of_dicts)

    print("List of dictionaries:", list_of_dicts)
    print("Combined dictionary:", final_dict)


if __name__ == "__main__":
    main()

#string refactored

import re

def normalize_and_capitalize(text):
    """Normalize case and capitalize the first letter of each sentence."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    normalized_sentences = []
    for sentence in sentences:
        sentence = re.sub(r'[.!?]+\s*$', '', sentence.strip())  # Remove trailing punctuation
        words = sentence.split()
        words = [word.lower() for word in words]
        if words:
            words[0] = words[0].capitalize()
        normalized_sentence = ' '.join(words)
        normalized_sentences.append(normalized_sentence)
    return normalized_sentences

def create_sentence_from_last_words(sentences):
    """Create a sentence with the last word of each existing sentence and add it to the end."""
    last_words = [sentence.split()[-1] for sentence in sentences if sentence]
    return ' '.join(last_words)

def fix_mistakes(text):
    """Fix specific mistakes in the text, e.g., replacing 'iz' with 'is'."""
    return re.sub(r'\biz\b', 'is', text, flags=re.IGNORECASE)

def count_whitespace_characters(text):
    """Count the number of whitespace characters in the text."""
    return len(re.findall(r'\s', text))

def main():
    text = '''
        tHis iz your homeWork, copy these Text to variable.

        You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

        it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

        last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
    '''

    normalized_sentences = normalize_and_capitalize(text)
    new_sentence = create_sentence_from_last_words(normalized_sentences)
    normalized_sentences.append(new_sentence)
    normalized_text = '. '.join(normalized_sentences) + '.'
    corrected_text = fix_mistakes(normalized_text)
    whitespace_count = count_whitespace_characters(corrected_text)

    print("Corrected Text:\n", corrected_text)
    print("\nNumber of whitespace characters:", whitespace_count)

if __name__ == "__main__":
    main()