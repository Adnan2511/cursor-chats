# Module 06 — Gatepass (Delivery, Packing, Dispatch & Reports)

**Company:** Zeenat Pret  
**Module:** Gatepass  
**Version:** 1.0  
**Depends on:** Packing Store, Orders, Outlets, Courier, Inventory  
**Feeds to:** Accounts (where value/settlement), Stock in transit, Management reports

---

## 1. Purpose

Control **gatepass** for order delivery, packing and dispatch, with **per-day, weekly, monthly and annual reports**. Every physical exit of goods from factory/packing store must have a gatepass linked to the underlying dispatch/transfer.

---

## 2. Scope

| In scope | Detail |
|----------|--------|
| Gatepass creation | Against packing / dispatch / outlet transfer / customer / courier |
| Packing confirmation | Packed qty vs ordered qty |
| Dispatch confirmation | Vehicle / courier / receiver details |
| Order delivery status | Dispatched / In Transit / Delivered / Returned |
| Security / gate check | Optional verify at gate |
| Reports | Daily, weekly, monthly, annual |

---

## 3. Gatepass Types

| Type | Use |
|------|-----|
| Outlet Transfer | Packing Store → Outlet |
| Customer Delivery | Direct customer order |
| Online / Shopify | Courier dispatch |
| Job Work / Vendor Send | Material or semi-finished to vendor (if used) |
| Return Out | Goods leaving for return-to-supplier (link Purchase) |
| Other | Authorized miscellaneous with reason |

---

## 4. Gatepass Document — Required Fields

| Field | Required | Notes |
|-------|----------|-------|
| Gatepass No. | Auto unique | Searchable |
| Date & Time | Yes | |
| Type | Yes | See §3 |
| Source Location | Yes | Packing Store / Warehouse |
| Destination | Yes | Outlet / Customer / Courier / Vendor |
| Reference | Yes | Dispatch No. / Transfer No. / Order No. / Shopify Order |
| Party Name | Yes | Outlet/Customer/Courier |
| Vehicle No. / Courier / CN | As applicable | |
| Driver / Rider Name & Mobile | Optional | |
| Items | Yes | Article + Color + Size + Qty (+ barcode scan) |
| Packed By | Yes | User |
| Dispatched By | Yes | User |
| Gate Checked By | Optional | Security |
| Remarks | Optional | |
| Status | Yes | Draft / Packed / Dispatched / Delivered / Cancelled / Returned |

---

## 5. Workflow

```
1. Create / Import order or transfer
2. Pack (scan items) → status Packed
3. Generate Gatepass (auto from dispatch or manual confirm)
4. Gate verify (optional) → Dispatched
5. Delivery confirmation / Outlet receive → Delivered / Received
6. If RTO / return → Returned + stock receive scan
```

### Rules

- Gatepass quantity must match scanned packed quantity.  
- Cannot dispatch with missing/wrong variants (same scan controls as Packing Store).  
- Stock reduces on dispatch; outlet stock increases only on receive confirmation.  
- Cancellation requires reason + authorized user; no hard delete after dispatch.  
- One dispatch can map to one gatepass (preferred) or clearly linked multi-parcel gatepasses.

---

## 6. Packing Link

- Pick list: article picture, code, color, size, qty  
- Scan each item; block wrong/duplicate scan  
- Green confirmation when qty complete  
- Packing complete → ready for gatepass  

---

## 7. Dispatch & Delivery Tracking

| Status | Meaning |
|--------|---------|
| Packed | Ready at store |
| Dispatched | Left premises (gatepass done) |
| In Transit | On the way |
| Delivered | Customer/outlet confirmed |
| Returned / RTO | Coming back; available only after scan receive |

Courier tracking/CN stored and visible on gatepass.

---

## 8. Reports

### Daily
- Gatepasses issued today  
- Packed vs dispatched vs delivered today  
- Outlet-wise / courier-wise summary  
- Pending deliveries  

### Weekly
- Week gatepass register  
- Delivery performance (dispatched vs delivered)  
- Returns / RTO weekly  
- Article-wise outbound qty  

### Monthly
- Monthly dispatch volume & value (if cost linked)  
- Outlet transfer summary  
- Courier-wise monthly  
- Pending / overdue deliveries  
- Cancelled gatepasses  

### Annually
- Annual outbound summary by type  
- Outlet vs online vs customer mix  
- Year comparison (optional)  
- Top articles dispatched  

### Common report filters

Date range | Type | Outlet | Courier | Article | Collection | Status | User  

Export: PDF / Excel  

---

## 9. Dashboard Widgets

- Gatepasses today  
- Dispatched today  
- In transit  
- Delivered today  
- Returns pending  
- Pending packing  

---

## 10. Roles

| Role | Access |
|------|--------|
| Packer | Pack + prepare gatepass draft |
| Dispatch User | Confirm dispatch, courier/CN |
| Gate Security | Verify/check out |
| Store Manager | All store gatepass + cancel with reason |
| Accounts / Management | Reports & value views |
| Admin | Full |

---

## 11. Integration Points

| Module | Link |
|--------|------|
| Packing Store / Inventory | Stock movement on dispatch/receive |
| Outlet POS | Transfer receive against gatepass/transfer ref |
| Shopify / Courier | Fulfillment + tracking |
| Accounts | Dispatch value / COD settlement references |
| Production | Only when vendor send / FG handover refs needed |

---

## 12. Acceptance Criteria

- [ ] Every outbound finished-goods movement can generate a unique gatepass  
- [ ] Packing scan quantities match gatepass lines  
- [ ] Dispatch updates stock and status automatically  
- [ ] Delivery / return statuses are reportable  
- [ ] Daily, weekly, monthly, annual reports export correctly  
- [ ] Cancel/reverse leaves audit trail  
