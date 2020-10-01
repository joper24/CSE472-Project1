import pandas as pd
import gpt_2_simple as gpt2
import tensorflow as tf
import os
import requests

# Reads the .csv file created from searching for articles on CNN's website
df = pd.read_csv('BLM_CNN_articles.csv')

# Store the data extracted from the .csv file
article_urls = list(df['Article_Urls'])
headlines = list(df['Headlines'])
article_text = list(df['Article_Text'])

# Creates a new sesstion to run the model trained in the previous step
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, model_name='run1')

gpt2GeneratedText = []
gpt2_length = []
file = open("BLM_CNN_GPT2_ouputs.txt", "w") # Stores the output of each GPT2 generated article
for i in range(0, len(headlines), 1):
    print("----------- " + str(i) + " -----------" )
    headline_prefix = headlines[i]

    # Set the length of the generation to the max generation length if the article length is greater than the max
    articleLength = len(article_text[i].split())
    if articleLength > 1023:
        articleLength = 1023
    output = gpt2.generate(
                sess,
                prefix=headline_prefix,
                length=articleLength,
                temperature=0.7,
                top_p=0.9,
                return_as_list=True
        )
    print(output)
    gpt2GeneratedText.append(output[0])
    gpt2_length.append(articleLength)

    file.write("---------------------------- " + str(i) + " ----------------------------\n")
    file.write("Prefix Text (Headlines): " + headline_prefix + "\n")
    file.write("length: " + str(articleLength) + "\n")
    file.write("GPT2 Output:\n" + output[0] + "\n\n")

file.close()

# Dictionary to storte the collected data in a .csv file
retrievedData = {
    'Article_Urls': article_urls,
    'Headlines' : headlines,
    'Article_Text' : article_text,
    'Generated_Text': gpt2GeneratedText,
    'Generated_Text_length': gpt2_length
}

#Data frame to export the articles as a .csv
df = pd.DataFrame(retrievedData, columns=['Article_Urls','Headlines','Article_Text','Generated_Text','Generated_Text_length'])
df.index.name = 'Index'
df.to_csv(r'BLM_CNN_GPT2_Output_articles.csv', index = True, header = True)

print(df)
