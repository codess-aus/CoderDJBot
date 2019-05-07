from twython import Twython
import random
from messages import messages
from auth import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET
)

twitter = Twython(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET,
)

# message = random.choice(messages)
message = "Hello world - here's a pic!"
image = open('snicker2.png', 'rb')
response = twitter.upload_media(media=image)
media_id = [response['media_id']]
twitter.update_status(status=message, media_ids=media_id)
# twitter.update_status(status=message)
