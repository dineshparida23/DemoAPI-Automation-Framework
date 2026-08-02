from utils.excel_writer import ExcelWriter

results = [
    [1, "Dinesh", "Dinesh", "PASS"],
    [2, "Rahul", "Rahul", "PASS"],
    [3, "Amit", "Amit", "PASS"]
]

ExcelWriter.write_results(
    "testdata/test_results.xlsx",
    results
)

print("Excel report generated successfully!")