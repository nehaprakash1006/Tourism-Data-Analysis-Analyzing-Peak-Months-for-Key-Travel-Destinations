import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load the data from the CSV file
data_file = "Tourist_Sites_Monthly_Data.csv"  # Change this to the path of your CSV file
df = pd.read_csv(data_file)

# Convert columns to numeric, coercing errors for non-numeric entries
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Identify the peak visitor count and the corresponding month
df['Peak_Visitor_Count'] = df.iloc[:, 1:].max(axis=1)  # Get the count of visitors for the peak month
df['Peak_Month'] = df.iloc[:, 1:].idxmax(axis=1)  # Get the name of the month for the peak visitor count

# Prepare the final DataFrame for output
results_df = df[['Site', 'Peak_Visitor_Count', 'Peak_Month']]

# Generate a PDF report
pdf_output_file = 'peak_visitors_report.pdf'  # Change this if you want a different output path

c = canvas.Canvas(pdf_output_file, pagesize=letter)
width, height = letter

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(30, height - 40, "Peak Visitors Analysis Report")

# Header
c.setFont("Helvetica-Bold", 12)
c.drawString(30, height - 70, "Site")
c.drawString(200, height - 70, "Peak Visitor Count")
c.drawString(400, height - 70, "Peak Month")

# Draw the data
c.setFont("Helvetica", 12)
y = height - 90
for index, row in results_df.iterrows():
    c.drawString(30, y, str(row['Site']))
    c.drawString(200, y, str(row['Peak_Visitor_Count']))
    c.drawString(400, y, str(row['Peak_Month']))
    y -= 20  # Move to the next line

# Finalize the PDF
c.save()
print(f"PDF report generated: {pdf_output_file}")
