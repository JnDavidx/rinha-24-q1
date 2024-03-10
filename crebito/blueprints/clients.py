from flask import Blueprint, current_app, jsonify, request
from flask.typing import ResponseReturnValue

from ..helper import check_transaction

clients = Blueprint("clients", __name__, url_prefix="/clientes")


@clients.post("/<int:id_>/transacoes")
def post_transaction(id_: int) -> ResponseReturnValue:
    status_code = 422
    response = {"erro": "transacao invalida"}

    try:
        client = current_app.db.insert_transaction(
            id_, **check_transaction(**request.get_json())
        )

        if client:
            status_code = 200
            response = client
        elif client is None:
            status_code = 404
            response = {"erro": "usuario nao encontrado"}
    except TypeError:
        pass

    return jsonify(response), status_code


@clients.get("/<int:id_>/extrato")
def get_statement(id_: int) -> ResponseReturnValue:
    statement = current_app.db.get_statement(id_)

    if statement:
        response = statement
        status_code = 200
    else:
        response = {"erro": "usuario nao encontrado"}
        status_code = 404

    return jsonify(response), status_code