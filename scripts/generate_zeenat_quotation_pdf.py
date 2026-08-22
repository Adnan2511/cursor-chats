#!/usr/bin/env python3
"""Generate Codevelix final quotation PDF for Zeenat Pret ERP project."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, ListFlowable, ListItem,
)
import os

OUTPUT_PATH = "/workspace/documents/Codevelix_Final_Quotation_Zeenat_Pret.pdf"
BRAND = colors.HexColor("#1A365D")
MUTED = colors.HexColor("#4A5568")
LIGHT = colors.HexColor("#E2E8F0")


def bullet(text):
    return ListItem(Paragraph(text, styles["BulletItem"]), leftIndent=12)


def make_table(data, col_widths=None, header=True):
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    if header:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), BRAND),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]
    t.setStyle(TableStyle(style))
    return t


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    global styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="CoverTitle", fontName="Helvetica-Bold", fontSize=26,
        textColor=BRAND, alignment=TA_CENTER, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="CoverSub", fontName="Helvetica", fontSize=13,
        textColor=MUTED, alignment=TA_CENTER, spaceAfter=12,
    ))
    styles.add(ParagraphStyle(
        name="CoverMain", fontName="Helvetica-Bold", fontSize=16,
        textColor=BRAND, alignment=TA_CENTER, spaceAfter=16,
    ))
    styles.add(ParagraphStyle(
        name="CoverMeta", fontName="Helvetica", fontSize=10,
        alignment=TA_CENTER, leading=14,
    ))
    styles.add(ParagraphStyle(
        name="H1", fontName="Helvetica-Bold", fontSize=14,
        textColor=BRAND, spaceBefore=14, spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="H2", fontName="Helvetica-Bold", fontSize=11,
        textColor=BRAND, spaceBefore=10, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="Body", fontName="Helvetica", fontSize=9.5,
        leading=13, alignment=TA_JUSTIFY, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="BulletItem", fontName="Helvetica", fontSize=9,
        leading=12, leftIndent=0, spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name="BoldBody", fontName="Helvetica-Bold", fontSize=9.5,
        leading=13, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="Footer", fontName="Helvetica-Oblique", fontSize=8,
        textColor=MUTED, alignment=TA_CENTER, spaceBefore=12,
    ))

    story = []

    # Cover
    story += [
        Spacer(1, 0.6 * inch),
        Paragraph("CODEVELIX", styles["CoverTitle"]),
        Paragraph("Integrated ERP &amp; Manufacturing Management System", styles["CoverSub"]),
        Spacer(1, 0.2 * inch),
        Paragraph("FINAL IMPLEMENTATION QUOTATION", styles["CoverMain"]),
        Spacer(1, 0.15 * inch),
        Paragraph(
            "<b>Prepared for:</b> Zeenat Pret<br/>"
            "<b>Prepared by:</b> Codevelix<br/>"
            "<b>Website:</b> https://codevelix.com/<br/>"
            "<b>Email:</b> info@codevelix.com | <b>Phone:</b> +92 306 4228502<br/>"
            "<b>Location:</b> Lahore, Pakistan<br/>"
            "<b>Document Date:</b> 22 August 2026 | <b>Revision:</b> 1.0<br/>"
            "<b>Validity:</b> 30 days from date of issue",
            styles["CoverMeta"],
        ),
        PageBreak(),
    ]

    # 1. Executive Summary
    story.append(Paragraph("1. Executive Summary", styles["H1"]))
    story.append(Paragraph(
        "Codevelix is pleased to submit this final quotation for the design, development, "
        "and implementation of a fully integrated ERP and Manufacturing Management System "
        "for Zeenat Pret. This proposal is prepared against your business requirements "
        "document and covers production, inventory, multi-branch retail, accounts, HR, "
        "purchase, packing, dispatch, gatepass, and management reporting in one connected platform.",
        styles["Body"],
    ))
    story.append(Paragraph(
        "The solution is purpose-built for apparel manufacturing and retail operations. "
        "It connects the complete workflow from employee attendance and purchasing through "
        "production job cards, finished goods, outlet sales, online orders, dispatch, and "
        "financial reconciliation — without duplicate data entry across departments.",
        styles["Body"],
    ))
    story.append(Paragraph(
        "<b>Total one-time implementation investment: Rs. 800,000 (Pakistani Rupees).</b> "
        "Data migration, user training, go-live support, and a post-launch stabilization "
        "period are included within this amount.",
        styles["Body"],
    ))

    # 2. Requirement Coverage
    story.append(Paragraph("2. Requirement Coverage Summary", styles["H1"]))
    story.append(Paragraph(
        "The following table maps your stated requirements to the modules included in this quotation.",
        styles["Body"],
    ))
    coverage = [
        ["Requirement Area", "Scope in This Quotation", "Delivery"],
        ["HR & Payroll", "Employee records, attendance, shifts, leave, advances, PF, payroll, increments, performance history", "Phase 2"],
        ["Purchase & Procurement", "Requisitions, PO, receiving, rejection, returns, exchange, supplier ledger, low-stock alerts", "Phase 3"],
        ["Inventory & Stock", "Item master, stock ledger, transfers, issuance, barcode, valuation, multi-warehouse control", "Phase 3"],
        ["Production Management", "Style/Job Card, operations workflow, worker assignment, daily production, piece-rate wages, costing", "Phase 4"],
        ["Accounts & Finance", "Chart of accounts, vouchers, ledgers, expenses, petty cash, bank/cash, P&L, balance sheet, reconciliation", "Phase 5"],
        ["Packing, Dispatch & Gatepass", "Finished goods receiving, packing, dispatch, vehicle/driver gatepass, delivery tracking", "Phase 6"],
        ["Outlet POS (3 Branches)", "Barcode billing, hold/resume, exchange, branch stock, transfers, daily closing, party ledgers", "Phase 3–4"],
        ["Integrations", "E-commerce order sync, courier booking/tracking/COD, FBR digital invoicing readiness", "Phase 4–5"],
        ["Reports & Dashboards", "Management and department dashboards, PDF/Excel export, audit trail, role-based access", "All Phases"],
    ]
    story.append(make_table(coverage, [1.3 * inch, 3.5 * inch, 0.9 * inch]))
    story.append(Spacer(1, 10))

    # 3. Detailed Scope
    story.append(Paragraph("3. Detailed Scope of Work", styles["H1"]))

    scope_sections = {
        "3.1 Core Platform & Security": [
            "User management with role-based access control (Admin, Management, HR, Purchase, Store, Production, Accounts, Outlet, Security)",
            "Company and brand configuration with department-wise data visibility",
            "Configurable approval workflows for purchase, leave, advances, production, and accounts",
            "Complete audit trail — created by, updated by, approved by, with timestamp and change history",
            "Daily automated backups, secure cloud hosting, and HTTPS access",
        ],
        "3.2 HR & Payroll Management": [
            "Employee registration with CNIC, documents, bank details, department, designation, and employment history",
            "Shift management with grace period, overtime rules, and shift allocation",
            "Daily attendance — present, absent, leave, half-day, late arrival, early departure, manual correction with approval",
            "Leave management — annual, casual, sick, emergency, unpaid; request, approval, balance, and history",
            "Salary advances with approval, recovery schedule, and remaining balance tracking",
            "Provident Fund (PF) — employee and company contribution, monthly calculation, ledger, and reports",
            "Payroll processing — monthly salary, daily wages, production-based wages, allowances, deductions, bonuses",
            "Salary increments, allowances, and complete employee history",
            "HR reports — attendance register, leave analysis, payroll register, salary slips, PF summary",
        ],
        "3.3 Purchase & Procurement": [
            "Purchase requisition with department request, priority, and approval workflow",
            "Configurable item categories — fabric, accessories, maintenance, office/general stock",
            "Supplier master with tax, payment terms, bank details, and transaction history",
            "Purchase order creation with multi-level approval, tax, discount, and delivery schedule",
            "Goods receiving against PO with ordered vs received vs rejected quantity",
            "Rejection management with reason, return status, and replacement tracking",
            "Purchase returns and supplier exchange with stock and ledger adjustment",
            "Purchase reports — daily/monthly/supplier-wise/item-wise, pending POs, outstanding quantities",
            "Automatic low-stock alerts when items fall below minimum level",
        ],
        "3.4 Inventory & Warehouse Management": [
            "Product/item master — code, name, category, colour, size, fabric type, barcode, SKU, min/max stock",
            "Stock ledger — opening, purchase, production, transfer, issue, return, adjustment, damaged, closing",
            "Stock issuance to production, departments, and approved users with full traceability",
            "Inter-warehouse and inter-location stock transfers with in-transit control",
            "Scan-based controls — wrong scan blocked, duplicate scan blocked, negative stock blocked",
            "Stock valuation reports — item-wise, category-wise, warehouse-wise, movement history",
            "Finished goods variant control by Article + Colour + Size + SKU",
        ],
        "3.5 Production & Manufacturing": [
            "Job Card / Style management — article code, tech pack, BOM version, colour-wise tracking, planned quantity",
            "Version-controlled Tech Pack and BOM with approval workflow; no hard delete after approval",
            "Embroidery planning — repeat-wise issue based on configurable machine-head standards",
            "Backup store — reserve non-embroidered components against Job Card until embroidery reconciles",
            "Stage-wise production workflow from PO through Finished Goods",
            "Stage issue/receive with automatic short/excess calculation, allowed loss, debit notes, and vendor/worker rates",
            "Worker assignment and daily production recording — completed qty, accepted/rejected qty, piece-rate wages",
            "Weekly worker settlement — stitch, press, pack — with payable ledger and duplicate-payment prevention",
            "Pre-cost vs post-cost per good suit with variance reporting by article and collection",
            "Production dashboard — active job cards, stage ageing, embroidery pending, backup reserved, cost variance",
            "Size-wise control (XS to XL): planned, cut, stitched, packed, short quantities",
        ],
        "3.6 Accounts & Finance": [
            "Chart of accounts, journals, vouchers, and period locking",
            "Supplier payable, customer receivable, worker payable, and courier receivable ledgers",
            "Automatic day book from production, store, outlet, purchase, and payroll transactions",
            "Expense management by category with attachments and approval",
            "Petty cash — opening, received, expense, transfer, closing, reconciliation",
            "Bank and cash accounts — deposits, withdrawals, transfers, bank reconciliation",
            "Department-wise reconciliation — production vs payable, FG vs store, outlet vs cash, COD vs courier",
            "Financial reports — trial balance, P&L, balance sheet, cash flow, aged receivable/payable",
            "FBR digital invoicing support for tax-compliant sales invoices where required",
        ],
        "3.7 Outlet POS — 3 Branches": [
            "Barcode/SKU billing with article, colour, size, quantity selection",
            "Hold and resume bill, return and exchange against original invoice",
            "Multi-payment — cash, card, bank, online, cheque, split payment",
            "Branch-wise live stock, warehouse-to-outlet transfer with 4-step in-transit control",
            "Branch purchase, expense, cash/bank accounts, customer and supplier ledgers",
            "Daily outlet closing — opening + received − paid = expected cash reconciliation",
            "Role control — Cashier, Outlet Manager, Accounts, Owner with configurable permissions",
            "Invoice print, WhatsApp delivery, and reprint capability",
        ],
        "3.8 Packing, Dispatch & Gatepass": [
            "Scan-based receiving of packed suits from production into finished goods store",
            "Packing management — order, style, packed qty, carton/box number, packing employee",
            "Dispatch to outlet, customer, or online order with pick list and courier details",
            "Gatepass creation — vehicle, driver, material, quantity, destination, authorized person, security verification",
            "Workflow: Order → Production → Quality → Finishing → Packing → Dispatch → Gatepass → Delivery",
            "Dispatch reports — daily/weekly/monthly, customer-wise, order-wise, pending vs completed",
        ],
        "3.9 Integrations": [
            "E-commerce integration — order import, SKU mapping, stock reservation, fulfilment write-back, inventory sync",
            "Courier integration — consignment booking from dispatch screen, CN/tracking storage, delivery status, COD reconciliation",
            "Returned/RTO stock released only after physical scan verification",
            "Email integration for system-generated documents and notifications",
        ],
        "3.10 Reports & Management Dashboard": [
            "Management dashboard — employees, attendance, payroll, purchases, inventory, production, dispatch, accounts",
            "Department dashboards for HR, Purchase, Inventory, Production, Accounts, and Dispatch/Security",
            "Configurable alerts — low stock, pending approvals, production delays, pending dispatch, outstanding balances",
            "PDF and Excel export on all major reports",
            "Advanced search and filter by date, department, employee, supplier, item, style, order, status",
        ],
    }

    for heading, items in scope_sections.items():
        story.append(Paragraph(heading, styles["H2"]))
        story.append(ListFlowable(
            [bullet(i) for i in items],
            bulletType="bullet", start="•", leftIndent=14,
        ))
        story.append(Spacer(1, 4))

    story.append(PageBreak())

    # 4. Implementation
    story.append(Paragraph("4. Implementation Approach", styles["H1"]))
    story.append(Paragraph(
        "Codevelix follows a phased delivery model to reduce business disruption and ensure "
        "each department is trained before the next module goes live.",
        styles["Body"],
    ))
    phases = [
        ["Phase", "Duration", "Activities", "Key Output"],
        ["Phase 1\nFoundation", "Week 1–2", "Discovery, blueprint, master data structure, users, roles, departments, chart of accounts", "Signed blueprint & configured base system"],
        ["Phase 2\nHR & Payroll", "Week 3–4", "Employee enrollment, attendance, shifts, leave, advances, PF, payroll setup", "Live HR & payroll module"],
        ["Phase 3\nPurchase & Inventory", "Week 5–6", "Requisitions, PO, receiving, stock, transfers, low-stock alerts", "Live purchase & inventory"],
        ["Phase 4\nProduction & POS", "Week 7–9", "Job Card, workflow, worker wages, costing, outlet POS (3 branches), integrations", "Live production, outlets & integrations"],
        ["Phase 5\nAccounts", "Week 10", "Vouchers, ledgers, reconciliation, financial reports, FBR invoicing", "Live accounts module"],
        ["Phase 6\nDispatch & Go-Live", "Week 11–12", "Packing, dispatch, gatepass, data migration, UAT, training, go-live, stabilisation", "Production go-live & handover"],
    ]
    story.append(make_table(phases, [0.9 * inch, 0.7 * inch, 2.8 * inch, 1.9 * inch]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>Total estimated delivery timeline: 12 weeks</b> from contract sign-off and receipt of "
        "initial master data, subject to timely client approvals and staff availability for training.",
        styles["Body"],
    ))

    # 5. Project Team
    story.append(Paragraph("5. Dedicated Project Team", styles["H1"]))
    team = [
        ["Role", "Allocation"],
        ["Project Manager", "1 — single point of contact throughout engagement"],
        ["Business Analyst / Implementation Consultant", "2 — requirement mapping, configuration, UAT"],
        ["Production / Apparel Specialist", "1 — job card, embroidery, workflow, costing setup"],
        ["Integration Engineer", "1 — e-commerce, courier, and third-party API connections"],
        ["Data Migration Engineer", "1 — master data import and opening balance verification"],
        ["Support Engineer (Post Go-Live)", "1 — dedicated for stabilisation and after-sales support"],
    ]
    story.append(make_table(team, [2.2 * inch, 4.0 * inch]))

    story.append(PageBreak())

    # 6. Commercial Proposal
    story.append(Paragraph("6. Commercial Proposal", styles["H1"]))
    story.append(Paragraph("6.1 One-Time Implementation Investment", styles["H2"]))
    commercial = [
        ["Component", "Qty", "Rate (PKR)", "Amount (PKR)"],
        ["Core Platform — Users, Roles, Security & Approvals", "1", "50,000", "50,000"],
        ["HR, Attendance & Payroll Module", "1", "105,000", "105,000"],
        ["Purchase & Procurement Module", "1", "75,000", "75,000"],
        ["Inventory, Warehouse & Stock Management", "1", "85,000", "85,000"],
        ["Production & Manufacturing (Job Card, Embroidery, Workflow, Costing, Dashboard)", "1", "170,000", "170,000"],
        ["Accounts, Finance & Reconciliation", "1", "95,000", "95,000"],
        ["Outlet POS — Branch Operations", "3", "30,000", "90,000"],
        ["Packing Store, Dispatch & Gatepass", "1", "55,000", "55,000"],
        ["E-Commerce & Courier Integration", "1", "75,000", "75,000"],
        ["Reports, Dashboards & Management Analytics", "1", "Included", "—"],
        ["Data Migration & Opening Balances", "1", "Included", "—"],
        ["On-Site Training, UAT & Go-Live Support", "1", "Included", "—"],
        ["TOTAL ONE-TIME IMPLEMENTATION", "", "", "Rs. 800,000"],
    ]
    t = make_table(commercial, [2.8 * inch, 0.5 * inch, 0.9 * inch, 1.0 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, -1), (-1, -1), LIGHT),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, -1), (-1, -1), 10),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>Payment terms:</b> 50% (Rs. 400,000) upon contract sign-off | "
        "50% (Rs. 400,000) upon go-live and final handover.",
        styles["BoldBody"],
    ))

    # After-sales
    story.append(Paragraph("6.2 After-Sales Services & Annual Maintenance", styles["H2"]))
    story.append(Paragraph(
        "Codevelix provides structured after-sales support so your operations continue smoothly "
        "after go-live. The following services are available as monthly or annual plans:",
        styles["Body"],
    ))
    support = [
        ["Service", "Standard Plan", "Premium Plan"],
        ["Cloud hosting, SSL, daily backups & system updates", "Included", "Included"],
        ["Software licence for all contracted modules", "Included", "Included"],
        ["WhatsApp, phone & email technical support", "Business hours", "24/7 priority"],
        ["Bug fixes & security patches", "Included", "Included"],
        ["Minor configuration changes", "Up to 4 hrs/month", "Up to 10 hrs/month"],
        ["New user training", "1 session/quarter", "Unlimited sessions"],
        ["Monthly system health check & performance report", "—", "Included"],
        ["Dedicated account manager", "—", "Included"],
        ["Emergency on-site visit (Lahore)", "—", "1 visit/quarter"],
        ["Monthly subscription (all users)", "Rs. 45,000/month", "Rs. 75,000/month"],
        ["Annual subscription (pay yearly — 2 months free)", "Rs. 450,000/year", "Rs. 750,000/year"],
    ]
    story.append(make_table(support, [2.5 * inch, 1.85 * inch, 1.85 * inch]))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Note:</b> After-sales subscription begins from the go-live month. First 60 days post go-live "
        "include complimentary Standard Plan support at no additional charge as part of the implementation package.",
        styles["Body"],
    ))

    story.append(Paragraph("6.3 What Is Included at No Extra Cost", styles["H2"]))
    included = [
        "Complete data migration — articles, components, colours, sizes, parties, workers, rates, opening stock and balances",
        "Role-based on-site training in Urdu or English for all departments",
        "User Acceptance Testing (UAT) support and issue resolution",
        "60-day post go-live stabilisation with dedicated support engineer",
        "Blueprint workshop within 5 working days of contract acceptance",
        "All reports, dashboards, PDF/Excel export, and audit trail features",
    ]
    story.append(ListFlowable([bullet(i) for i in included], bulletType="bullet", start="•", leftIndent=14))

    story.append(Paragraph("6.4 Exclusions", styles["H2"]))
    exclusions = [
        "Hardware — barcode scanners, label printers, POS terminals, biometric devices, and networking equipment",
        "Third-party subscription fees — e-commerce platform, courier account, SMS gateway, or payment gateway charges",
        "Government taxes (GST/SRB) applicable on services as per prevailing law",
        "Travel and accommodation for out-of-city visits beyond Lahore (if required)",
        "Additional custom features, new modules, or branches beyond three outlets — quoted separately as change requests",
        "Historical transaction data migration (opening balances and master data only are included)",
    ]
    story.append(ListFlowable([bullet(i) for i in exclusions], bulletType="bullet", start="•", leftIndent=14))

    story.append(PageBreak())

    # 7. Terms
    story.append(Paragraph("7. Terms & Conditions", styles["H1"]))
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
        story.append(Paragraph(f"<b>{title}:</b> {text}", styles["Body"]))

    # 8. Acceptance
    story.append(Paragraph("8. Agreement & Acceptance", styles["H1"]))
    story.append(Paragraph(
        "By signing below, both parties accept the scope, delivery approach, commercial terms, "
        "and after-sales services outlined in this quotation.",
        styles["Body"],
    ))
    sign = [
        ["For Codevelix", "For Zeenat Pret"],
        ["Name: ___________________________", "Name: ___________________________"],
        ["Designation: _____________________", "Designation: _____________________"],
        ["Signature & Date: ________________", "Signature & Date: ________________"],
    ]
    t = make_table(sign, [3.1 * inch, 3.1 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BRAND),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ]))
    story.append(Spacer(1, 10))
    story.append(t)
    story.append(Paragraph(
        "Codevelix — Develop a professional website and custom software for your company.<br/>"
        "https://codevelix.com/ | info@codevelix.com | +92 306 4228502 | Lahore, Pakistan",
        styles["Footer"],
    ))

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    doc.build(story)
    print(f"PDF saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
