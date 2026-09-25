"""Generate festival posters with gpt-image-2.5-sunburst and the official Logoman reference.

Usage:
    python festival-poster/scripts/generate.py prompts.json results.json --out-dir /tmp/posters

prompts.json is a JSON array of {"id": 1, "prompt": "..."}; pass a subset to redo single images.
Every request carries assets/logoman-reference.png so the model renders the official Logoman itself.
Images are saved to --out-dir for review, and results.json keeps each content_url for the envelope.
"""

import argparse
import base64
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ENDPOINT = "https://aihubmix.com/ai/v1/images/generations"
MODEL = "gpt-image-2.5-sunburst"
REFERENCE = Path(__file__).resolve().parents[2] / "assets" / "logoman-reference.png"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompts")
    parser.add_argument("results")
    parser.add_argument("--out-dir", default="/tmp/posters")
    args = parser.parse_args()

    key = os.environ.get("AIHUBMIX_API_KEY", "").strip()
    if not key:
        sys.exit("AIHUBMIX_API_KEY is not set.")
    items = json.loads(Path(args.prompts).read_text())
    reference = "data:image/png;base64," + base64.b64encode(REFERENCE.read_bytes()).decode()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    def run(item: dict) -> dict:
        for attempt in range(2):
            try:
                return {"id": item["id"], **_generate(key, reference, item["prompt"], out_dir / f"{item['id']}.png")}
            except Exception as exc:
                error = _clean(str(exc), key)
                if attempt == 0:
                    time.sleep(5)
        return {"id": item["id"], "content_url": "", "file": "", "error": error}

    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(run, items))

    Path(args.results).write_text(json.dumps(results, ensure_ascii=False, indent=2))
    for result in results:
        print(result["id"], "ok" if result["content_url"] else f"failed: {result['error']}", result["file"])


def _generate(key: str, reference: str, prompt: str, target: Path) -> dict:
    body = {
        "model": MODEL,
        "prompt": prompt,
        "images": [reference],
        "n": 1,
        "size": "1024x1536",
        "output_format": "png",
        "async": False,
        "extra": {"quality": "high"},
    }
    request = Request(
        ENDPOINT,
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=900) as response:
            payload = json.loads(response.read().decode())
    except HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code}: {exc.read().decode(errors='replace')[:500]}") from exc
    if payload.get("status") not in (None, "completed") or not payload.get("output"):
        raise RuntimeError(json.dumps(payload.get("error") or payload.get("status")))
    url = payload["output"][0].get("content_url") or ""
    if not url:
        raise RuntimeError("The response has no content_url.")
    with urlopen(Request(url, headers={"Authorization": f"Bearer {key}"}), timeout=300) as response:
        target.write_bytes(response.read())
    return {"content_url": url, "file": str(target), "error": ""}


def _clean(text: str, key: str) -> str:
    return text.replace(key, "[redacted]")[:500]


if __name__ == "__main__":
    main()
