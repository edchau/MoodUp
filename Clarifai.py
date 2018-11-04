from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


app = ClarifaiApp(api_key='bdd2a71595674c4f995647b96b7509b5')

# You can also create an environment variable called `CLARIFAI_API_KEY`
# and set its value to your API key.
# In this case, the construction of the object requires no `api_key` argument.

# response = model.predict([ClImage(url="https://static.boredpanda.com/blog/wp-content/uuuploads/cute-baby-animals/cute-baby-animals-2.jpg")])


def predict_image(url):
    model = app.public_models.general_model
    model.model_version = 'aa7f35c01e0642fda5cf400f543e7c40'
    response = model.predict([ClImage(url="https://static.boredpanda.com/blog/wp-content/uuuploads/cute-baby-animals/cute-baby-animals-2.jpg")])
    return response

def predict_video(url):
    model = app.models.get('general-v1.3')
    video = ClVideo(url='url')
    model.predict([video])
