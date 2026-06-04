from paddleocr import PaddleOCR
import json

ocr = PaddleOCR(
    use_textline_orientation=True,
    lang='en'
)

result = ocr.predict("datasets/sample2.png")

texts = []

for res in result:
    for text in res['rec_texts']:
        texts.append(text)

with open("outputs/output.json", "w") as f:
    json.dump(texts, f, indent=4)

print("JSON file created successfully!")