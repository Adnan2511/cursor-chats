# Module 05 — Accounts (Vyapar-Style, Connected & Audit Friendly)

**Company:** Zeenat Pret  
**Module:** Accounts  
**Version:** 1.0  
**Source:** Accounts Department Software Requirement PDF + meeting requirements  
**Style:** Simple like Vyapar — vouchers, party ledgers, cash/bank, payable/receivable, day book, reports

---

## 1. Purpose

Provide a complete accounts system with **supplier ledger, expenses, petty cash, cash & bank, worker payments, receivables/payables, reconciliation, and financial reports**, fully connected to Production, Store, Outlets, Purchase, Shopify/Online and Courier — **without re-entering** department transactions.

---

## 2. Core Accounts Principle

```
1. Department Entry → 2. Auto Posting → 3. Verify → 4. Pay / Receive → 5. Reconcile
```

### Golden Rules

- ONE TRANSACTION = ONE ENTRY.  
- Every financial posting has unique reference and link to original department transaction.  
- Keep UI simple: clear vouchers, ledgers, cash/bank, day book, reports.

### Connected Departments

| Source | What Accounts receives |
|--------|------------------------|
| Production | Worker qty / job work payables |
| Packing Store | Stock receiving / dispatch value movement |
| Outlets / POS | Sales / cash / expenses |
| Purchase | Supplier bills / payables |
| Shopify / Online | Orders / payments / refunds |
| Courier | COD / charges / returns |
| HR | Salary, advances, PF postings |
| Gatepass / Dispatch | Delivery-linked settlements where financial |

---

## 3. Menu / Modules

1. Dashboard  
2. Worker Payments  
3. Purchase  
4. Expense (incl. Petty Cash)  
5. Cash & Bank  
6. Ledger / Parties  
7. Reconciliation  
8. Reports  

---

## 4. Worker Payments (Weekly Job Work)

Special method for **Stitchers, Press Team, Packing Team**.

### Flow

1. Create PO / Article  
2. Production records work  
3. Auto payable = Approved Qty × Rate  
4. Weekly review  
5. Weekend payment (Cash/Bank)  

### Example Pattern

Article ZSE #041, PO Qty 240 — multiple workers/processes (shirt stitching, trouser, dupatta, press, packing) with completed qty and auto payable status Unpaid → Paid.

### Worker Ledger

Opening Payable → Previous Unpaid → This Week Work → Advance/Deduction → Net Payable → Paid This Week → Closing Payable  

Also: Articles worked count/detail; Payment status Unpaid / Partial / Paid.

### Weekly Payment Screen Flow

Select Week → Select Worker → Review Detail (Article + Process + Qty + Rate) → Approve → Pay & Voucher  

### Worker / Team Master

Name/Team, Mobile, CNIC/ID (if required), Process Type, Active/Inactive.  
Rate by Article + Process (or default process rate).  
Rate changes need approval + history.

### Controls

- No pay above approved production qty without override  
- No double pay for same approved work  
- Edits after approval: user, date, time, old/new  
- Partial payment leaves balance in ledger  
- Voucher shows worker, week, article-wise detail, gross, advance/deduction, paid, balance  

---

## 5. Purchase / Supplier

- Supplier bill/invoice + reference  
- Items, qty, cost, tax/charges  
- Paid / Partial / Credit  
- Supplier payable auto-update  
- Purchase return / debit adjustment  

---

## 6. Expense & Petty Cash

### Expense

| Field | Notes |
|-------|-------|
| Category | Salary / Courier / Fuel / Rent / Utilities / Marketing / Misc / etc. |
| Amount | Yes |
| Description | Yes |
| Paid from | Cash / Bank / Petty Cash |
| Bill attachment | Supported |
| Department / cost center | Yes |
| User | Auto |

### Petty Cash

- Petty cash account with opening balance  
- Small expenses issued from petty cash  
- Replenishment from main cash/bank  
- Petty cash book: In / Out / Closing  
- Limit warnings as configured  

