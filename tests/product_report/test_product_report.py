from inventory_report.inventory.product import Product


def test_relatorio_produto():
    result = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "na geladeira",
    )

    expected = (
        f"O produto Nicotine Polacrilex"
        f" fabricado em 2021-02-18"
        f" por Target Corporation com validade"
        f" até 2023-09-17"
        f" precisa ser armazenado na geladeira."
    )

    assert str(result) == expected
