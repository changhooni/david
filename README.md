## 반달곰 커피 홈페이지 (H2 헤더)

[반달곰 커피](https://반달곰 커피)

- 오디오 출력 소스코드

```Python
lang = request.args.get('lang', DEFAULT_LANG)
fp = BytesIO()
gTTS(text, "com", lang).write_to_fp(fp)
encoded_audio_data = base64.b64encode(fp.getvalue())
```

![david](https://github.com/changhooni/david/blob/main/templates/david.jpg)

```python
def hello_world():
    # 파이썬 함수
    print("Hello, World!")
