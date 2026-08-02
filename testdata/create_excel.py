from openpyxl import Workbook

# Create a new workbook
workbook = Workbook()

# Select active sheet
sheet = workbook.active

# Rename sheet
sheet.title = "Users"

# Add header
sheet.append(["User ID", "Expected Name"])

# Add test data
sheet.append([1, "Dinesh"])
sheet.append([2, "Rahul"])
sheet.append([3, "Amit"])

# Save workbook
workbook.save("testdata/users.xlsx")

print("Excel file created successfully!")