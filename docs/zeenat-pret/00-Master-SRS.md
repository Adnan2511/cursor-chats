# Zeenat Pret — Master Software Requirements Specification (SRS)

**Product name:** Zeenat Pret Operations & Accounts System  
**Document type:** Master SRS (working company document)  
**Version:** 1.0  
**Audience:** Management, Accounts, Production, Store, Outlets, HR, Purchase, Development team  

---

## 1. Purpose

Build one connected software system for Zeenat Pret that covers:

- HR & payroll
- Purchase of fabric, accessories and materials
- Inventory / product master (including POS products)
- Production (job cards, styles, operations, wages, orders)
- Accounts (Vyapar-style, audit-friendly, department-connected)
- Gatepass (delivery, packing, dispatch & period reports)
- Finished Goods / Packing Store
- Outlet POS
- Online (Shopify) & courier settlement hooks where required

The system must give **live stock, live production location, correct worker/supplier payables, outlet sales control, and management dashboards** without duplicate data entry.

---

## 2. Business Context

Zeenat Pret produces and sells ready-to-wear suits through:

| Channel | Flow |
|---------|------|
| Production house | PO → Warehouse → Job Card → stages → Finished Goods |
| Packing Store | Receive packed suits → stock → dispatch |
| Outlets | Transfer stock → POS sale / return / expense |
| Online | Shopify orders → reserve → pick/scan → courier |
| Direct customer | Packing Store dispatch |
| Job work / piece rate | Stitchers, Press, Packing weekly payments |

---

## 3. System Scope — Module Map

```
┌─────────────┐   ┌─────────────┐   ┌──────────────┐
│     HR      │   │  Purchase   │   │  Inventory   │
│ Attendance  │   │ Fabric/Acc. │   │ Article/SKU  │
│ Payroll     │   │ Issue/Return│   │ Variant Qty  │
└──────┬──────┘   └──────┬──────┘   └──────┬───────┘
       │                 │                  │
       ▼                 ▼                  ▼
┌──────────────────────────────────────────────────┐
│                  PRODUCTION                       │
│ Job Card · Styles · Operations · Wages · Orders  │
└───────────────────────┬──────────────────────────┘
                        ▼
┌──────────────────────────────────────────────────┐
│        FINISHED GOODS / PACKING STORE             │
│ Receive · Scan · Stock · Dispatch · Shopify      │
└───────────┬──────────────────────────┬───────────┘
            ▼                          ▼
    ┌───────────────┐          ┌───────────────┐
    │  Outlet POS   │          │   Gatepass    │
    │ Sale / Cash   │          │ Pack/Dispatch │
    └───────┬───────┘          └───────┬───────┘
            └────────────┬─────────────┘
                         ▼
              ┌────────────────────┐
              │     ACCOUNTS       │
              │ Ledgers · Pay ·    │
              │ Expense · P&L      │
              └────────────────────┘
```

---

## 4. In Scope

### 4.1 HR
Employee registration/enrollment, daily attendance, shifts, salaries/payroll, attendance correction, advance salary, PF, annual leaves, history, increments, allowances, performance.

### 4.2 Purchase
Purchasing of fabric, accessories, materials; stock; issuance; rejection; returns; exchange; daily/monthly reports; low-stock alerts.

### 4.3 Inventory
Create new products/articles; variant (Article + Color + Size + Barcode/SKU); POS product linkage; stock movements.

### 4.4 Production
Daily worker operations; new styles; style-based operations; operation cost / daily wages; new orders; order workflow wages; job card from sample to FG; embroidery + backup store; pre/post cost.

### 4.5 Accounts
Supplier ledger, expenses, petty cash, cash & bank, worker weekly payments, receivables/payables, day book, reconciliation with all departments, P&L.

### 4.6 Gatepass
Gatepass for order delivery, packing, dispatch; daily / weekly / monthly / annual reports.

### 4.7 Finished Goods / Packing Store
Receive from production, barcode scan, variant stock, outlet/customer/Shopify/courier dispatch, dashboards & reports.

