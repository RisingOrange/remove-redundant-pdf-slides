# TU-remove-redundant-pdf-slides
Slides of courses often contain incremental pages where one slide is like the last slide with e.g. some text added. This script removes all such slides except for the last in a series of slides. (This is the slide which normally contains all of the information.) I found "deduplicated" pdfs to be useful during open-book exams.

The script will not work for all slides / courses but it seems to work for a lot of the slides used at the technical university in Vienna.

## Setup
pip install requirements.txt

## Usage
python ./pdf_deduplicator.py [--output_file=out.pdf] input_file 
