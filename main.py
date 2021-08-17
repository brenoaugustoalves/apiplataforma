import json
import os
from flask import Flask, request
app = Flask(__name__)

def veiculo():
    request_data = request.get_json()

    fname = os.path.join(app.root_path, 'data', 'plataformas.json')

    with open(fname) as json_data:
        data = json.load(json_data)

    for req in request_data:
        largura=req.get('largura', 0)
        altura=req.get('altura', 0)
        espessura=req.get('espessura', 0)
        peso=req.get('peso', 0)

        for plat in data:
            plat['veiculos'] = [plat['veiculos'][i] for i in range(len(plat['veiculos']))
                if (plat['veiculos'][i]['largura'] >= largura and
                    plat['veiculos'][i]['altura'] >= altura and
                    plat['veiculos'][i]['espessura'] >= espessura and
                    plat['veiculos'][i]['peso'] >= peso)]

    data = [data[i] for i in range(len(data)) if data[i]['plataforma'] == 'Ogi']

    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)
