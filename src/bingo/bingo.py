from docxtpl import DocxTemplate
from uuid import uuid4

doc = DocxTemplate("../../9x9.docx")
context = { 'fact1' : "Arild er min morfar" }
doc.render(context)

doc.save(f"../../out/{uuid4()}.docx")