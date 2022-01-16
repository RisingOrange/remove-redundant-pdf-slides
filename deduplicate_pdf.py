import argparse

import fitz

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("--output_file", default="out.pdf")
args = parser.parse_args()

doc = fitz.open(args.input_file)

duplicates = []
prev_page = doc[0] if len(doc) else None  # dont throw exception if empty
for i, page in enumerate(list(doc)[1:], 1):
    text_dict = page.get_text("dict")
    if page.get_text("text") == prev_page.get_text("text"):
        duplicates.append(i - 1)
    prev_page = page

print(f'Removed {len(duplicates)} pages:\n {" ".join(map(str, duplicates))}')

doc.delete_pages(duplicates)
doc.save(args.output_file)
