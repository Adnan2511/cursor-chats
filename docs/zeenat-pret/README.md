# Zeenat Pret — Software Requirements Documentation

**Company:** Zeenat Pret  
**Document set:** Working software requirements for ERP / operations system  
**Sources:** Meeting requirements + company-shared PDF specifications  
**Version:** 1.0  
**Status:** Working draft for implementation & review  

---

## Document Index

| # | Document | Purpose |
|---|----------|---------|
| 1 | [00-Master-SRS.md](./00-Master-SRS.md) | Overall scope, principles, module map, system rules |
| 2 | [01-HR.md](./modules/01-HR.md) | Employee enrollment, attendance, shifts, payroll, PF, leaves, performance |
| 3 | [02-Purchase.md](./modules/02-Purchase.md) | Fabric, accessories, materials — stock, issuance, rejection, returns, alerts |
| 4 | [03-Inventory.md](./modules/03-Inventory.md) | Product/article master, variant stock, POS linkage |
| 5 | [04-Production.md](./modules/04-Production.md) | Job card, styles, operations, wages, order workflow |
| 6 | [05-Accounts.md](./modules/05-Accounts.md) | Ledgers, expenses, petty cash, worker payments, reconciliation |
| 7 | [06-Gatepass.md](./modules/06-Gatepass.md) | Delivery, packing, dispatch, gatepass reporting |
| 8 | [07-Finished-Goods-Packing-Store.md](./modules/07-Finished-Goods-Packing-Store.md) | Receiving, scan, dispatch, Shopify, courier |
| 9 | [08-Outlet-POS.md](./modules/08-Outlet-POS.md) | Outlet sales, stock, cash & bank, day book |
| 10 | [09-Integrations-Roles-Reports.md](./09-Integrations-Roles-Reports.md) | Cross-module integrations, roles, reports, controls |
| 11 | [10-Acceptance-Checklist.md](./10-Acceptance-Checklist.md) | Go-live / UAT acceptance checklist |

---

## Source PDFs (Company Shared)

1. `Zeenat_Pret_Accounts_Department_Software_Requirement.pdf`
2. `Zeenat_Pret_Finished_Goods_Packing_Store_Software_Requirement_Redeveloped.pdf`
3. `Zeenat_Pret_Production_Job_Card_and_Software_Workflow.pdf`
4. `Zeenat_Pret_Outlet_POS_Software_Requirement.pdf`

Plus meeting requirements for **HR, Purchase, Inventory, Production, Accounts, Gatepass**.

---

## Golden Rules (All Modules)

1. **ONE TRANSACTION = ONE ENTRY** — Departments enter once; Accounts / Stock / Day Book update automatically. No re-entry of the same event.
2. **ONE PHYSICAL MOVEMENT = ONE SYSTEM ENTRY** — Scan once; stock updates everywhere linked.
3. Every financial or stock posting must carry a **unique reference** and link to the original department transaction.
4. **No hard delete** after approval — use cancel/reversal with reason and authorized user.
5. Full **audit trail**: User + Date + Time + Old/New values on edits, approvals, payments, and reversals.
