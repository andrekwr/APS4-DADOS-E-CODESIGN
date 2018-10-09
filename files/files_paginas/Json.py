import json

geral = {}

geral['abahome'] = {}
geral['abafotos'] = {}

geral['abahome']['feitos'] = {}
geral['abahome']['feitos']['teorico'] = {'titulo': 'aaaaaaaa', 'descricao':'bbbbbbbb', 'foto':'ggggggggg'}
geral['abahome']['feitos']['criatividade'] = {'titulo': 'aaaaaaaa', 'descricao':'bbbbbbbb', 'foto':'ggggggggg'}
geral['abahome']['feitos']['projeto'] = {'titulo': 'aaaaaaaa', 'descricao':'bbbbbbbb', 'foto':'ggggggggg'}
geral['abahome']['feitos']['trabalho'] = {'titulo': 'aaaaaaaa', 'descricao':'bbbbbbbb', 'foto':'ggggggggg'}

geral['abafotos']['migue'] = {}
geral['abafotos']['migue']['titulos'] = {'titulo': 'titulo 1', 'oqeh':'bbbbbbbb', 'foto1':'ggggggggg', 'foto2':'ggggggggg', 'foto3':'ggggggggg'}
geral['abafotos']['migue']['titulos'] = {'titulo': 'titulo 1', 'oqeh':'bbbbbbbb', 'foto1':'ggggggggg', 'foto2':'ggggggggg', 'foto3':'ggggggggg'}
geral['abafotos']['migue']['titulos'] = {'titulo': 'titulo 1', 'oqeh':'bbbbbbbb', 'foto1':'ggggggggg', 'foto2':'ggggggggg', 'foto3':'ggggggggg'}
    

with open('jadson.json', 'w') as zeviado:
    json.dump(geral, zeviado, sort_keys=True, indent=4)