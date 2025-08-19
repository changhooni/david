## 반달곰 커피 홈페이지 (H2 헤더)

[반달곰 커피](https://반달곰 커피)

- 오디오 출력 소스코드

```
lang = request.args.get('lang', DEFAULT_LANG)\n
fp = BytesIO()\n
gTTS(text, "com", lang).write_to_fp(fp)\n
encoded_audio_data = base64.b64encode(fp.getvalue())\n
```

![david](https://github.com/changhooni/david/blob/main/templates/david.jpg)

