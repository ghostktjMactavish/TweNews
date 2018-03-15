import Algorithmia

def sentiment(text):
    input = {
      "document": text
    }
    client = Algorithmia.client('simLxeLhdObYV+LWP0AMm2xEt7D1')
    algo = client.algo('nlp/SentimentAnalysis/1.0.4')
    return algo.pipe(input).result#returns list of dictionaries,"document","sentiment"
#of value string and decimel respectively
