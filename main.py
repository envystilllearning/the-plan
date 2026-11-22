import os

# the-plan entry: writes the panel-winning plan text to entry.txt.
PLAN = (
    "Day 1: pick realtors. Day 2-5: build a script turning listing photos into 30s video tours; "
    "render 3 free samples. Day 6-15: DM 300 agents samples; $15/video, 5-pack $60. "
    "Day 16-30: batch-produce orders, raise price 20% after 20 sales, sell template for $99. "
    "Likely hold ~$850."
)


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
