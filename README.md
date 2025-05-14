# Supplier Data Pipeline

This is an ETL pipeline developed in three phases, which I will refer to as versions: **V1**, **V2**, and **V3**.

It collects real monthly reports from multiple suppliers gathered around a **Cooperative**, for a **Wholesale and Retail Company**. The reports come directly from the Cooperative and are manually downloaded at the end of each month.

These reports are very valuable, since they contain:

- The amount purchased from a particular supplier affiliated with the Cooperative:
  - From the **Warehouse** of the Cooperative
  - **Directly** to the Supplier
  - Occasionally, through **Special Orders** (Encargos)

Each monthly report is provided in CSV format. After manual download, the pipeline parses and transforms these files into a clean, unified dataset. This dataset becomes the foundation for business intelligence tasks such as supplier analysis, purchasing trends, and budget planning.

---

## Report Structure (Raw CSV Columns)

Each row represents a single supplier. The columns include purchase accumulations across two years and multiple channels:

| Column Name              | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `PROVEEDOR`              | Supplier name (string). Each row identifies a different supplier.           |
| `Acum. Almacén 2024`     | Accumulated purchases from the warehouse in 2024.                           |
| `Acum. Directo 2024`     | Accumulated direct purchases in 2024.                                       |
| `Acum. Encargos 2024`    | Accumulated special or custom orders in 2024 (infrequently used).           |
| `Acum. Almacén 2023`     | Accumulated purchases from the warehouse in 2023.                           |
| `Acum. Directo 2023`     | Accumulated direct purchases in 2023.                                       |
| `Acum. Encargos 2023`    | Accumulated special or custom orders in 2023 (infrequently used).           |

> **Note:** Some columns, especially those for *Encargos*, often contain missing or null values due to their limited use.

---

More details about the ETL phases, data cleaning logic, and SQL schema will be provided in their respective subfolders.

README under construction 🚧