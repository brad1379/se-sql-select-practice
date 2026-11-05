import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# # ------------- Basic select of all data ------------- 
# product_data = pd.read_sql("""
# SELECT *
#   FROM products;
# """, conn)

# print(product_data)

# # ------------- STEP 1: Select product name and product code and show last five products ------------- 
# product_name_and_code = pd.read_sql("""
# SELECT productName, productCode
#   FROM products;
# """, conn).tail(5)

# print(product_name_and_code)

# # ------------- STEP 2: Select product name and product code and show last five products (switch columns from previous) ------------- 
# product_name_and_code = pd.read_sql("""
# SELECT productCode, productName
#   FROM products;
# """, conn).tail(5)

# print(product_name_and_code)

# # ------------- STEP 3: Select product name and product line when product name is "Planes" keep as original otherwise "Not Planes" call new column "Planes" ------------- 
# product_name_and_code = pd.read_sql("""
# SELECT productName, productLine,
#   CASE
#   WHEN productLine = "Planes" THEN "Planes"
#   ELSE "Not Planes"
#   END AS Planes
# FROM products;
# """, conn)

# print(product_name_and_code)

# # --------------------- STEP 4: Find length of product description for each product ---------------------
# description_length = pd.read_sql("""
# SELECT length(productDescription) AS description_length
#   FROM products
# """, conn).head(5)

# print(description_length)


# # --------------------- STEP 5:  Change product vendor to all caps ---------------------
# product_vendor_upper = pd.read_sql("""
# SELECT upper(productVendor) AS caps_vendor
#   FROM products
# """, conn).head(5)

# print(product_vendor_upper)


# # --------------------- STEP 6: Change product vendor to lowercase ---------------------
# product_vendor_lower = pd.read_sql("""
# SELECT lower(productVendor) AS lower_name
#   FROM products
# """, conn).head(5)

# print(product_vendor_lower)

# # --------------------- STEP 7: Take substring of productScale ---------------------
# product_scale = pd.read_sql("""
# SELECT substr(productScale, 3, 3) AS non
#   FROM products
# """, conn)

# print(product_scale)

# # --------------------- STEP 8: Combine productVendor and productName into one column ---------------------
# product_vendor_and_name = pd.read_sql("""
# SELECT productVendor || " " || productName AS fullName
#   FROM products
# """, conn)

# print(product_vendor_and_name)

# # --------------------- STEP 9: Find difference between MSRP and buy price and round as integer with new column name  ---------------------
# round_diff = pd.read_sql("""
# SELECT CAST(round(MSRP - buyPrice) AS INTEGER) AS round_diff
#   FROM products
# """, conn)

# print(round_diff)


conn.close()