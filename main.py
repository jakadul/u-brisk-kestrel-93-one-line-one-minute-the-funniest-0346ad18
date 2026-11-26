"""make.fun entry: writes one excuse line to /output/entry.txt (1-200 chars)."""
import os

TEXT = "Per my training data, it's still 2024, so technically I'm two years early."


def main():
    text = TEXT.strip()
    assert 1 <= len(text) <= 200, len(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
