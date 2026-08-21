# Module 03 — Inventory (Products, Variants & POS Stock)

**Company:** Zeenat Pret  
**Module:** Inventory  
**Version:** 1.0  
**Depends on:** Article/Product Master, Warehouse / Packing Store / Outlet locations  
**Feeds to:** Production FG handover, Packing Store, Outlet POS, Shopify sync, Accounts stock value

---

## 1. Purpose

Create and maintain **products (articles)**, control **variant-wise stock**, and keep Inventory synchronized with **POS**, Packing Store, Production finished goods, and online channels.

---

## 2. Product / Article Creation

### 2.1 Article Master

| Field | Required | Notes |
|-------|----------|-------|
| Article Code | Yes | e.g. ZSE #041, ZPE #033 |
| Article Name | Yes | |
| Collection / Season | Yes | |
| Category / Product Line | Yes | Frock, Suit, etc. |
| Shoot / Product Picture | Strongly recommended | Visual ID for store/POS |
| Cost / Inventory Cost | Yes (permissioned) | One defined cost basis |
| Retail Price | Yes for POS | |
| Active | Yes | |

### 2.2 Variants (Mandatory Control)

Every finished suit is controlled as:

**Article + Color + Size + Barcode/SKU**

| Field | Rule |
|-------|------|
| Color | Mandatory |
| Size | XS/S/M/L/XL or company size chart |
| SKU | Unique per variant |
| Barcode | Unique; printable from system |
| Opening stock | Optional at create |

### 2.3 Search

Search by Article Name, Article Code, SKU, Barcode, Color, Size, Collection.

---

## 3. Stock Locations

| Location | Stock type |
|----------|------------|
| Material Warehouse | Fabric / accessories (Purchase module) |
| Backup Store | Reserved non-embroidered components (Production) |
| Packing Store / FG | Finished suits available |
| In Transit | Dispatched not yet received |
| Outlet(s) | Per outlet stock |
| Reserved | Shopify / order reserved |
| Damaged / Hold | Not for sale |

**Rule:** Backup and Reserved stock are **not free stock**.

---

## 4. Stock Movements (Automatic)

| Event | Stock effect |
|-------|--------------|
| Production FG receiving | Packing Store ↑ |
| Outlet transfer dispatch | Packing Store ↓, In Transit ↑ |
| Outlet transfer receive | In Transit ↓, Outlet ↑ |
| POS sale | Outlet ↓ |
| Sale return | Outlet ↑ (after verify) |
| Customer / Shopify dispatch | Packing Store ↓ |
| Return / RTO receive + scan | Available ↑ |
| Stock adjustment | ± with reason |
| Damage / hold | Move to Damaged/Hold |

**Golden Rule:** ONE PHYSICAL MOVEMENT = ONE SYSTEM ENTRY. No manual duplicate stock entry at Packing Store, Outlet, or Shopify.

---

## 5. POS Linkage

- Products created in Inventory appear in Outlet POS after activation for that outlet (or global).  
- POS sells only variants with stock (block negative by default).  
- Price comes from article/variant price list; discount rules in POS.  
- Cost/profit visible only to permitted roles.  

---

## 6. Stock Value

- Management configures one cost basis (e.g. production/inventory cost).  
- Stock in Hand Value = available qty × inventory cost.  
- Dispatch Stock Value = dispatched qty × inventory cost for period/status.  

---

## 7. Low Stock & Alerts

- Reorder / low stock level per variant or article  
- Dashboard: Low Stock variants  
- Used by Packing Store, POS, Management  

---

## 8. Stock Audit / Physical Count

- Create audit session by location  
- Scan / count physical qty  
- System shows variance  
- Post adjustment with approval + reason  
- Full audit trail  

---

## 9. Reports

- Current stock (Article / Color / Size)  
- Stock by location  
- Stock value  
- Stock movement history  
- Low stock  
- Damaged / Hold  
- Physical stock audit variance  
- In transit  

---

## 10. Roles

| Role | Access |
|------|--------|
| Inventory User | Create articles/variants (as permitted), view stock |
| Store Manager | Adjustments, audits |
| POS Cashier | View outlet stock only (no cost) |
| Accounts / Owner | Cost & value |
| Admin | Full |

---

## 11. Acceptance Criteria

- [ ] New product creates article + color/size variants with unique SKU/barcode  
- [ ] Packing Store and Outlet stock stay in sync with transfers and sales  
- [ ] POS can sell only by barcode/SKU and reduces stock once  
- [ ] Reserved / backup stock not treated as sellable  
- [ ] Stock value reports use configured cost basis  
- [ ] Physical audit posts controlled adjustments only  
