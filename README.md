# sqlite3-class
 
Certainly! Here's a simple README file for the `Connector` class with both Persian (Farsi) and English content:

---

# Connector Class

## English

The `Connector` class in Python provides a convenient interface for interacting with SQLite databases. It encapsulates common operations such as connecting, disconnecting, executing queries, and fetching results.

### Usage

1. **Initialization:**
   ```python
   connector = Connector(database_path)
   ```
   Replace `database_path` with the path to your SQLite database file.

2. **Connect to Database:**
   ```python
   if connector.connect():
       print("Connected to the database.")
   else:
       print("Connection failed.")
   ```

3. **Execute SELECT Query:**
   ```python
   connector.select(table, items, where=None)
   ```
   - `table`: The name of the table to select from.
   - `items`: The columns to select.
   - `where` (optional): The WHERE clause of the query.

4. **Execute INSERT Query:**
   ```python
   connector.insert(table, items, values)
   ```
   - `table`: The name of the table to insert into.
   - `items`: The columns to insert data into.
   - `values`: The values to insert into the specified columns.

5. **Fetch a Single Row:**
   ```python
   success, row = connector.fetch_one()
   ```
   - `success`: A boolean indicating the success of the operation.
   - `row`: The fetched row.

6. **Fetch All Rows:**
   ```python
   success, rows = connector.fetch_all()
   ```
   - `success`: A boolean indicating the success of the operation.
   - `rows`: The fetched rows.

7. **Disconnect from Database:**
   ```python
   if connector.disconnect():
       print("Disconnected from the database.")
   else:
       print("Disconnection failed.")
   ```

## Persian (Farsi)

کلاس `Connector` در پایتون یک رابط راحت برای ارتباط با پایگاه داده‌های SQLite فراهم می‌کند. این کلاس عملیات‌های متداول مانند اتصال، قطع اتصال، اجرای کوئری‌ها و بازیابی نتایج را دربرمی‌گیرد.

### استفاده

1. **مقدماتی:**
   ```python
   connector = Connector(آدرس_پایگاه_داده)
   ```
   آدرس_پایگاه_داده را با مسیر فایل پایگاه داده SQLite خود جایگزین کنید.

2. **اتصال به پایگاه داده:**
   ```python
   if connector.connect():
       print("به پایگاه داده متصل شدید.")
   else:
       print("اتصال ناموفق بود.")
   ```

3. **اجرای کوئری SELECT:**
   ```python
   connector.select(نام_جدول, ستون‌ها, شرط=None)
   ```
   - `نام_جدول`: نام جدول برای انتخاب.
   - `ستون‌ها`: ستون‌های مورد نظر برای انتخاب.
   - `شرط` (اختیاری): شرط WHERE کوئری.

4. **اجرای کوئری INSERT:**
   ```python
   connector.insert(نام_جدول, ستون‌ها, مقادیر)
   ```
   - `نام_جدول`: نام جدول برای درج اطلاعات.
   - `ستون‌ها`: ستون‌هایی که داده در آنها قرار می‌گیرد.
   - `مقادیر`: مقادیری که در ستون‌ها قرار می‌گیرند.

5. **بازیابی یک ردیف:**
   ```python
   موفقیت, ردیف = connector.fetch_one()
   ```
   - `موفقیت`: یک بولین که موفقیت عملیات را نشان می‌دهد.
   - `ردیف`: ردیف بازیابی شده.

6. **بازیابی تمام ردیف‌ها:**
   ```python
   موفقیت, ردیف‌ها = connector.fetch_all()
   ```
   - `موفقیت`: یک بولین که موفقیت عملیات را نشان می‌دهد.
   - `ردیف‌ها`: تمام ردیف‌های بازیابی شده.

7. **قطع اتصال از پایگاه داده:**
   ```python
   if connector.disconnect():
       print("از پایگاه داده قطع اتصال برقرار شد.")
   else:
       print("قطع اتصال ناموفق بود.")
   ```

---