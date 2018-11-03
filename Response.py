import IBMWatson as ibmw

def responseType():
    return ibmw.response_to_df(ibmw.get_tone("I'm so happy!"))

print(responseType())
#Check if sadness
df.groupby('tone_id')['score'].count()/(df['sentence_id'].values[-1] + 1)
