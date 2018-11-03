import json
from watson_developer_cloud import ToneAnalyzerV3
import numpy as np
import pandas as pd
import seaborn as sns
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import matplotlib.pyplot as plt

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

def get_current_mood(text): #GET INFO
    return get_emotion(get_tones_and_scores(get_tone(text)))

def split_rows(response):
    for sentence in response['sentences_tone']:
        tones = sentence['tones']
        if tones:
            for tone in tones:
                yield {'sentence_id': sentence['sentence_id'],
                      'tone_id': tone['tone_id'],
                       'score': tone['score']}
        else:
            yield {'sentence_id': sentence['sentence_id'],
                      'tone_id': 'neutral',
                       'score': 1}

def response_to_df(response):
    return pd.DataFrame(split_rows(response))[['sentence_id', 'tone_id', 'score']]

def plot_distribution_of_scores(df):
    for tone in ('emotion', 'fear', 'joy', 'sadness', 'analytical', 'confident', 'tentative'):
        if tone in df['tone_id'].values:
            x = df['score'][df['tone_id'] == tone]
            data = [go.Histogram(x=x)]
            layout = go.Layout(
                title=tone,
                xaxis=dict(
                    title='Score'
                ),
                yaxis=dict(
                    title='Count'
                ),
                bargap=0.2,
                bargroupgap=0.1
            )
            fig = go.Figure(data=data, layout=layout)
            iplot(fig)
def plot_proportion_of_sentences_with_emotion(df):
    x=['joy', 'confident', 'analytical', 'neutral', 'tentative', 'sadness', 'anger']
    data = [go.Bar(
                x = x,
                y=(df.groupby('tone_id')['score'].count()/(df['sentence_id'].values[-1] + 1)).loc[x].fillna(0),
                marker=dict(
                    color=['#47EC6C', '#A7C696',
                   '#C6B26D', '#CEC8B2',
                   '#EEBA91', '#E8796B', '#F4493B'])
                )
            ]
    layout = go.Layout(
                title="Proportion of Sentences With Tone",
                xaxis=dict(
                    title='Tone'
                ),
                yaxis=dict(
                    title='Proportion'
                ),
                bargap=0.2,
                bargroupgap=0.1
            )
    fig = go.Figure(data=data, layout=layout)
    iplot(fig)

if __name__ == 'main':