### 4.8 Outlet POS
Sales, returns/exchange, stock transfers, purchase (outlet), expenses, cash & bank, parties/ledger, day book, outlet closing.

---

## 5. Out of Scope (unless later approved)

- Full manufacturing machine PLC / IoT control
- Third-party payroll tax filing automation beyond PF tracking fields
- Custom mobile apps beyond scanner/mobile-friendly web (unless specified later)
- Multi-company / multi-country consolidation (single company Zeenat Pret first)

---

## 6. Core Principles

| # | Principle | Meaning |
|---|-----------|---------|
| 1 | One transaction = one entry | No re-typing sale/production/purchase/expense already entered |
| 2 | Auto posting | Department entry → financial/stock effect posts automatically |
| 3 | Verify then pay/receive | Accounts verifies qty, rate, party, reference before settlement |
| 4 | Unique references | Every voucher, job card, gatepass, transfer has unique ID |
| 5 | Variant control | Finished goods always Article + Color + Size + SKU/Barcode |
| 6 | No negative stock | Block by default (override only with authorization) |
| 7 | Audit forever | Edits/approvals/reversals logged; no silent hard deletes |
| 8 | Period lock | After accounts finalize a period, lock with Admin unlock only |

---

## 7. Accounts Core Flow (All Departments)

1. **Department Entry** — Production / Store / Outlet / Purchase enters original transaction  
2. **Auto Posting** — Accounts receives financial effect automatically  
3. **Verify** — Accounts checks quantity, rate, party & reference  
4. **Pay / Receive** — Cash / Bank / Other payment recorded  
5. **Reconcile** — Ledger, Day Book & reports update automatically  

---

## 8. Users & Environments

| Environment | Users |
|-------------|-------|
| Head office | Admin/Owner, Accounts, HR, Purchase, Management |
| Production floor | Production Manager, Department users, Warehouse, QC, D-Studio |
| Packing Store | Receiver, Picker/Packer, Dispatch, Store Manager |
| Outlets | Cashier, Outlet Manager |
| Vendors (optional portal later) | View-only job issue/receive (future) |

---

## 9. Non-Functional Requirements

| Area | Requirement |
|------|-------------|
| Performance | Outlet POS barcode scan & sale complete < 2–3 seconds typical |
| Availability | Daily business hours + evening outlet; backup nightly |
| Security | Role-based access; session logout; password policy |
| Backup | Daily backup + restore option |
| Export | PDF / Excel for all major reports |
| Attachments | Bills, QC images, sample images, challans, Tech Pack |
| Devices | Desktop + mobile/tablet friendly for scan screens |
| Search | Article, SKU, barcode, PO, worker, supplier, customer, invoice, gatepass, Shopify order |

---

## 10. Master Data (Shared)

Must exist as shared masters used by all modules:

- Company / Outlet / Warehouse / Store locations  
- Employees / Workers / Teams  
- Suppliers / Customers / Couriers / Vendors  
- Article / Collection / Category / Color / Size  
- SKU / Barcode  
- Fabric Stuff / Material / Accessories item master  
- Process / Operation master (stitching, press, packing, embroidery, etc.)  
- Rate cards (article + process, piece rates)  
- Chart of accounts / expense categories  
- Payment methods (Cash, Bank, Card/EDC, Online, Cheque, Split)  
- Shifts / Leave types / Allowance types  

---

## 11. Success Criteria

- Production can run Job Card from sample approval to Finished Goods with live WIP  
- Packing Store receives and dispatches by scan without duplicate stock  
- Outlets sell by barcode with automatic stock & accounts posting  
- Accounts pays weekly stitchers/press/packing from approved production qty only  
- HR payroll uses attendance + advances + allowances + PF + leaves  
- Purchase & material store show low stock and full issue/return history  
- Gatepass reports available daily, weekly, monthly, annually  
- Management sees dashboards for cash, stock value, payables, production ageing, P&L  

---

## 12. Related Module Documents

See folder `docs/zeenat-pret/modules/` for detailed functional requirements per module.
