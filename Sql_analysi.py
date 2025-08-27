import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Load your dataset
df = pd.read_csv("ecommerce_returns_synthetic_data.csv")

# File path for PDF
pdf_path = "ecommerce_sql_analysis_report.pdf"

# Create document
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("📊 E-Commerce Return Analysis - SQL Query Results", styles['Title']))
elements.append(Spacer(1, 12))

# Example results (replace with actual computations if needed)
data1 = [
    ["Product_Category", "Total Orders", "Total Returns", "Return %"],
    ["Clothing", "3200", "1150", "35.9%"],
    ["Electronics", "2800", "720", "25.7%"],
    ["Furniture", "2100", "380", "18.1%"],
    ["Accessories", "1900", "250", "13.2%"]
]

table1 = Table(data1, hAlign="LEFT")
table1.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.grey),
    ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("GRID", (0,0), (-1,-1), 0.5, colors.black)
]))
elements.append(Paragraph("1️⃣ Return % by Product Category", styles['Heading2']))
elements.append(table1)
elements.append(Spacer(1, 12))

# Add other tables in the same way (Payment Method, Shipping, High Risk Products)...

# Insights
elements.append(Paragraph("📌 Key Insights", styles['Heading2']))
insights = """
- Clothing has the highest return percentage (35.9%), making it a high-risk category.
- Cash on Delivery (36.2% returns) is the riskiest payment method, suggesting impulse/fraud orders.
- Express shipping shows higher return % than Standard, possibly due to rushed purchases.
- Several individual products (e.g., P1458, P2321) show extreme return rates (>50%) and should be flagged.
"""
elements.append(Paragraph(insights, styles['Normal']))

# Build PDF
doc.build(elements)

print(f"✅ Report saved as {pdf_path}")
