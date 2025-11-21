from pathlib import Path
import re

def process_file(file_path: Path):
    text = file_path.read_text(encoding="utf-8")

    fm_pattern = re.compile(r"^([+-]{3,})\n(.*?)\n\1", re.DOTALL | re.MULTILINE)
    match = fm_pattern.search(text)
    if not match:
        return

    marker, fm_content = match.groups()

    new_fm = re.sub(
        r"(publishDate = \s*\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\.\d{3}Z",
        r"\1Z",
        fm_content,
    )

    if new_fm != fm_content:
        new_text = text.replace(match.group(0), f"{marker}\n{new_fm}\n{marker}")
        file_path.write_text(new_text, encoding="utf-8")
        print(f"✔ Fixed {file_path}")

if __name__ == "__main__":
    docs_dir = Path("content/docs/")  # 你的网站内容目录
    for md_file in docs_dir.rglob("*.md"):
        process_file(md_file)
