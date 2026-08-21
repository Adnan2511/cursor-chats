# Module 02 — Purchase (Fabric, Accessories & Materials)

**Company:** Zeenat Pret  
**Module:** Purchase  
**Version:** 1.0  
**Depends on:** Supplier Master, Item/Material Master, Warehouse, Accounts  
**Feeds to:** Warehouse Inventory, Production BOM issues, Accounts payables

---

## 1. Purpose

Control purchasing of **fabric, accessories and materials** with stock, issuance, rejection, returns, exchange, and daily/monthly reporting including **low-stock alerts**.

---

## 2. Item Categories

| Category | Examples |
|----------|----------|
| Fabric | Lawn, Organza, Chiffon, Net, Cotton, etc. |
| Accessories / Trims | Thread, elastic, buckram, buttons, tassels, lace, zippers |
| Other materials | Packaging materials, misc production store items |

Each item must support: Item Code, Name, Category, Unit (meter / pcs / kg), Color (where relevant), Stuff/Type, Reorder Level, Preferred Supplier, Active status.

---

## 3. Purchase Flow

```
Indent / Need → Purchase Order → Goods Receipt → QC → Stock In → Supplier Bill → Payment
```

### 3.1 Purchase Order (PO)

| Field | Required |
|-------|----------|
| PO No. | Auto unique |
| Supplier | Yes |
| Order Date / Expected Date | Yes |
| Items | Item, Color/Stuff, Qty, Rate, Amount |
| Charges / Tax | Optional |
| Remarks | Optional |
| Status | Draft / Issued / Partial Received / Closed / Cancelled |

### 3.2 Goods Receipt (GRN)

| Field | Required |
|-------|----------|
| GRN No. | Auto |
| PO reference | Yes (or direct purchase if allowed) |
| Supplier | Yes |
| Received Date | Yes |
| Lot / Batch | Recommended for fabric |
| Width / Meterage (fabric) | As applicable |
| Received Qty | Yes |
| Rejected Qty | If any |
| Accepted Qty | Auto |
| Warehouse location | Yes |
| Received By | User |
| Attachments | Challan / invoice image |

**Rule:** Inventory increases only on accepted QC quantity (see QC).

---

## 4. QC on Purchase Receipt

- Status: Accept / Reject / Hold  
- Defect notes + images  
- Accepted qty becomes available stock  
- Rejected qty does not enter free stock; may drive return/debit  

---

## 5. Stock (Material Inventory)

| Feature | Requirement |
|---------|-------------|
| Stock in hand | By item + color/stuff + location + lot |
| Stock value | Qty × approved cost rate |
| Reservation | Against Job Card / Article when issued or reserved |
| Movement history | Every in/out with reference |

---

## 6. Issuance

Issue materials to Production / Department / Job Card.

| Field | Requirement |
|-------|-------------|
| Issue No. | Unique |
| Date | Yes |
| Issued To | Department / Job Card / Article / Worker-Vendor |
| Items & Qty | Yes |
| UOM | Yes |
| Purpose | Dyeing / Embroidery / Cutting / General |
| Authorized By | Yes |
| Stock effect | Decrease available stock |

Cannot issue more than available (block by default).

---

## 7. Rejection

- Record rejected material at receipt or during process  
- Reason, responsible party, qty, photos  
- Link to debit note where recoverable  

---

## 8. Returns

### 8.1 Purchase Return (to Supplier)

- Against GRN / Bill  
- Qty, rate, reason  
- Stock decreases (if already in stock)  
- Supplier payable reduced / debit note  

### 8.2 Material Return (from Production)

- Against issue / Job Card  
- Returned qty increases store stock  
- Must match item/lot where required  

---

## 9. Exchange

- Exchange with supplier: return item A / receive item B (or same item different lot/color)  
- Both legs linked under one Exchange reference  
- Stock and supplier ledger update for both sides  
- Reason + approval mandatory  

---

## 10. Low Stock Alerts

| Rule | Detail |
|------|--------|
| Reorder level | Per item (and optionally per location) |
| Alert | Dashboard + report when stock ≤ reorder level |
| Channels | In-app alert; optional email/WhatsApp later |
| Filters | Category (Fabric / Accessories), location |

---

## 11. Daily & Monthly Reports

### Daily
- Purchases today  
- Receipts today  
- Issues today  
- Returns / rejections today  
- Low stock list  

### Monthly
- Supplier-wise purchase  
- Item-wise purchase qty & value  
- Issue consumption by department / Job Card  
- Rejection & return summary  
- Closing stock & stock value  
- PO pending (ordered not received)  

---

## 12. Accounts Link

- Supplier bill → Supplier Payable  
- Payment: Paid / Partial / Credit  
- Purchase return / debit adjustment  
- Day Book auto post  
- No re-entry of purchase already recorded in Purchase module  

---

## 13. Roles

| Role | Can do |
|------|--------|
| Purchase User | Create PO, receive, basic returns |
| Store / Warehouse | Issue, return from production, stock view |
| QC | Accept/reject receipts |
| Purchase Manager | Approvals, rate changes, exchange |
| Accounts | Bills, payments, ledgers |
| Admin | Full |

---

## 14. Acceptance Criteria

- [ ] PO → GRN → QC → Stock works without duplicate entry  
- [ ] Fabric and accessories tracked with correct UOM  
- [ ] Issuance reduces stock and links to Job Card when provided  
- [ ] Rejection, return, exchange leave full audit trail  
- [ ] Low stock alerts fire at reorder level  
- [ ] Daily and monthly purchase/stock reports export to PDF/Excel  
- [ ] Supplier ledger updates from bills and payments automatically  