---

## 7. Cash & Bank

- Cash in Hand and bank accounts  
- Opening / Money In / Money Out / Closing  
- Deposit / withdrawal / account transfer  
- Payment and receipt vouchers  
- Daily cash reconciliation  
- Outlet cash deposits appear automatically  

---

## 8. Parties / Ledger

| Party type | Use |
|------------|-----|
| Worker payable | Job work |
| Supplier payable | Purchases |
| Customer receivable | Credit sales / outlets |
| Courier / COD settlement | Online deliveries |
| Employee advances | HR |

Invoice/voucher-wise balance; statements; due/overdue where applicable.

---

## 9. Automatic Day Book

Every approved payment, receipt, purchase, expense, worker settlement, outlet cash deposit, supplier payment and customer receipt posts to Day Book.

Columns: Date/Time | Reference | Department | Transaction Type | Party | Payment Method | Money In | Money Out | User  

---

## 10. Department Reconciliation

| Department | Compare | Result |
|------------|---------|--------|
| Production | PO Qty vs Completed vs Worker Payable | Unapproved / excess / unpaid visible |
| Finished Goods | Production completion vs Store receiving vs Stock value | Qty/value difference |
| Outlet / POS | Sales vs Cash/Card/Bank vs Returns/Expenses | Daily closing difference |
| Shopify / Online | Orders vs Payments vs Fulfillment vs Refunds | Pending payment/refund |
| Courier | COD dispatched vs Delivered/Returned vs COD received | Courier receivable/charges |
| Purchase | Supplier invoice vs receipt vs payment | Payable & variance |
| HR Payroll | Payroll register vs payment vouchers | Unpaid salaries |

### Audit Requirement

- Open any financial entry → see original source (PO, production completion, GRN, outlet invoice, Shopify order, courier settlement, purchase bill, expense, gatepass).  
- No hard delete; cancel/reverse with reason + authorized user.  
- Complete audit trail on edit, approval, payment, reversal.  

---

## 11. Management Dashboard

Cash in Hand | Bank Balance | Worker Payable (current) | This Week Worker Payable | Supplier Payable | Customer Receivable | Courier Receivable (COD) | Today’s Expenses | Today’s Payments | Today’s Receipts | Stock Value | P&L (selected period)

---

## 12. Essential Reports

### Worker / Job Work
Worker-wise payable; Article-wise work; Process-wise work; Weekly payment; Paid/unpaid; Rate history; Advance/deduction  

### Accounts
Cash Book; Bank Book; Day Book; Payment/Receipt Voucher; Supplier Ledger; Receivable/Payable; Expense Report; Petty Cash Book  

### Department / Audit
Production / Store / Outlet closing / Shopify / Courier COD reconciliation; User audit trail; Edited/reversed entries  

### Management
Profit & Loss; Department expenses; Cash flow summary; Stock value; Outstanding liabilities/receivables; Date-wise comparison  

---

## 13. Developer Controls

- Roles: Accounts User, Accounts Manager, Department Approver, Admin/Owner  
- Unique refs for work entries, payments, receipts, purchases, expenses, reversals  
- Search by Article, PO, Worker, Supplier, Customer, Invoice, Shopify Order, Barcode/SKU, Reference, Gatepass  
- PDF/Excel export, daily backup, attachments, period locking after finalize  

---

## 14. Acceptance Criteria

- [ ] Department transactions auto-post; Accounts does not re-enter them  
- [ ] Weekly worker settlement combines multi-article work with audit detail  
- [ ] Supplier, customer, worker, courier ledgers stay balanced to vouchers  
- [ ] Petty cash and expenses post to Day Book  
- [ ] Outlet and production reconciliations show differences clearly  
- [ ] P&L and cash/bank dashboards match underlying vouchers  
- [ ] Period lock prevents silent edits  
