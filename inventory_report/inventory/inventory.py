from inventory_report.importer.importer import CsvStrategy


class Inventory:
    def __init__(self, path_strategy):
        self.path_strategy = path_strategy

    def read_data(self, path, report):
        return self.path_strategy.read_data(path, report)

    @staticmethod
    def import_data(path, report):
        if path.endswith(".csv"):
            return Inventory(CsvStrategy).read_data(path, report)
