import pandas as pd
import gpt_2_simple as gpt2
import os
import requests

# 355M is the medium model and is the largest model that could be ran in google collab and our personal machines
model_name = "355M"
if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/355M/

# The file created from articles that did NOT contain "BLM" or "Black Lives Matter" in the headline
file_name = "BLM_CNN_GPT2_Training_V1.txt"

# Train the model from the text file in the previous step
sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              dataset=file_name,
              model_name="355M",
              steps=1000,
              restore_from='fresh',
              run_name='run1',
              print_every=1,
              sample_every=100,
              save_every=100
              )

# generate the model created
gpt2.generate(sess)
