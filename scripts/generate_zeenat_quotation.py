#!/usr/bin/env python3
"""Generate Codevelix final quotation for Zeenat Pret ERP project."""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

OUTPUT_PATH = "/workspace/documents/Codevelix_Final_Quotation_Zeenat_Pret.docx"


def set_cell_shading(cell, color_hex):
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), color_hex)
    shading.set(qn("w:val"), "clear")
    cell._tc.get_or_add_tcPr().append(shading)


def add_heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
    return h


def add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style="List Bullet")
    if bold_prefix:
        run_b = p.add_run(bold_prefix)
        run_b.bold = True
        p.add_run(text)
    else:
        p.add_run(text)
    return p


def add_table_row(table, cells, header=False, shade=False):
    row = table.add_row()
    for i, text in enumerate(cells):
        cell = row.cells[i]
        cell.text = text
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(10)
                if header:
                    run.bold = True
                    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        if shade and header:
            set_cell_shading(cell, "1A365D")
    return row


def build_document():
    doc = Document()

    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)

    # Cover / Header
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("CODEVELIX")
    run.bold = True
    run.font.size = Pt(28)
    run.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Integrated ERP & Manufacturing Management System")
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0x4A, 0x55, 0x68)

    doc.add_paragraph()
    cover_title = doc.add_paragraph()
    cover_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = cover_title.add_run("FINAL IMPLEMENTATION QUOTATION")
    run.bold = True
    run.font.size = Pt(18)
    run.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    doc.add_paragraph()
    meta = doc.add_paragraph()
    meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    meta.add_run("Prepared for: Zeenat Pret\n").bold = True
    meta.add_run("Prepared by: Codevelix\n")
    meta.add_run("Website: https://codevelix.com/\n")
    meta.add_run("Email: info@codevelix.com | Phone: +92 306 4228502\n")
    meta.add_run("Location: Lahore, Pakistan\n")
    meta.add_run("Document Date: 22 August 2026 | Revision: 1.0\n")
    meta.add_run("Validity: 30 days from date of issue")

    doc.add_page_break()

    # 1. Executive Summary
    add_heading(doc, "1. Executive Summary", 1)
    doc.add_paragraph(
        "Codevelix is pleased to submit this final quotation for the design, development, "
        "and implementation of a fully integrated ERP and Manufacturing Management System "
        "for Zeenat Pret. This proposal is prepared against your business requirements "
        "document and covers production, inventory, multi-branch retail, accounts, HR, "
        "purchase, packing, dispatch, gatepass, and management reporting in one connected platform."
    )
    doc.add_paragraph(
        "The solution is purpose-built for apparel manufacturing and retail operations. "
        "It connects the complete workflow from employee attendance and purchasing through "
        "production job cards, finished goods, outlet sales, online orders, dispatch, and "
        "financial reconciliation — without duplicate data entry across departments."
    )
    doc.add_paragraph(
        "Total one-time implementation investment: Rs. 800,000 (Pakistani Rupees). "
        "Data migration, user training, go-live support, and a post-launch stabilization "
        "period are included within this amount."
    )

    # 2. Comparison Summary
    add_heading(doc, "2. Requirement Coverage Summary", 1)
    doc.add_paragraph(
        "The following table maps your stated requirements to the modules included in this quotation."
    )

    table = doc.add_table(rows=1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    hdr[0].text = "Requirement Area"
    hdr[1].text = "Scope in This Quotation"
    hdr[2].text = "Delivery"
    for cell in hdr:
        set_cell_shading(cell, "1A365D")
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)

    coverage = [
        ("HR & Payroll", "Employee records, attendance, shifts, leave, advances, PF, payroll, increments, performance history", "Phase 2"),
        ("Purchase & Procurement", "Requisitions, PO, receiving, rejection, returns, exchange, supplier ledger, low-stock alerts", "Phase 3"),
        ("Inventory & Stock", "Item master, stock ledger, transfers, issuance, barcode, valuation, multi-warehouse control", "Phase 3"),
        ("Production Management", "Style/Job Card, operations workflow, worker assignment, daily production, piece-rate wages, costing", "Phase 4"),
        ("Accounts & Finance", "Chart of accounts, vouchers, ledgers, expenses, petty cash, bank/cash, P&L, balance sheet, reconciliation", "Phase 5"),
        ("Packing, Dispatch & Gatepass", "Finished goods receiving, packing, dispatch, vehicle/driver gatepass, delivery tracking", "Phase 6"),
        ("Outlet POS (3 Branches)", "Barcode billing, hold/resume, exchange, branch stock, transfers, daily closing, party ledgers", "Phase 3–4"),
        ("Integrations", "E-commerce order sync, courier booking/tracking/COD, FBR digital invoicing readiness", "Phase 4–5"),
        ("Reports & Dashboards", "Management and department dashboards, PDF/Excel export, audit trail, role-based access", "All Phases"),
    ]
    for req, scope, phase in coverage:
        row = table.add_row()
        row.cells[0].text = req
        row.cells[1].text = scope
        row.cells[2].text = phase
        for cell in row.cells:
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(9)

    doc.add_paragraph()

    # 3. Scope of Work
    add_heading(doc, "3. Detailed Scope of Work", 1)

    add_heading(doc, "3.1 Core Platform & Security", 2)
    for item in [
        "User management with role-based access control (Admin, Management, HR, Purchase, Store, Production, Accounts, Outlet, Security)",
        "Company and brand configuration with department-wise data visibility",
        "Configurable approval workflows for purchase, leave, advances, production, and accounts",
        "Complete audit trail — created by, updated by, approved by, with timestamp and change history",
        "Daily automated backups, secure cloud hosting, and HTTPS access",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "3.2 HR & Payroll Management", 2)
    for item in [
        "Employee registration with CNIC, documents, bank details, department, designation, and employment history",
        "Shift management with grace period, overtime rules, and shift allocation",
        "Daily attendance — present, absent, leave, half-day, late arrival, early departure, manual correction with approval",
        "Leave management — annual, casual, sick, emergency, unpaid; request, approval, balance, and history",
        "Salary advances with approval, recovery schedule, and remaining balance tracking",
        "Provident Fund (PF) — employee and company contribution, monthly calculation, ledger, and reports",
        "Payroll processing — monthly salary, daily wages, production-based wages, allowances, deductions, bonuses",
        "Salary increments, allowances, and complete employee history",
        "HR reports — attendance register, leave analysis, payroll register, salary slips, PF summary",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "3.3 Purchase & Procurement", 2)
    for item in [
        "Purchase requisition with department request, priority, and approval workflow",
        "Configurable item categories — fabric, accessories, maintenance, office/general stock",
        "Supplier master with tax, payment terms, bank details, and transaction history",
        "Purchase order creation with multi-level approval, tax, discount, and delivery schedule",
        "Goods receiving against PO with ordered vs received vs rejected quantity",
        "Rejection management with reason, return status, and replacement tracking",
        "Purchase returns and supplier exchange with stock and ledger adjustment",
        "Purchase reports — daily/monthly/supplier-wise/item-wise, pending POs, outstanding quantities",
        "Automatic low-stock alerts when items fall below minimum level",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "3.4 Inventory & Warehouse Management", 2)
    for item in [
        "Product/item master — code, name, category, colour, size, fabric type, barcode, SKU, min/max stock",
        "Stock ledger — opening, purchase, production, transfer, issue, return, adjustment, damaged, closing",
        "Stock issuance to production, departments, and approved users with full traceability",
        "Inter-warehouse and inter-location stock transfers with in-transit control",
        "Scan-based controls — wrong scan blocked, duplicate scan blocked, negative stock blocked",
        "Stock valuation reports — item-wise, category-wise, warehouse-wise, movement history",
        "Finished goods variant control by Article + Colour + Size + SKU",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "3.5 Production & Manufacturing", 2)
    for item in [
        "Job Card / Style management — article code, tech pack, BOM version, colour-wise tracking, planned quantity",
        "Version-controlled Tech Pack and BOM with approval workflow; no hard delete after approval",
        "Embroidery planning — repeat-wise issue based on configurable machine-head standards",
        "Backup store — reserve non-embroidered components against Job Card until embroidery reconciles",
        "Stage-wise production workflow: PO → QC → Warehouse → Sampling → Job Card → Dyeing → Embroidery → Cutting → Stitching → Press → Packing → Finished Goods",
        "Stage issue/receive with automatic short/excess calculation, allowed loss, debit notes, and vendor/worker rates",
        "Worker assignment and daily production recording — completed qty, accepted/rejected qty, piece-rate wages",
        "Weekly worker settlement — stitch, press, pack — with payable ledger and duplicate-payment prevention",
        "Pre-cost vs post-cost per good suit with variance reporting by article and collection",
        "Production dashboard — active job cards, stage ageing, embroidery pending, backup reserved, cost variance",
        "Size-wise control (XS to XL): planned, cut, stitched, packed, short quantities",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "3.6 Accounts & Finance", 2)
    for item in [
        "Chart of accounts, journals, vouchers, and period locking",
        "Supplier payable, customer receivable, worker payable, and courier receivable ledgers",
        "Automatic day book from production, store, outlet, purchase, and payroll transactions",
        "Expense management by category with attachments and approval",
        "Petty cash — opening, received, expense, transfer, closing, reconciliation",
        "Bank and cash accounts — deposits, withdrawals, transfers, bank reconciliation",
        "Department-wise reconciliation — production vs payable, FG vs store, outlet vs cash, COD vs courier",
        "Financial reports — trial balance, P&L, balance sheet, cash flow, aged receivable/payable",
        "FBR digital invoicing support for tax-compliant sales invoices where required",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "3.7 Outlet POS — 3 Branches", 2)
    for item in [
        "Barcode/SKU billing with article, colour, size, quantity selection",
        "Hold and resume bill, return and exchange against original invoice",
        "Multi-payment — cash, card, bank, online, cheque, split payment",
        "Branch-wise live stock, warehouse-to-outlet transfer with 4-step in-transit control",
        "Branch purchase, expense, cash/bank accounts, customer and supplier ledgers",
        "Daily outlet closing — opening + received − paid = expected cash reconciliation",
        "Role control — Cashier, Outlet Manager, Accounts, Owner with configurable permissions",
        "Invoice print, WhatsApp delivery, and reprint capability",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "3.8 Packing, Dispatch & Gatepass", 2)
    for item in [
        "Scan-based receiving of packed suits from production into finished goods store",
        "Packing management — order, style, packed qty, carton/box number, packing employee",
        "Dispatch to outlet, customer, or online order with pick list and courier details",
        "Gatepass creation — vehicle, driver, material, quantity, destination, authorized person, security verification",
        "Workflow: Order → Production → Quality → Finishing → Packing → Dispatch → Gatepass → Delivery",
        "Dispatch reports — daily/weekly/monthly, customer-wise, order-wise, pending vs completed",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "3.9 Integrations", 2)
    for item in [
        "E-commerce integration — order import, SKU mapping, stock reservation, fulfilment write-back, inventory sync",
        "Courier integration — consignment booking from dispatch screen, CN/tracking storage, delivery status, COD reconciliation",
        "Returned/RTO stock released only after physical scan verification",
        "Email integration for system-generated documents and notifications",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "3.10 Reports & Management Dashboard", 2)
    for item in [
        "Management dashboard — employees, attendance, payroll, purchases, inventory, production, dispatch, accounts",
        "Department dashboards for HR, Purchase, Inventory, Production, Accounts, and Dispatch/Security",
        "Configurable alerts — low stock, pending approvals, production delays, pending dispatch, outstanding balances",
        "PDF and Excel export on all major reports",
        "Advanced search and filter by date, department, employee, supplier, item, style, order, status",
    ]:
        add_bullet(doc, item)

    doc.add_page_break()

    # 4. Implementation Approach
    add_heading(doc, "4. Implementation Approach", 1)
    doc.add_paragraph(
        "Codevelix follows a phased delivery model to reduce business disruption and ensure "
        "each department is trained before the next module goes live."
    )

    impl_table = doc.add_table(rows=1, cols=4)
    impl_table.style = "Table Grid"
    impl_hdr = impl_table.rows[0].cells
    for i, text in enumerate(["Phase", "Duration", "Activities", "Key Output"]):
        impl_hdr[i].text = text
        set_cell_shading(impl_hdr[i], "1A365D")
        for p in impl_hdr[i].paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)

    phases = [
        ("Phase 1\nFoundation", "Week 1–2", "Discovery, blueprint, master data structure, users, roles, departments, chart of accounts", "Signed blueprint & configured base system"),
        ("Phase 2\nHR & Payroll", "Week 3–4", "Employee enrollment, attendance, shifts, leave, advances, PF, payroll setup", "Live HR & payroll module"),
        ("Phase 3\nPurchase & Inventory", "Week 5–6", "Requisitions, PO, receiving, stock, transfers, low-stock alerts", "Live purchase & inventory"),
        ("Phase 4\nProduction & POS", "Week 7–9", "Job Card, workflow, worker wages, costing, outlet POS (3 branches), integrations", "Live production, outlets & integrations"),
        ("Phase 5\nAccounts", "Week 10", "Vouchers, ledgers, reconciliation, financial reports, FBR invoicing", "Live accounts module"),
        ("Phase 6\nDispatch & Go-Live", "Week 11–12", "Packing, dispatch, gatepass, data migration, UAT, training, go-live, stabilisation", "Production go-live & handover"),
    ]
    for phase, dur, act, output in phases:
        row = impl_table.add_row()
        row.cells[0].text = phase
        row.cells[1].text = dur
        row.cells[2].text = act
        row.cells[3].text = output
        for cell in row.cells:
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(9)

    doc.add_paragraph()
    doc.add_paragraph(
        "Total estimated delivery timeline: 12 weeks from contract sign-off and receipt of "
        "initial master data, subject to timely client approvals and staff availability for training."
    )

    # 5. Project Team
    add_heading(doc, "5. Dedicated Project Team", 1)
    team_table = doc.add_table(rows=1, cols=2)
    team_table.style = "Table Grid"
    team_hdr = team_table.rows[0].cells
    team_hdr[0].text = "Role"
    team_hdr[1].text = "Allocation"
    for cell in team_hdr:
        set_cell_shading(cell, "1A365D")
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    team = [
        ("Project Manager", "1 — single point of contact throughout engagement"),
        ("Business Analyst / Implementation Consultant", "2 — requirement mapping, configuration, UAT"),
        ("Production / Apparel Specialist", "1 — job card, embroidery, workflow, costing setup"),
        ("Integration Engineer", "1 — e-commerce, courier, and third-party API connections"),
        ("Data Migration Engineer", "1 — master data import and opening balance verification"),
        ("Support Engineer (Post Go-Live)", "1 — dedicated for stabilisation and after-sales support"),
    ]
    for role, alloc in team:
        row = team_table.add_row()
        row.cells[0].text = role
        row.cells[1].text = alloc

    doc.add_page_break()

    # 6. Commercial Proposal
    add_heading(doc, "6. Commercial Proposal", 1)

    add_heading(doc, "6.1 One-Time Implementation Investment", 2)
    doc.add_paragraph(
        "Codevelix offers a complete end-to-end implementation of the integrated ERP and "
        "Manufacturing Management System as defined in Section 3 of this quotation. The "
        "investment covers all modules, integrations, data migration, training, and go-live support."
    )

    summary_table = doc.add_table(rows=2, cols=2)
    summary_table.style = "Table Grid"
    hdr = summary_table.rows[0].cells
    hdr[0].text = "Description"
    hdr[1].text = "Amount (PKR)"
    for cell in hdr:
        set_cell_shading(cell, "1A365D")
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)

    total_cells = summary_table.rows[1].cells
    total_cells[0].text = (
        "Complete ERP Implementation — all modules, 3 outlet branches, integrations, "
        "data migration, training, UAT, and go-live support"
    )
    total_cells[1].text = "Rs. 800,000"
    for cell in total_cells:
        set_cell_shading(cell, "E2E8F0")
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.size = Pt(11)

    doc.add_paragraph()
    doc.add_paragraph("This investment includes:").runs[0].bold = True
    for item in [
        "Core platform with users, roles, security, and approval workflows",
        "HR, attendance, and payroll management",
        "Purchase, procurement, and supplier management",
        "Inventory, warehouse, and stock control",
        "Production and manufacturing (Job Card, embroidery, workflow, costing, dashboard)",
        "Accounts, finance, and department-wise reconciliation",
        "Outlet POS for 3 branches",
        "Packing store, dispatch, and gatepass management",
        "E-commerce and courier integration",
        "Reports, dashboards, and management analytics",
        "Data migration, opening balances, on-site training, UAT, and go-live support",
    ]:
        add_bullet(doc, item)

    doc.add_paragraph()
    doc.add_paragraph(
        "Payment terms: 50% (Rs. 400,000) upon contract sign-off | 50% (Rs. 400,000) upon go-live and final handover."
    ).runs[0].bold = True

    # 6.2 After-Sales Services
    add_heading(doc, "6.2 After-Sales Services & Annual Maintenance", 2)
    doc.add_paragraph(
        "Codevelix provides structured after-sales support so your operations continue smoothly "
        "after go-live. The following services are available as monthly or annual plans:"
    )

    support_table = doc.add_table(rows=1, cols=3)
    support_table.style = "Table Grid"
    sup_hdr = support_table.rows[0].cells
    for i, text in enumerate(["Service", "Standard Plan", "Premium Plan"]):
        sup_hdr[i].text = text
        set_cell_shading(sup_hdr[i], "1A365D")
        for p in sup_hdr[i].paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)

    support_items = [
        ("Cloud hosting, SSL, daily backups & system updates", "Included", "Included"),
        ("Software licence for all contracted modules", "Included", "Included"),
        ("WhatsApp, phone & email technical support", "Business hours", "24/7 priority"),
        ("Bug fixes & security patches", "Included", "Included"),
        ("Minor configuration changes", "Up to 4 hrs/month", "Up to 10 hrs/month"),
        ("New user training", "1 session/quarter", "Unlimited sessions"),
        ("Monthly system health check & performance report", "—", "Included"),
        ("Dedicated account manager", "—", "Included"),
        ("Emergency on-site visit (Lahore)", "—", "1 visit/quarter"),
        ("Monthly subscription (all users)", "Rs. 45,000/month", "Rs. 75,000/month"),
        ("Annual subscription (pay yearly — 2 months free)", "Rs. 450,000/year", "Rs. 750,000/year"),
    ]
    for item in support_items:
        row = support_table.add_row()
        for i, val in enumerate(item):
            row.cells[i].text = val
            for p in row.cells[i].paragraphs:
                for r in p.runs:
                    r.font.size = Pt(9)

    doc.add_paragraph()
    doc.add_paragraph(
        "Note: After-sales subscription begins from the go-live month. User counts and plan tier "
        "are confirmed at handover. First 60 days post go-live include complimentary Standard Plan "
        "support at no additional charge as part of the implementation package."
    )

    add_heading(doc, "6.3 What Is Included at No Extra Cost", 2)
    for item in [
        "Complete data migration — articles, components, colours, sizes, parties, workers, rates, opening stock and balances",
        "Role-based on-site training in Urdu or English for all departments",
        "User Acceptance Testing (UAT) support and issue resolution",
        "60-day post go-live stabilisation with dedicated support engineer",
        "Blueprint workshop within 5 working days of contract acceptance",
        "All reports, dashboards, PDF/Excel export, and audit trail features",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "6.4 Exclusions", 2)
    for item in [
        "Hardware — barcode scanners, label printers, POS terminals, biometric devices, and networking equipment",
        "Third-party subscription fees — e-commerce platform, courier account, SMS gateway, or payment gateway charges",
        "Government taxes (GST/SRB) applicable on services as per prevailing law",
        "Travel and accommodation for out-of-city visits beyond Lahore (if required)",
        "Additional custom features, new modules, or branches beyond three outlets — quoted separately as change requests",
        "Historical transaction data migration (opening balances and master data only are included)",
    ]:
        add_bullet(doc, item)

    doc.add_page_break()

    # 7. Terms & Conditions
    add_heading(doc, "7. Terms & Conditions", 1)
    terms = [
        ("Validity", "This quotation is valid for 30 days from the date of issue."),
        ("Payment", "50% advance upon contract sign-off; 50% upon successful go-live and final handover."),
        ("Taxes", "All prices are exclusive of applicable taxes unless stated otherwise."),
        ("Client Responsibilities", "Client will provide clean master data, approval matrices, rate cards, machine-head standards, and staff availability for training within agreed timelines."),
        ("Change Requests", "Any scope change beyond this document will be documented and quoted separately before work begins."),
        ("Timeline", "Delivery schedule depends on timely data provision, approvals, and sandbox/API access for integrations."),
        ("Intellectual Property", "Upon full payment, Zeenat Pret receives a perpetual licence to use the delivered system. Codevelix retains ownership of the underlying platform framework."),
        ("Confidentiality", "Both parties agree to keep commercial terms and business data confidential."),
        ("Warranty", "Codevelix warrants that delivered modules will perform as described in this document for 90 days post go-live, covered under the included support period."),
        ("Force Majeure", "Neither party shall be liable for delays caused by events beyond reasonable control."),
    ]
    for title, text in terms:
        p = doc.add_paragraph()
        run = p.add_run(f"{title}: ")
        run.bold = True
        p.add_run(text)

    # 8. Acceptance
    add_heading(doc, "8. Agreement & Acceptance", 1)
    doc.add_paragraph(
        "By signing below, both parties accept the scope, delivery approach, commercial terms, "
        "and after-sales services outlined in this quotation."
    )
    doc.add_paragraph()

    sign_table = doc.add_table(rows=4, cols=2)
    sign_table.style = "Table Grid"
    sign_table.rows[0].cells[0].text = "For Codevelix"
    sign_table.rows[0].cells[1].text = "For Zeenat Pret"
    for cell in sign_table.rows[0].cells:
        set_cell_shading(cell, "1A365D")
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    sign_table.rows[1].cells[0].text = "Name: ___________________________"
    sign_table.rows[1].cells[1].text = "Name: ___________________________"
    sign_table.rows[2].cells[0].text = "Designation: _____________________"
    sign_table.rows[2].cells[1].text = "Designation: _____________________"
    sign_table.rows[3].cells[0].text = "Signature & Date: ________________"
    sign_table.rows[3].cells[1].text = "Signature & Date: ________________"

    doc.add_paragraph()
    closing = doc.add_paragraph()
    closing.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = closing.add_run(
        "\nCodevelix — Develop a professional website and custom software for your company.\n"
        "https://codevelix.com/ | info@codevelix.com | +92 306 4228502 | Lahore, Pakistan"
    )
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x4A, 0x55, 0x68)
    run.italic = True

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    doc.save(OUTPUT_PATH)
    print(f"Document saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_document()
