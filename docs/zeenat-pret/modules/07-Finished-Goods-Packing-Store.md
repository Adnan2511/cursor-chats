# Module 07 — Finished Goods / Packing Store

**Company:** Zeenat Pret  
**Module:** Finished Goods / Packing Store  
**Version:** 1.0  
**Source:** Finished Goods Packing Store Software Requirement (Redeveloped) PDF  

---

## 1. Purpose

Manage finished packed suits from Production receiving through stock holding to dispatch for outlets, customers, Shopify/online and courier — with barcode scanning and variant-wise control.

**Menus:** Receiving Scan / Inventory | Stock | Dispatch | Shopify | Courier | Reports | Settings  

---

## 2. Core Flow

```
1. Receive Suits → 2. Scan / Count → 3. Variant Stock → 4. Store Stock → 5. Dispatch
```

Receive complete packed suits from Production → Scan Barcode/SKU → Verify Article & Qty → Article > Color > Size qty → Stock available → Dispatch to Outlet / Customer / Online Courier.

### Golden Rules

- ONE PHYSICAL MOVEMENT = ONE SYSTEM ENTRY  
- Every suit: Article + Color + Size + Barcode/SKU  
- No manual duplicate stock entry at Packing Store, Outlet or Shopify  

### Simple Stock Statuses

Received | Stock in Hand | Dispatched | In Transit | Reserved | Damaged/Hold | Returned  

---

## 3. Production → Packing Store Receiving

Production Handover → Scan Article → Verify Variant → Accept Stock → Stock Updated  

### Receiving Screen Fields

| Group | Fields |
|-------|--------|
| Article | Name/Code, Shoot Picture, Category/Collection, Cost/Stock Value |
| Variant | Color, Size, Quantity, Variant Barcode |
| Receiving | From Production, Date/Time, Production Ref/Batch, Remarks |
| Control | Barcode scan, Received By, Short/Excess Qty, Accept/Reject |

### Article Master Notes

- Shoot/product picture for visual ID  
- Multiple colors/sizes; each variant own SKU/barcode  
- Search by name, code, SKU, barcode, color, size  
- Optional barcode label print  

---

## 4. Dispatch Types

| Type | Flow |
|------|------|
| A. Outlet Transfer | Select outlet → scan suits → Draft → Packed → Dispatched → Received |
| B. Direct Customer | Select/add customer → scan → dispatch |
| C. Shopify Order | Import order → pick & scan → fulfill |
| D. Courier Dispatch | Courier + tracking/CN |
| E. Complete | Stock reduces; dispatch record saved |

### Outlet Dispatch Rules

- Packing Store → Selected Outlet  
- Validate Article + Color + Size against transfer qty  
- Packing Store ↓ on dispatch; Outlet ↑ only on outlet confirm  
- Short / excess / damaged receipt needs reason + user  

### Customer / Online Rules

- Order source: Manual / Shopify / Other Online  
- Pick list with picture, code, color, size, qty  
- Wrong variant warning; cannot complete packing  
- After packing: courier, tracking/CN, date, user  
- Status auto: Packed / Dispatched / Fulfilled per integration  

---

## 5. Shopify Integration

```
Order Imported → Reserve Stock → Pick & Scan → Dispatch → Sync Back
```

- SKU/variant mapping  
- Import: Order #, Customer, Article, Color, Size, Qty, payment/COD, delivery details  
- Reservation prevents double-promise of same stock  
- Stock sync on receive/transfer/dispatch/return/adjust per agreed location setup  
- Cancelled/unfulfilled releases reserved stock  
- Fulfillment + tracking sync back where supported  

### Scan Controls

Wrong Item → Block + Alert  
Duplicate Scan → Block + Alert  
Qty Complete → Green Confirmation  
Missing Item → Do Not Dispatch  
User Log / Time Log / Device / Audit Trail  

---

## 6. Stock Dashboard (Owner-Friendly)

Stock in Hand (suits + value) | Dispatched (suits + value) | Reserved | In Transit | Received Today | Dispatched Today | Low Stock | Damaged/Hold | Returns Pending | Available to Sell  

Order status KPIs: Total Delivered | Total Return/RTO | In Process  

### Filters

Date range | Article/Collection/Category | Color/Size | Location | Dispatch Type | Courier | Order Status | Stock Status  

### Value Rule

One configured cost basis.  
Stock in Hand Value = available qty × inventory cost.  
Dispatch Stock Value = dispatched qty × inventory cost.  

Returned stock becomes available only after physical receiving + scan verification.

---

## 7. Essential Reports

**Stock:** Current; Article/Color/Size; Value; Movement; Low Stock; Damaged/Hold; Physical Audit  

**Receiving:** Production receiving; Date-wise; Article-wise; Short/Excess; User-wise; Receiving value; Batch/Ref  

**Dispatch:** Outlet transfer; Customer; Online; Date-wise; Article-wise; In Transit; Received/Pending  

**Shopify/Courier:** Order status; Reserved; Fulfillment; Courier-wise; Tracking/CN; Return/RTO; Pending dispatch  

---

## 8. Roles

| Role | Can do | Restricted |
|------|--------|------------|
| Store Receiver | Receive, scan, view receiving | No cost change; no delete confirmed receipt |
| Picker / Packer | Pick list, scan, pack | No order qty/stock manual change |
| Dispatch User | Create dispatch + tracking | No delete completed dispatch |
| Store Manager | Receiving, dispatch, adjustment, audit, reports | Sensitive cost/settings by permission |
| Admin / Owner | Full | — |

---

## 9. Developer Controls

Audit trail | Unique Receive/Transfer/Dispatch refs | Backup/Restore | Search Article/SKU/Barcode/Order | PDF/Excel | Stock audit scan | No negative stock (default) | Article pictures  

---

## 10. Acceptance Criteria

- [ ] Production receiving updates variant stock via scan  
- [ ] Outlet transfer in-transit until outlet receives  
- [ ] Shopify reserve/fulfill/release works without double allocation  
- [ ] Wrong/duplicate scans blocked  
- [ ] Dashboard values match stock movements  
- [ ] Reports export for Store, Management, Accounts  
