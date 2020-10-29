#!/usr/bin/python

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os


# get current working directory
cwd = os.getcwd()

def gen_wordcloud(df, col, word):

    """
    Generate a wordcloud for each job description.

    Input: Dataframe to reference from, column to iterate, word input from main.py
    Output: A wordcloud for each job description
    """
    
    # initialising index
    index = 0
   
    for i in range(len(df)):

        text = df[col][index]

        # create and generate a word cloud image
        wordcloud = WordCloud(max_font_size = 50, 
                              max_words = 50, 
                              background_color = 'white', 
                              stopwords = STOPWORDS).generate(text)

        plt.figure()
        plt.imshow(wordcloud, interpolation = 'bilinear')
        plt.axis('off')

        # save image
        plt.savefig(cwd + '/Images/' + str(word) + '_' + str(index) + '.png')
        plt.close()

        index += 1