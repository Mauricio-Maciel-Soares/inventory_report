from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def __init__(self, info):
        super().__init__(info)

    @staticmethod
    def generate(info):
        full_data = SimpleReport.generate(info)

        company_name = []
        for index in info:
            company_name.append(index["nome_da_empresa"])

        dictionary = Counter(company_name)

        companies = ''
        for company, quantity in dictionary.items():
            companies += f"- {company}: {quantity}\n"

        return (
            f"{full_data}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies}"
        )
