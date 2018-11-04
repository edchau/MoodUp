import IBMWatson as ibmw

def responseType(text):
    return ibmw.response_to_df(ibmw.get_tone(text))

x = responseType('I am sad')
#Check if sadness
#Average
print(x.groupby('tone_id')['score'].count()/(x['sentence_id'].values[-1] + 1))
