# Module 04 — Production (Job Card, Styles, Operations & Wages)

**Company:** Zeenat Pret  
**Module:** Production  
**Version:** 1.0  
**Sources:** Meeting requirements + Production Job Card & Software Workflow PDF  
**Feeds to:** Finished Goods Store, Accounts worker payables, Purchase material consumption, Costing

---

## 1. Purpose

Control production from **approved sample to Finished Goods** using one Job Card, with:

- Daily employee/worker operations  
- New styles and style-based operations  
- Operation cost and wages (piece rate / daily)  
- New orders and order workflow wages  
- Live location, WIP, ageing, pre-cost vs post-cost  

**Primary control:** Article / Job Card / Tech Pack / BOM / stage-wise issue-receive / costing / ageing  

---

## 2. High-Level Production Workflow

```
PO / Fabric Receiving → QC → Warehouse → D-Studio / Sampling → Sample Approval
→ Tech Pack → BOM + Pre-Cost → Job Card → Dyeing (if required)
→ Embroidery + Backup Store → Adda / Patching (if required) → Cutting
→ Stitching → Handmade → Press / Finishing → Packing
→ Finished Goods Store → Dispatch / Close → Post-Cost & Audit
```

Every stage uses the same reconciliation: **Issued / Received / Short-Excess / Allowed Loss / Actual Loss / Recoverable Shortage / Reason / Rate / Ageing / Audit**.

---

## 3. Styles (New Style Creation)

| Feature | Requirement |
|---------|-------------|
| Create style / article | From D-Studio / Product Development |
| Sample | Create, approve/reject; keep version + image |
| Tech Pack | Measurements, size plan, fabric consumption, trims, process route, color, approved sample ref, version |
| BOM + Pre-Cost | Materials + planned consumption + rates + planned amount |
| Style operations | Define operation sequence for the style (see §5) |
| Version control | Tech Pack / BOM / Job Card versions; changes after release need approval |

---

## 4. Production Job Card — Master Control Document

Created after sample approval; linked to Article, Tech Pack version, BOM, planned qty, production route.

### 4.1 Job Card Header

| Field | Rule |
|-------|------|
| Job Card No. | Auto unique, searchable |
| Article Code / Name | Linked to approved sample |
| Collection / Season | Collection reporting |
| Design / Product Line / Category | e.g. Frock / Summer |
| Color | Mandatory color-wise tracking |
| Planned Suit Qty | Base for all component plans |
| Plan Date / Required Date | Ageing / overdue |
| Tech Pack Version | Lock after production release |
| BOM Version | Revision requires approval |
| Prepared / Verified / Approved By | User + date + time |

### 4.2 Embroidery Instruction (Required)

Per component line:

Component/Placement | Embroidery Yes/No | Fabric Stuff | Color | PPC/Consumption | Machine Heads | Meter/Repeat | Repeats | Fabric to Embroidery (m) | Expected Output | Backup to Store | Remarks

**Configurable machine-head standards (not hard-coded):**

- 24-head ≈ 8.50 m per repeat  
- 28-head ≈ 9.50 m per repeat  

**Formula:** Fabric to Embroidery = Repeats × Meter per Repeat  

Fabric Stuff and Color are separate mandatory columns (Lawn, Organza, Chiffon, Net, Cotton, etc.).

### 4.3 Embroidery + Backup Logic

- Only components with Embroidery = Yes are issued to embroidery.  
- Non-embroidered components (e.g. Back, Trouser) reserved as **BACKUP** against Job Card + Article + Color + Component.  
- Backup is **not free stock**.  
- After embroidery receipt & reconciliation: Embroidery Received + Backup Released = consolidated issue to next stage.  
- Shortage / rejection / damage / excess recorded with reason, responsible vendor/team, approval before backup release.

### 4.4 Backup Store Register

Job Card | Article | Component | Fabric Stuff | Color | Backup Qty | UOM | Location | Reserved Date | Release Date | Released Qty | Balance | Status  

Statuses: Reserved / Partially Released / Released / Hold / Excess Returned  

---

## 5. Style-Based Operations & Daily Working

Meeting requirement: employees work daily on operations; salaries/wages based on operation work.

### 5.1 Operation Master

Examples: Dyeing, Embroidery, Cutting, Patching, Stitching (Shirt/Trouser/Dupatta), Adda/Handmade, Press, Packing, QC, etc.

| Field | Notes |
|-------|-------|
| Operation Code / Name | Unique |
| Unit | Piece / Meter / Bundle / Day |
| Default rate | Optional |
| Department | |
| Active | |

### 5.2 Style → Operations Mapping

For each style/article, define ordered operations with:

- Operation  
- Rate per piece / process (Article + Process rate card)  
- Expected sequence  
- Whether piece-rate payable to worker/team  

### 5.3 Daily Worker Operation Entry

| Field | Requirement |
|-------|-------------|
| Date | Working date |
| Worker / Team | From Worker Master |
| Job Card / Article / Order | Link |
| Operation / Process | Style operation |
| Completed Qty | Yes |
| Rate | From rate card (editable with approval) |
| Payable | Qty × Rate (auto) |
| Status | Draft / Approved / Posted to Accounts |

**Rules:**

- Production records completed qty; Accounts receives approved qty automatically.  
- Do not pay above approved production completion without override.  
- Same approved work cannot be paid twice.  
- Rate change needs authorization + history.  

---

## 6. Orders & Order Workflow Wages

