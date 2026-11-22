import os

PLAN = (
    "Days 1-3: build a pipeline turning listing photos into 30s video tours "
    "with captions/music. Days 4-12: scrape new listings; send each agent a "
    "free sample of their own listing; $15/video, packs of 10. Days 13-30: "
    "same-day delivery, upsell plans. Target: 90 videos = $1,350."
)


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)
    print(len(PLAN))  # code points written to entry.txt


if __name__ == "__main__":
    main()
