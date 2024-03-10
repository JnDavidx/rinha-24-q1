from typing import Union


def check_transaction(
    valor: int, tipo: str, descricao: str
) -> dict[str, Union[str, int]]:
    if (
        descricao and type(descricao) is str and len(descricao) < 11
        and type(valor) is int and valor > 0
        and (tipo == "c" or tipo == "d")
    ):
        return {
            "description": descricao,
            "type_": tipo,
            "value": valor
        }

    raise TypeError