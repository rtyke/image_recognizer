# Start service
Clone the repo
```shell
git clone git@github.com:rtyke/image_recognizer.git
cd image_recognizer
```

```shell
docker-compose up --build -d
```

check it's working
```shell
curl -i --request GET --url http://127.0.0.1:5001
```

# Usage
send request to upload image to DB
```shell
curl -i --request POST \
  --url http://127.0.0.1:5001/image \
  --form "image=@/absolute/path/pic.jpg"
```

send request to check matches with face in DB
```shell
curl -i --request POST \
  --url http://127.0.0.1:5001/recognize \
  --form "image=@/absolute/path/pic.jpg"
```

Allowed images extensions are:
- jpg
- jpeg
- png

If you send request without picture or without faces you will get following responces correspondingly:
```json
{"exception": "No valid image in request"}
```

```json
{"exception": "No faces on a pic"}
```