| Feature | Requirement |
|---------|-------------|
| New production order | Customer/internal order linked to Article + Qty + delivery date |
| Order → Job Card | Create/link Job Card(s) for order qty |
| Order progress | Stage-wise % / qty complete |
| Wages by order | Worker operation entries filterable by order; wage settlement by order or weekly combined |
| Close order | When FG received and variances approved |

Example (from Accounts PDF): Article ZSE #041, PO Qty 240 — shirt stitching workers X/Y/W with completed qtys; trouser, dupatta, press, packing teams — all auto payable.

---

## 7. Stage Controls (Summary)

| Stage | Key control |
|-------|-------------|
| PO / Fabric Receiving | PO ref, supplier, stuff, color, width, lot, qty, meters |
| QC | Accept/Reject/Hold + defects/images |
| Warehouse | Stock after QC; PO loss separate |
| Dyeing | Meter issue/receive; shrinkage tolerance; debit if recoverable |
| Embroidery | Repeat-wise; heads; meters; good/reject; vendor cost |
| Backup Store | Reserve / release |
| Cutting / Patching | Size-wise plan vs actual; bundles |
| Stitching | Bundle + size + worker issue/receive; worker cost |
| Adda / Handmade | Count-based; expected return = issue unless exception |
| Press / Packing | Finishing QC; article+color+size pack; good/reject |
| Finished Goods | Scan variant; accept good suits; production short |
| Post-Cost / Close | Actual cost ÷ good suits; variance; close approval |

---

## 8. Size-Wise Production Control

Size | Planned | Cut Actual | Stitched Actual | Packed Good | Short/Pending  

XS–XL + TOTAL — auto/entry as configured.

---

## 9. Costing

| Cost head | Pre-Cost | Post-Cost |
|-----------|----------|-----------|
| Raw Fabric | Planned m × rate | Actual warehouse consumption |
| Trims / Accessories | BOM plan | Issues − returns |
| Dyeing / Embroidery / Adda / Stitching / Press / Packing | Planned rates | Actual bills / worker payments |

**Post-Cost per good suit = Total Actual Article Cost ÷ Actual Completed Good Suits**  
Show Pre-Cost, Post-Cost, Variance Rs. and % by Article and Collection.

---

## 10. Live Location, Ageing & WIP

Every Job Card shows: Current Stage, Live Location, Issue/Receive dates, Stage Ageing, Total Ageing, Pending Days, Completed Date.  
Overdue highlighting from management-defined allowed ageing.

Live stages include: Plan, D-Studio, Sampling, Tech Pack, Job Card, Dyeing, Embroidery, Backup Store, Adda, Cutting, Patching, Stitching, Handmade, Press, Packing, Finished Goods, Dispatch.

---

## 11. Management Dashboard (Required)

KPI cards: Active/Completed/Pending Articles, Planned vs Completed Suits, Production Short, Today’s Working, Overdue, stage pendings (Dyeing/Embroidery/Cutting/Stitching/Packing), Backup reserved / awaiting release, Debit Notes, Pre/Post Cost & Variance, Average Ageing.

Also: Live Job Card table, Today Working by department, Embroidery dashboard, Backup Store dashboard, Stage WIP bottleneck, management alerts (RED/AMBER/GREEN), filters and drill-down, PDF/Excel export.

---

## 12. Weekly Worker Payment Link (Accounts)

Applies especially to **Stitchers, Press Team, Packing Team**:

1. Create PO / Article  
2. Record work (Production)  
3. Auto payable (Qty × rate)  
4. Weekly review (Accounts)  
5. Weekend payment (one settlement combining all articles)  

Worker ledger: Opening payable → This week work → Advance/Deduction → Net → Paid → Closing.

---

## 13. Job Card Closure Checklist

- [ ] Approved sample & Tech Pack linked  
- [ ] BOM approved  
- [ ] Planned qty & size plan confirmed  
- [ ] Embroidery components Yes/No set  
- [ ] Fabric Stuff & Color entered  
- [ ] Machine heads & m/repeat confirmed  
- [ ] Repeats & meters calculated  
- [ ] Backup reserved for non-embroidered components  
- [ ] Embroidery reconciled  
- [ ] Backup released & combined  
- [ ] All stage issue/receive reconciled  
- [ ] Shortages/rejections/debit notes resolved/approved  
- [ ] FG good qty posted  
- [ ] Post-Cost calculated  
- [ ] Production short & cost variance reviewed  
- [ ] Closed by authorized user  

---

## 14. Essential Production Reports

Job Card register; Embroidery repeat plan & reconciliation; Fabric stuff/color; Backup reserve/release; Plan vs actual; WIP/live location; Size-wise production; FG handover; Department pending; BOM; Material consumption; Pre vs Post cost; Cost sheet; Collection costing; Cost variance; PO loss; Dyeing shrinkage; Recoverable shortage; Debit notes; Ageing; Overdue; Version history; User activity; Approval/edit audit; Daily worker operation & wage report; Order-wise production & wages.

---

## 15. Roles

Warehouse, QC, D-Studio/Fashion, Sampling, Production User, Department User, Production Manager, Costing/Accounts, Admin/Owner.

---

## 16. Acceptance Criteria

- [ ] Job Card created only from approved sample/Tech Pack/BOM  
- [ ] Embroidery meters calculate from configurable head standards  
- [ ] Backup stock reserved and released only after embroidery reconciliation  
- [ ] Daily operation entries create worker payables without double payment  
- [ ] Order workflow shows progress and wages by order/article  
- [ ] Size-wise plan vs actual visible  
- [ ] Pre vs Post cost and variance available at close  
- [ ] Live dashboard shows location, ageing, bottlenecks, alerts  
