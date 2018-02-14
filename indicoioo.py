import indicoio
indicoio.config.api_key = '46591a9d64060e374f49e52ce68cf542'
import operator
# single example
indicoio.emotion("I did it. I got into Grad School. Not just any program, but a GREAT program. :-)")

# batch example

emotion=indicoio.emotion(
    "I did it. I got into Grad School. Not just any program, but a GREAT program. :-)",
)
print(emotion)
emotion_feel=max(emotion.items(), key=operator.itemgetter(1))[0]
print(emotion_feel)
