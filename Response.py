import IBMWatson as ibmw

def responseType():
    return ibmw.response_to_df(ibmw.get_tone("I'm so happy! I'm not happy"))

x = responseType()
#Check if sadness
#Average
print(x.groupby('tone_id')['score'].count()/(x['sentence_id'].values[-1] + 1))
