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
        f"O produto {result.nome_do_produto} "
        f"fabricado em {result.data_de_fabricacao} "
        f"por {result.nome_da_empresa} com validade "
        f"até {result.data_de_validade} "
        f"precisa ser armazenado {result.instrucoes_de_armazenamento}."
    )

    assert str(result) == expected
