# Module 08 — Outlet POS

**Company:** Zeenat Pret  
**Module:** Outlet POS  
**Version:** 1.0  
**Source:** Outlet POS Software Requirement PDF  

---

## 1. Purpose

Provide a simple outlet point-of-sale with stock, purchase, expense, cash & bank, parties/ledger, day book and reports — automatically posting to Accounts and Inventory without duplicate entry.

**Menus:** POS/Sale | Purchase | Stock | Expense | Cash & Bank | Parties/Ledger | Day Book | Reports | Settings  

---

## 2. Core POS Sale Flow

```
1. Select Item → 2. Customer → 3. Discount → 4. Payment → 5. Complete Sale
```

Barcode/SKU/Article → Color/Size/Qty/Price → Walk-in or saved customer → Item or bill discount (% or Rs.) → Paid/Partial/Credit (Cash/Card/Bank/Online/Split) → Invoice (Print / WhatsApp / Reprint)

### Automatic Posting After Sale

Invoice created (unique ref) → Stock updated → Accounts updated (Cash/Bank/Receivable) → Day Book updated  

**Golden Rule:** ONE TRANSACTION = ONE ENTRY. Never re-enter sale/purchase/expense/payment/return/transfer in Stock, Accounts or Day Book.

---

## 3. Module Requirements

### POS / Sale
- Scan/search by Barcode, SKU, Article, Code  
- Article > Color > Size > Qty  
- Walk-in or saved customer (Name / Mobile / City)  
- Discount: item-level or bill-level  
- Payment status: Paid / Partial / Credit  
- Payment methods: Cash / Card-EDC / Bank / Online / Cheque / Split  
- Hold & Resume Bill  
- Return / Exchange from original invoice  

### Stock
- Current stock by Article / Color / Size  
- Transfer: Warehouse/Packing Store → Outlet (Draft / Dispatched / Received)  
- Stock adjustment with reason  
- Damaged stock  
- Stock audit / physical count  
- Low stock alert  
- Stock movement history  

### Purchase (Outlet)
- Supplier, invoice/ref, items, qty, cost  
- Paid / Partial / Credit  
- Supplier payable auto-update  
- Stock increases on receipt  
- Purchase return  

### Expense
- Categories: Rent / Electricity / Salary / Courier / Stationery / Marketing / Internet / Fuel / Misc.  
- Amount; Paid From Cash/Bank/Card  
- Description / Bill photo / Ref  
- Employee/user who entered  
- Auto-post to Day Book  

### Cash & Bank
- Cash in Hand, Bank, POS/EDC, Online payment accounts  
- Opening / Money In / Money Out / Closing  
- Deposit / withdrawal / transfer  

### Parties / Ledger
- Customer receivable; Supplier payable  
- Invoice-wise balance; due date & overdue  
- Receive / Make payment  
- Party statement  

### Day Book (Auto)
Time | Ref | Transaction | Party | Payment | Money In | Money Out  

---

## 4. Dashboard — Today

Total Sale | Invoices | Cash | Card/EDC | Online | Expenses | Receivable | Payable | Cash in Hand | Stock Value | Low Stock | Returns  

---

## 5. Essential Reports

**Sales:** Daily/Monthly; Item-wise; Salesperson; Payment method; Discount; Sale return  

**Stock:** Current; Movement; Transfer; Low stock; Adjustment; Stock value  

**Accounts:** Cash Book; Bank Book; Day Book; Receivable; Payable; Expense; P&L  

**Purchase:** Purchase report; Supplier-wise; Purchase return; Supplier balance  

---

## 6. Outlet Closing

```
Expected Closing Cash = Opening Cash + Cash Received − Cash Paid
```

System must support daily outlet closing with difference reason if variance.

---

## 7. Roles

| Role | Can do | Restricted |
|------|--------|------------|
| Cashier | Sale, receive payment, hold/resume, reprint | No cost/profit; no delete; return/discount limits |
| Outlet Manager | Sales, returns, transfers, adjustments, expenses, reports | Sensitive accounting/settings by permission |
| Accounts | Purchases, expenses, cash/bank, ledgers, P&L | POS ops if not assigned |
| Admin / Owner | Full | — |

---

## 8. Developer Controls

- Audit trail on edit, delete, refund, stock adjustment  
- Unique Sale / Purchase / Expense / Payment / Transfer / Return refs  
- Daily backup, role permissions, session logout, restore  
- Search by invoice, mobile, article, barcode, SKU, customer, supplier  
- PDF / Excel export  

---

## 9. Acceptance Criteria

- [ ] Sale by barcode reduces stock and posts cash/bank/receivable once  
- [ ] Return/exchange links to original invoice  
- [ ] Transfer receive required before outlet stock increases  
- [ ] Day Book shows all outlet money movements automatically  
- [ ] Outlet closing cash formula matches transactions  
- [ ] Cashier cannot see cost/profit or delete invoices  
