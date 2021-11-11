#  Copyright (c) 2021 Roger Muñoz
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU Affero General Public License as
#      published by the Free Software Foundation, either version 3 of the
#      License, or (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU Affero General Public License for more details.
#
#      You should have received a copy of the GNU Affero General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
import base64
import json
import random

DWELL = 1
FLIGHT = 2
DIGRAPH = 3
TRIGRAPH = 4
FOURGRAPH = 5

generated_data = []
features = []

available_letters = "ABCDEFGHIJKLMNOPQRSTVWXYZ"

# generate 50 DWELL
for i in range(0, 50):
    aux = {
        'type': DWELL,
        'code': available_letters[random.randint(0, len(available_letters) -1)],
        'time': random.random()*10
    }
    features.append(aux)

# generate 50 FLIGHT
for i in range(0, 50):
    aux = {
        'type': FLIGHT,
        'code': available_letters[random.randint(0, len(available_letters) -1)]+available_letters[random.randint(0, len(available_letters) -1)],
        'time': random.random()*50
    }
    features.append(aux)

# generate 100 DIGRAPH
for i in range(0, 100):
    aux = {
        'type': DIGRAPH,
        'code': available_letters[random.randint(0, len(available_letters) -1)]+available_letters[random.randint(0, len(available_letters) -1)],
        'time': random.random()*75   }
    features.append(aux)

# generate 100 TRIGRAPH
for i in range(0, 50):
    aux = {
        'type': TRIGRAPH,
        'code': available_letters[random.randint(0, len(available_letters) -1)]+available_letters[random.randint(0, len(available_letters) -1)]+available_letters[random.randint(0, len(available_letters) -1)],
        'time': random.random()*100
    }
    features.append(aux)

# generate 100 FOURGRAPH4
for i in range(0, 25):
    aux = {
        'type': TRIGRAPH,
        'code': available_letters[random.randint(0, len(available_letters) -1)]+available_letters[random.randint(0, len(available_letters) -1)]+available_letters[random.randint(0, len(available_letters) -1)]+available_letters[random.randint(0, len(available_letters) -1)],
        'time': random.random()*125
    }
    features.append(aux)

generated_data.append({'features':features})
json_generated_data = json.dumps(generated_data)
b64encoded = base64.b64encode(json_generated_data.encode('utf-8'))

data = 'data:text/plain;base64,'+b64encoded.decode('utf8')
print(data)

