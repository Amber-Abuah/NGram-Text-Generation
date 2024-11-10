## Text Autocomplete Using N-Grams

A Streamlit app capable of auto-completing text from a given context. 
The app uses three N-grams: a Bigram, Trigram and Fourgram to generate further text from a context provided by the user.
The predicted following words are generated by Maximum Likelihood Estimator (MLE) models, trained on each N-gram.  

Below is an example of an autocomplete of the sentence _'I was in awe when I noticed'_ from each N-gram:

>**Bigram:** I was in awe when I noticed her friends in last...  
>**Trigram:** I was in awe when I noticed by the window. Emma then looked up; but as long as...   
>**Fourgram:** I was in awe when I noticed her father's house, he pleased them all.

![image](https://github.com/user-attachments/assets/4fa5bb63-25c4-48c2-8413-1190af00757b)
Training data: [Emma](https://www.gutenberg.org/ebooks/19839) and [Persuasion](https://www.gutenberg.org/ebooks/105) by Jane Austen from the [Gutenburg Corpus](https://www.gutenberg.org/).  
Libraries: `NLTK`, `Streamlit`.
