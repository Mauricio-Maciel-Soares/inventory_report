from abc import ABC, abstractmethod
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json


class GenerateStrategy(ABC):  # Interface
    @staticmethod  # é possível chamá-lo sem instanciar um objeto da classe.
    @abstractmethod
    def read_data(cls):
        raise NotImplementedError


class CsvStrategy(GenerateStrategy):
    @classmethod
    def read_data(cls, path, report):
        csv_file = []
        with open(path) as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            for index in content:
                csv_file.append(index)

        if report == "simples":
            return SimpleReport.generate(csv_file)

        else:
            return CompleteReport.generate(csv_file)


class JsonStrategy(GenerateStrategy):
    @classmethod
    def read_data(cls, path, report):
        with open(path) as file:
            json_file = json.load(file)

        if report == "simples":
            return SimpleReport.generate(json_file)

        else:
            return CompleteReport.generate(json_file)

# class XlmStrategy(GenerateStrategy):
#     @classmethod
#     def read(cls, path, report):
#         # Codigos específico do Bradesco (exemplo)
#         print("Sucesso!")
