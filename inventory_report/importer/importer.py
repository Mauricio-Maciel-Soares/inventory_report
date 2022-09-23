from abc import ABC, abstractmethod
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xml.etree.ElementTree as ET


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


class XmlStrategy(GenerateStrategy):
    @classmethod
    def read_data(cls, path, report):
        tree = ET.parse(path)
        root = tree.getroot()
        xml_file = []

        for index in root:
            dictionary = {}
            for index2 in index:
                dictionary[index2.tag] = index2.text
            xml_file.append(dictionary)

        if report == "simples":
            return SimpleReport.generate(xml_file)

        else:
            return CompleteReport.generate(xml_file)
