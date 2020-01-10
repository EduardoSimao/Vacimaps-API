from app.models.table_cidade import Cidade
from app.models.table_doenca_cidade import Doenca_Cidade
from app.models.table_vacina import Vacina
from app.models.table_doenca import Doenca
from app.models.table_sintoma import Sintoma
from app.models.table_doenca_sintoma import Doenca_Sintoma
from app.models.table_vacina_doenca import Vacina_Doenca
from app import db, app
from flask import request, jsonify
from app.controller.login import token_required

@app.route('/cidades', methods=['GET'])
@token_required
def get_all_city(current_user):
    dados = Cidade.query.filter_by().all()

    if not dados:
        return jsonify({'Mensagem': 'Nenhuma cidade cadastrada!'})

    cidades = []

    for info in dados:
        cidade = {}
        cidade['id_cidade'] = info.id_cidade
        cidade['nome_cidade'] = info.nome_cidade
        cidade['uf_cidade'] = info.uf_cidade

        cidades.append(cidade)

    return jsonify(cidades)


@app.route('/cidades/<cidade_id>', methods=['GET'])
@token_required
def get_one_city(current_user, cidade_id):
    info = Cidade.query.filter_by(id_cidade = cidade_id).first()
    doencas_cidades = Doenca_Cidade.query.filter_by(id_cidade = info.id_cidade).all()

    if not info:
        return jsonify({'Mensagem': 'Cidade não encontrado!'})

    cidade = {}
    cidade['id_cidade'] = info.id_cidade
    cidade['nome_cidade'] = info.nome_cidade
    cidade['uf_cidade'] = info.uf_cidade

    doencas = []
    if doencas_cidades:        
        for doenca in doencas_cidades:
            _doenca = {}
            nm_doenca = Doenca.query.filter_by(id_doenca = doenca.id_doenca).first()
            doenca_sintomas = Doenca_Sintoma.query.filter_by(id_doenca = doenca.id_doenca).all()
            doenca_vacinas = Vacina_Doenca.query.filter_by(id_doenca = doenca.id_doenca).all()
            

            _doenca['nome_doenca'] = nm_doenca.nome_doenca
            _doenca['ds_doenca'] = nm_doenca.ds_doenca
            _doenca['recomendacao'] = nm_doenca.recomendacao

            _sintomas_doenca = []
            for doenca_sintoma in doenca_sintomas:
                _sintomas = {}
                sintoma = Sintoma.query.filter_by(id_sintoma = doenca_sintoma.id_sintoma).first()

                _sintomas['nome_sintoma'] = sintoma.nome_sintoma

                _sintomas_doenca.append(_sintomas)

            _doenca['sintomas'] = _sintomas_doenca

            _vacinas_doenca = []
            for vacina_sintoma in doenca_vacinas:
                _vacinas = {}
                vacina = Vacina.query.filter_by(id_vacina = vacina_sintoma.id_vacina).first()

                _vacinas['nome_vacina'] = vacina.nome_vacina

                _vacinas_doenca.append(_vacinas)

            _doenca['vacina'] = _vacinas_doenca

            doencas.append(_doenca)

        cidade['doencas'] = doencas

    return jsonify(cidade)
