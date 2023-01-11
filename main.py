import os
import openai
import json
from pathlib import Path


def send(promt):
    try:
        PROMPT = str(promt)

        DATA_DIR = Path.cwd() / "responses"

        DATA_DIR.mkdir(exist_ok=True)

        openai.api_key = "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"

        response = openai.Image.create(
            prompt=PROMPT,
            n=1,
            size="256x256",
            response_format="b64_json",
        )

        file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"

        with open(file_name, mode="w", encoding="utf-8") as file:
            json.dump(response, file)
            from convert import convert
            convert()

        return "success"

    
    except openai.error.APIConnectionError:
        print("failed")

    except openai.error.InvalidRequestError:
        return "failed"