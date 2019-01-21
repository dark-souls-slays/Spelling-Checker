<b>Claudia Espinoza<br>
National Dong Hwa Univerisity <br>
Machine Learning </b>


Create a spelling checker that outputs the words with 3 or less editing distance.

<b>Spelling Checker<br></b>
1. Use dictionary.txt to input the words into a list.
2. Get input from user and check if the word is in our dictionary list.
3. If the word is not found in the dictionary, call spelling_checker().
4. Spelling checker looks for words that are between l + 3 and l - 3 in size. That is no more than 3 insertions or deletions away from the mispelled_word.
5. If found, spelling_checker() calls edit_distance() to get the edit distance between the 2 words and saves the word and its respective edit_distance in a dictionary.
6. Lastly we arrange the dictionary by editing distance and output the results.
