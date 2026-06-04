from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_textline_orientation=True,
    lang='en'
)
result = ocr.predict("outputs/enhanced_sample.jpg")

for res in result:
    print("\nDetected Text:")
    for text in res['rec_texts']:
        print(text)