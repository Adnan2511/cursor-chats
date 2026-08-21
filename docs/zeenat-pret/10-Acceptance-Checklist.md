# Zeenat Pret — UAT / Acceptance Checklist

**Company:** Zeenat Pret  
**Document:** Working acceptance checklist for software delivery  
**Version:** 1.0  

Use this checklist during User Acceptance Testing. Mark Pass / Fail / N/A.

---

## A. Global Principles

- [ ] One transaction posts stock/accounts/day book automatically (no re-entry)
- [ ] Unique references on all documents
- [ ] No hard delete after post; reverse/cancel with reason works
- [ ] Audit trail shows user, date/time, old/new values
- [ ] PDF/Excel export works on major reports
- [ ] Role permissions block unauthorized screens/actions
- [ ] Daily backup/restore verified by Admin

---

## B. HR

- [ ] Employee enrollment with unique code
- [ ] Shift assignment and late rules
- [ ] Daily attendance + correction with audit
- [ ] Payroll from attendance, allowances, advances, PF
- [ ] Advance payment and recovery
- [ ] Annual leave request/approval/balance
- [ ] Increment history affects payroll from effective date
- [ ] Performance review stored on employee history

---

## C. Purchase

- [ ] PO → GRN → QC → stock increase
- [ ] Fabric and accessories with correct UOM
- [ ] Issuance to Job Card / department reduces stock
- [ ] Rejection, return, exchange with ledger impact
- [ ] Low stock alert at reorder level
- [ ] Daily and monthly purchase/stock reports

---

## D. Inventory

- [ ] Create article with color/size variants and barcodes
- [ ] Product available to POS when activated
- [ ] Stock by location correct after movements
- [ ] Reserved/backup not sellable
- [ ] Stock value uses configured cost basis
- [ ] Physical audit adjustment with approval

---

## E. Production

- [ ] Style/sample/Tech Pack/BOM/Job Card version flow
- [ ] Embroidery repeat meters from configurable head standards
- [ ] Backup reserve and release after embroidery reconcile
- [ ] Stage issue/receive/shortage/debit note
- [ ] Daily worker operations create payables
- [ ] Order-linked production and wages
- [ ] Size-wise plan vs actual
- [ ] Pre vs post cost at Job Card close
- [ ] Live dashboard: location, ageing, WIP, alerts

---

## F. Accounts

- [ ] Auto posting from other departments
- [ ] Weekly worker payment with article-wise detail
- [ ] Supplier ledger, expenses, petty cash
- [ ] Cash & bank and day book accuracy
- [ ] Department reconciliations visible
- [ ] Dashboard KPIs match vouchers
- [ ] Period lock works

---

## G. Gatepass

- [ ] Gatepass created from packing/dispatch
- [ ] Scan qty matches gatepass lines
- [ ] Status: Packed → Dispatched → Delivered / Returned
- [ ] Daily / weekly / monthly / annual reports

---

## H. Finished Goods / Packing Store

- [ ] Receive from production by scan
- [ ] Outlet transfer in transit until received
- [ ] Customer/Shopify/courier dispatch
- [ ] Wrong/duplicate scan blocked
- [ ] Shopify reserve and release
- [ ] Dashboard stock and order KPIs

---

## I. Outlet POS

- [ ] Sale by barcode with payment methods including split
- [ ] Hold/resume bill
- [ ] Return/exchange from original invoice
- [ ] Stock transfer receive
- [ ] Expense and cash/bank
- [ ] Day book auto lines
- [ ] Outlet cash closing formula
- [ ] Cashier restrictions (no cost, no delete)

---

## J. Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Owner / Management | | | |
| Accounts | | | |
| Production | | | |
| Packing Store | | | |
| Outlet Manager | | | |
| HR | | | |
| Purchase | | | |
| Development Vendor | | | |

**Overall decision:** ☐ Accepted  ☐ Accepted with punch list  ☐ Rejected  

**Punch list / notes:**  

_______________________________________________________________  
_______________________________________________________________  
_______________________________________________________________  
