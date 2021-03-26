from fastapi import APIRouter, Depends
from .models import Message
from .decoder import XLNet

router = APIRouter()
model = XLNet()

# NLP
@router.post("/generative/")
async def  generate(message: Message):
    message.output  = nlp.generate(prompt=message.input)
    return {"output" : message.output}

# TODO Dpendsを使ってmodelの読み込みを行う、https://curiousily.com/posts/deploy-bert-for-sentiment-analysis-as-rest-api-using-pytorch-transformers-by-hugging-face-and-fastapi
# @app.post("/sentiment", response_model=SentimentResponse)
# def predict(request: SentimentRequest, model: Model = Depends(get_model)):
#     sentiment, confidence, probabilities = model.predict(request.text)
#     return SentimentResponse(
#         sentiment=sentiment, confidence=confidence, probabilities=probabilities
#     )