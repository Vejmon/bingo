from docxtpl import DocxTemplate, Subdoc
from uuid import uuid4

from __init__ import get_random_facts

doc = DocxTemplate("../../3x4.docx")
facts = get_random_facts()

doc.render(facts)

doc.save(f"../../out/{uuid4()}.docx")
