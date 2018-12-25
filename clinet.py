import json
import requests
import cv2

addr = 'http://localhost:5000'
test_url = addr + '/api/predict'

# prepare headers for http request
content_type = 'image/jpg'
headers = {'content-type': content_type}

img = cv2.imread('./full_55.png')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(
    test_url, data=img_encoded.tostring(), headers=headers)
# decode response
print(json.loads(response.text))

# expected output: {u'message': u'image received. size=124x124'}
