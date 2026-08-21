# Cross-Module Integrations, Roles & Reports

**Company:** Zeenat Pret  
**Document:** Integrations / Roles / Consolidated Reports  
**Version:** 1.0  

---

## 1. Integration Map

| From | To | Data passed |
|------|----|-------------|
| Purchase GRN (QC Accept) | Material Warehouse | Stock qty + cost |
| Warehouse Issue | Production Job Card | Material consumption |
| Production Worker Ops | Accounts Worker Payable | Approved qty × rate |
| Production FG Handover | Packing Store | Article+Color+Size qty |
| Packing Store Dispatch | Gatepass | Outbound document |
| Gatepass / Transfer | Outlet Stock | In transit → received |
| Outlet POS Sale | Inventory + Accounts + Day Book | Qty, money, invoice |
| Shopify Order | Packing Store | Reserve / pick / fulfill |
| Courier COD | Accounts | Receivable / settlement |
| HR Payroll / Advance | Accounts | Salary expense, advances |
| All modules | Audit Log | User, time, before/after |

---

## 2. Shared Transaction Rules

1. Unique document numbers per type (PO, GRN, JC, GP, Sale, Payment, etc.).  
2. Posted documents: cancel/reverse only — no hard delete.  
3. Attachments allowed on financial, QC, sample, challan documents.  
4. Period lock after Accounts finalize.  
5. Negative stock blocked by default.  
6. Search globally by Article, SKU, Barcode, PO, Worker, Supplier, Customer, Invoice, Shopify Order, Gatepass, Reference.  

---

## 3. Role Matrix (Summary)

| Role | HR | Purchase | Inventory | Production | FG Store | POS | Gatepass | Accounts |
|------|----|----------|-----------|------------|----------|-----|----------|----------|
| Admin / Owner | Full | Full | Full | Full | Full | Full | Full | Full |
| Accounts Manager | View payroll | Bills/Pay | Value | Worker pay verify | Value | Ledgers | Reports | Full |
| Accounts User | — | Enter bills | — | Weekly pay entry | — | View | — | Day ops |
| HR Manager | Full HR | — | — | — | — | — | — | Advances view |
| Purchase Manager | — | Full | Material | — | — | — | — | — |
| Production Manager | — | Issue view | — | Full | FG handoff | — | Vendor GP | — |
| Store Manager | — | Receive/Issue | FG stock | Receive FG | Full | — | Full store | — |
| Dispatch / Packer | — | — | Scan | — | Pack/Dispatch | — | Create GP | — |
| Outlet Manager | — | Outlet purchase | Outlet stock | — | Receive transfer | Full outlet | Receive | Outlet expenses |
| Cashier | — | — | View outlet qty | — | — | Sales limited | — | — |

Exact permissions configurable; this matrix is the baseline.

---

## 4. Consolidated Management Reports

### Daily pack
- Sales (all outlets)  
- Cash & bank position  
- Worker payables created today  
- Production today’s working  
- FG received / dispatched  
- Gatepasses issued  
- Low stock (material + FG)  
- Expenses / petty cash  

### Weekly pack
- Worker weekly settlement  
- Production ageing / overdue  
- Purchase receipts & issues  
- Dispatch vs delivery  
- Outlet performance  

### Monthly pack
- P&L  
- Payroll & PF  
- Purchase & supplier balances  
- Stock valuation  
- Production pre vs post cost  
- Gatepass monthly volume  
- Attendance & leave summary  

### Annual pack
- Annual P&L / cash flow summary  
- Annual dispatch & sales  
- Increment & headcount history  
- Collection-wise production costing  

---

## 5. Notification / Alert Baseline

| Alert | Severity |
|-------|----------|
| Low stock (material or FG variant) | Amber |
| Job Card / stage overdue | Red |
| Embroidery shortage above tolerance | Red |
| Backup reserved but embroidery already received | Amber |
| Post-cost over pre-cost beyond limit | Red |
| Outlet cash closing variance | Red |
| COD pending beyond days | Amber |
| Payroll / worker unpaid after week close | Amber |
| Attendance missing punch | Amber |

---

## 6. Data Safety

- Daily automated backup  
- Restore procedure documented for Admin  
- Role-based access + session timeout  
- Attachment virus/size limits as per IT policy  
- Export logs for sensitive reports (optional)  

---

## 7. Implementation Phasing (Suggested)

| Phase | Modules |
|-------|---------|
| Phase 1 | Inventory masters, Purchase+Warehouse, Production Job Card core, FG Store receiving/dispatch, Accounts cash/bank/expense/supplier, Outlet POS |
| Phase 2 | Embroidery+Backup advanced, Worker weekly payments, Shopify+Courier, Gatepass reports, HR attendance+payroll |
| Phase 3 | Performance/PF deep policies, advanced dashboards, device/biometric attendance, vendor portal (optional) |

Phasing is guidance only; management may reorder.
