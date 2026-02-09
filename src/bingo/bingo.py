from docxtpl import DocxTemplate
from uuid import uuid4
from docx import Document
from io import BytesIO
from os import remove

from __init__ import get_random_facts

pages = []

for i in range(1, 25):
    page = DocxTemplate("../../3x4.docx")
    # todo: ensure all facts are used at least once for the first 10 pages
    page.render(get_random_facts())
    buffer = BytesIO()
    page.save(buffer)
    buffer.seek(0)
    pages.append(buffer)

doc = Document(pages[0])
doc.add_page_break()
for index, page in enumerate(pages[1:]):
    sp = Document(page)
    if index < len(pages) - 1:
        sp.add_page_break()

    for element in sp.element.body:
        doc.element.body.append(element)

doc.save(f"../../out/{uuid4()}.docx")
