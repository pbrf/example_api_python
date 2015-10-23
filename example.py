#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib
import json

data = {}
data['type_blank'] = 'a'
data['from_name'] = 'Ивана Ивановича'
data['from_city'] = 'г. Москва'
data['from_street'] = 'ул. Стахановская'
data['from_build'] = '999'
data['from_appartment'] = '99'
data['from_zip'] = '109428'
data['whom_surname'] = 'Петрову'
data['whom_name'] = 'Петру Петровичу'
data['whom_city'] = 'г. Санкт-Петербург'
data['whom_street'] = 'ул. Гоголя'
data['whom_build'] = '888'
data['whom_appartment'] = '88'
data['whom_zip'] = '190000'
data['declared_value'] = '1000.00'
data['COD_amount'] = '1100.00'

params = {}
params['access_token'] = ''
params['data'] = json.dumps(data)

params = urllib.urlencode(params)
f = urllib.urlopen("http://pbrf.ru/pdf.F7", params)
print f.read()
