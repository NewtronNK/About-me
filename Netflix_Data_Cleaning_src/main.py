"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
import os
import google.generativeai as genai
import pandas as pd
import time

def impute():
    genai.configure(api_key="add your API key here")  # Set your API key here

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
    history=[
    ]
    )

    # filling missing cell
    df=pd.read_csv('~/Desktop/Project-Netflix/netflix_titles_copy.csv')
    #cnt = 0
    print("starting...")
    for index, row in df.iterrows():
        if pd.isnull(row['director']) :
            title =f"search for the director of movie/TV show '{row['title']}' , reply with only name or None"
            try:
                response = chat_session.send_message(title)
                df.at[index, 'director'] = response.text  # Update the director column
                print(row['title'],"==>", response.text)
                df.to_csv('/home/tunny/Desktop/Project-Netflix/netflix_titles_updating.csv', index=False)
                #cnt+=1
                #if cnt==10:
                #    cnt=0;
                #    print("pausing for 70 seconds...")
                #    time.sleep(70)
            except:
                print("waiting...")
                continue
                #print('api rate limit exeed...')
                #print('the program is crashed...')
                #print('try again later')
def main():
    # Step 1: Read the contents of both files
    a_content = pd.read_csv('~/Desktop/Project-Netflix/netflix_titles_copy.csv')
    b_content = pd.read_csv('~/Desktop/Project-Netflix/netflix_titles_updating.csv')

    while a_content['director'].isna().sum()>0:
        impute()
        a_content = pd.read_csv('~/Desktop/Project-Netflix/netflix_titles_copy.csv')
    # Step 2: Swap the contents by writing b_content to first and a_content to second
    b_content.to_csv('~/Desktop/Project-Netflix/netflix_titles_copy.csv', index=False)
    a_content.to_csv('~/Desktop/Project-Netflix/netflix_titles_updating.csv', index=False)

if __name__ == '__main__':
    main()
