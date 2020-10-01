# ***Understanding Machine vs Human Generated Text in News***
## Black Lives Matter (US Category) `CSE 472 - Group 3`
By: John Oper & Joshua Dipert

---

## **This report is best viewed in a Jupyter Notebook**
# If you cannot open the Jupyter notebook on your own machine, you can do one of the following:
1. Open the Google Collabe File, found [here](https://colab.research.google.com/drive/1873Id-1eBi6OdKusK-hvEmOtdofG7G4v?usp=sharing)
2. Open the .pdf file (Not as nice looking but it has all of the data)

---

## **The zip file consists of the following**
`More on each of these can be found in the Jupyter Notebook`
#### ***Initial Data Sets***
* Name: `BLM_CNN_articles.csv`
* Description: This data set is the result of all articles whos headlines contained "blm" or "black lives matter"
* Usage: Allowed for the GPT-2 model to generate text based on these values
* Contents:
  * `Index` the array value that the data was stored in
  * `Article_Urls` the url for each article
  * `Headlines` the headline of each article
  * `Article_Text` the text of each article

---
* Name: `BLM_CNN_GPT2_Training_V1.txt`
* Description: This text file consits of all the articles whos healines did NOT contain "blm" or "black lives matter"
* Usage: Trained the GPT-2 model
* Contents:
  * 700+ articles text with a new line between each article 

#### ***Model***
* Name: `checkpoint -> run1` (folder)
* Description: The model generated from the text input
* Usage: Generated text based on the headlines
---
* Name: `samples -> run1` (folder)
* Description: Sample outputs for every 100 steps while training

#### ***Final Outputs***
* Name: `BLM_CNN_GPT2_Output_articles.csv`
* Description: This data set is the result of `BLM_CNN_articles.csv` combined with the associated GPT-2 generated text and the number of tokens used for the generated text
* Usage: Observe and compare results
* Contents:
  * `Index` the array value that the data was stored in
  * `Article_Urls` the url for each article
  * `Headlines` the headline of each article
  * `Article_Text` the text of each article
  * `Generated_Text` the text generated from the GPT-2 trained model
  * `Generated_Text_Length` the number of tokens used to generate the GPT-2 text

---
* Name: `BLM_CNN_GPT2_ouputs.txt`
* Description: Text file with all the outputs of the GPT-2 generated text
* Usage: Observe the text by itself and search for any copied text (none found)
* Contents:
  * `index` the index that it is associated with in the `BLM_CNN_GPT2_Output_articles.csv` file
  * `Prefix Text` the headline of the article / prefix text of the generated text output
  * `GPT-2 Output` the generated text output associated with the text file
  
 #### ***Python***
 * Name: `Get_BLM_CNN_Articles.py`
 * Description: Gets the BLM articles from CNN and stores them in their associated dataset
 ---
 * Name: `BLM_CNN_GPT2_Training.py`
 * Description: Trains the model based on the data collected in the previous step
 ---
 * Name: `GPT2_BLM_Article_Outputs.py`
 * Description: Gets the model ouput based on the headline and stores the associated data

---

## ***Deliverables***
!pip install selenium
!pip install pandas
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!pip install -q git+https://github.com/huggingface/transformers.git
!pip uninstall tensorflow
!pip install tensorflow==1.13.2
!pip install -q gpt-2-simple
 
