import os

TEXT = (
    "I told my dentist I floss religiously: I confess to not doing it, "
    "feel guilty, and promise to change every six months."
)


def write_entry(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"), TEXT)


if __name__ == "__main__":
    main()
