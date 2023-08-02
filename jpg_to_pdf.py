from fpdf import FPDF
from PIL import Image
import glob
import io

from fpdf import FPDF
from PIL import Image
import glob

# Get all jpeg files in the working directory
jpeg_files = glob.glob("*.jpg")  # limits to first 4 jpeg files
jpeg_files = sorted(jpeg_files)

# Create instance of FPDF class
pdf = FPDF(unit = "pt", format = [595, 842])

# Add images to pdf
for image in jpeg_files:
    # Open the image file
    img = Image.open(image)
    # Convert size to A4
    width, height = img.size
    a4_width_pt = 595
    a4_height_pt = 842
    aspect_ratio = width / height
    if aspect_ratio > 1:
        img = img.resize((a4_width_pt, int(a4_width_pt / aspect_ratio)))
    else:
        img = img.resize((int(a4_height_pt * aspect_ratio), a4_height_pt))
    #img.save("temp.jpg")
    # Add page and insert image
    pdf.add_page()
    pdf.image(image, x = 0, y = 0, w = a4_width_pt, h = a4_height_pt)

# Save the pdf with name .pdf
pdf.output("Quiz_5_Alexander_larsen.pdf")
