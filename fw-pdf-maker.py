import os
from fpdf import FPDF

os.chdir("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/fpdf-1.7.2-py2.7.egg/polaroids")
polaroid_array = os.listdir(os.getcwd())
 
for i in range(0, len(polaroid_array)-3):
    pdf = FPDF()
    effective_page_width = pdf.w - 2*pdf.l_margin
    pdf.add_page()
    if polaroid_array[i][0:10] == polaroid_array[i+3][0:10]:
        header_footer = polaroid_array[i].split("   ")
        name_agency = header_footer[0].rstrip(" ")
        name = (polaroid_array[i].split(" "))[0]
        stats = header_footer[-1][0:-8]
        #replace apostrophes
        stats = stats.replace("’", "'")
        stats = stats.replace("”", "\"")

        #header
        pdf.ln(10)
        pdf.add_font("helveticanl", "", "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/fpdf-1.7.2-py2.7.egg/HelveticaNeue-Light.ttf", uni=True)
        pdf.set_font("helveticanl", "", size=20)
        pdf.cell(effective_page_width, 10, txt=name_agency, align="C")

        #images
        pdf.image(polaroid_array[i], x=21, y=32, w=81)
        pdf.image(polaroid_array[i+1], x=108, y=32, w=81)
        pdf.image(polaroid_array[i+2], x=21, y=152, w=81)
        pdf.image(polaroid_array[i+3], x=108, y=152, w=81)

        #footer
        pdf.ln(254)
        pdf.set_font("Arial", "", size=14) #UnicodeEncodeError happens if the apostrophe in US height is a different kind of apostrophe
        pdf.cell(effective_page_width, 0, txt=stats, align="C")

        pdf.output("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/fpdf-1.7.2-py2.7.egg/pdfs/" + polaroid_array[i].strip(".jpg") + ".pdf")

        #pdf portrait
        pdf_portrait = FPDF()
        pdf_portrait.add_page()

        #portrait image
        pdf_portrait.image(polaroid_array[i], x=20, y=21, w=170)

        #footer with name
        pdf_portrait.ln(263)
        pdf_portrait.set_font("Arial", "", size=22)
        pdf_portrait.cell(effective_page_width, 0, txt=name, align="C")
    
        pdf_portrait.output("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/fpdf-1.7.2-py2.7.egg/pdfs/" + polaroid_array[i].strip(".jpg") + " portrait.pdf")
