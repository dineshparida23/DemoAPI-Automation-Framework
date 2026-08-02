from openpyxl import Workbook


class ExcelWriter:

    @staticmethod
    def write_results(file_path, data):

        workbook = Workbook()

        sheet = workbook.active
        sheet.title = "Results"

        # Header
        sheet.append([
            "User ID",
            "Expected Name",
            "Actual Name",
            "Result"
        ])

        # Data
        for row in data:
            sheet.append(row)

        workbook.save(file_path)
        workbook.close()