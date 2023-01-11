import json
from base64 import b64decode
from pathlib import Path
import os


def convert():
    DATA_DIR = Path.cwd() / "responses"
    files = [d for d in os.listdir(DATA_DIR) if os.path.isfile(os.path.join(DATA_DIR, d))]

    try:

        for file in files:

            for file in files:
                JSON_FILE = DATA_DIR / f"{file}"

                IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem

                IMAGE_DIR.mkdir(parents=True, exist_ok=True)

                with open(JSON_FILE, mode="r", encoding="utf-8") as file:
                    response = json.load(file)

                for index, image_dict in enumerate(response["data"]):
                    image_data = b64decode(image_dict["b64_json"])
                    image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
                    with open(image_file, mode="wb") as png:
                        png.write(image_data)
        
    except json.decoder.JSONDecodeError:
        print("a file skiped")