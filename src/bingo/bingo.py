from docxtpl import DocxTemplate
from uuid import uuid4
from docx import Document
from os import remove

from __init__ import get_random_facts

pages = []

for i in range(1, 20):
    page = DocxTemplate("../../3x4.docx")
    # todo: ensure all facts are used at least once for the first 10 pages
    page.render(get_random_facts())
    name = f"{uuid4()}.docx"
    page.save(f"../../tmp/{name}")
    pages.append(name)

doc = Document(f"../../tmp/{pages[0]}")
doc.add_page_break()
remove(f"../../tmp/{pages[0]}")
for index, page in enumerate(pages[1:]):
    sp = Document(f"../../tmp/{page}")
    if index < len(pages) - 1:
        sp.add_page_break()

    for element in sp.element.body:
        doc.element.body.append(element)
    remove(f"../../tmp/{page}")

doc.save(f"../../out/{uuid4()}.docx")
