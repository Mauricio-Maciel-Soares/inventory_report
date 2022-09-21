from datetime import date
from collections import Counter


class SimpleReport:
    # def __init__(self, info: list):
    #     self.info = info

    @staticmethod
    def generate(info):
        closest_date = []
        oldest_date = []
        company_data = []
        today_date = date.today()

        for index in info:
            validate_date = date.fromisoformat(index["data_de_validade"])
            fabrication_date = date.fromisoformat(index["data_de_fabricacao"])
            company_name = index["nome_da_empresa"]

            if validate_date >= today_date:
                closest_date.append(validate_date)

            oldest_date.append(fabrication_date)

            company_data.append(company_name)

        company_bigger_stock = Counter(company_data).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {min(oldest_date)}\n"
            f"Data de validade mais próxima: {min(closest_date)}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )


#     def __iter__(self):
#         return ProfileIterator()


# class ProfileIterator:
#     def __init__(self, info):
#         self.info = info
#         self.index = 0

#     def __next__(self):
#         try:
#             result = self.info[self.index]
#         except IndexError:
#             raise StopIteration
#         self.index += 1
#         return result
