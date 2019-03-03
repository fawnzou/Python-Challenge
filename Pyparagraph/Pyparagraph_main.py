def paragraph_analysis(filename):

    import os
    import re

    # Lists to store "Sentences", "Words" and "Letters" splitted from target txt file, respectively
    sentences = []
    words = []
   

    # Set path for the location of txt file
    txt_path = os.path.join("raw_data", filename)

    with open(txt_path, "r") as txtfile:
        content = txtfile.read()
        # The whitespace character after ".", "!", or "?" 
        # Make sure that a "." inside a float number will not be considered as period
        sentences = re.split("(?<=[.!?]) +", content) 
        # Words are those flanked by any non-alphanumeric character(s) in passages
        words = re.split("\W+", content)
        # Note that the above syntax might introduce at most two "" at both beginning and ending of passages,  and end with quotation marks
        # Use while statement to remove "" from "words" list
        while "" in words:
            words.remove("")

        # Note that the above syntax split apart contraction word, which is generally considered as intact
        # Use "contraction_count" to calculate the amounts of contraction word in the passage
        contraction_count = len(re.split("[A-z]+['][A-z]+", content)) - 1

        # Note that the above syntax split apart hyphen-connected word, which is generally considered as intact as well
        # Use "hyphen_count" to calculate the amounts of hyphen-connected word in the passage
        hyphen_count = len(re.split("[A-z]+[-][A-z]+", content)) - 1
    
        # Note that the above syntax also split apart large numbers with comma, which is generally considered as intact
        # Use "comma_in_number_count" to calculate the amounts of commas in large numbers in the passage
        comma_in_number_count = len(re.split("[0-9]+[,][0-9]+", content)) - 1

        # Calculate Word counts and store in variant "word_count"
        word_count = len(words) - contraction_count - hyphen_count - comma_in_number_count
        
        # Loop through "words" list
        letter_count=0
        for word in words:
            letter_count +=len(word)

    
    # Output print
    print("\nParagraph Analysis")
    print('-'*12)
    print(f"Approximate Word Count: {word_count}")
    print(f"Approximate Sentence Count: {len(sentences)}")
    print(f"Average Letter Count: {round(letter_count / word_count, 1)}")
    print(f"Average Sentence Count: {round(word_count / len(sentences), 1)}")    
    
# Perform passage analysis on paragraph_1.txt
paragraph_analysis("paragraph_1.txt")

# Perform passage analysis on paragraph_2.txt
paragraph_analysis("paragraph_2.txt") 
    
