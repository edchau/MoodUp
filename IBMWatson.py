from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='X7XH0fw_2PNm--VtKGH2LVYWdiiqKvF9Rk54G2w-aohB',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

def get_tone(text):
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json'
    ).get_result()
    return tone_analysis

def get_tones_and_scores(response):
    d = dict(anger=0, fear=0, joy=0, sadness=0, analytical=0, confident=0, tentative=0)
    for sentence in response['sentences_tone']:
        tones = sentence['tones']
        for tone in tones:
            d[tone['tone_id']] += tone['score']
    return d

def get_emotion(dictionary):
    return max(dictionary.items(), key=lambda x: x[1])

def get_current_mood(text):
    return get_emotion(get_tones_and_scores(get_tone(text)))

if __name__ == 'main':
