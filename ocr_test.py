from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_textline_orientation=True,
    lang='en'
)
result = ocr.predict("datasets/sample2.png")

for res in result:
    print("\nDetected Text:")
    for text in res['rec_texts']:
        print(text)