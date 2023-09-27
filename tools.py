import flask, requests, random, settings as cfg, json
def convbot(msgtext, LN=cfg.LN):
	cfg.SimSimi['lc'] = LN
	cfg.SimSimi['text'] = msgtext
	try:
		result = requests.get(cfg.SimSimi['url'], params=cfg.SimSimi).json()
		if (result["result"] == 100):
			return result["response"]
		else:
			return random.choice(cfg.ErroApiSimSimi)
	except:
		return random.choice(cfg.ErroApiSimSimi)
def RespTG(**args):
	respTG = {}
	__locals__ = locals()['args']
	if "method" not in __locals__:
		respTG['method'] = 'sendMessage'
	else:
		respTG['method'] = __locals__['method']
		__locals__.pop('method')
	if "text" not in __locals__:
		respTG['text'] = random.choice(cfg.ErroApiSimSimi)
	else:
		respTG['text'] = __locals__['text']
		__locals__.pop('text')
	if "chat_id" not in __locals__:
		respTG['chat_id'] = cfg.Sudo_ID
	else:
		respTG['chat_id'] = __locals__['chat_id']
		__locals__.pop('chat_id')
	if "parse_mode" not in __locals__:
		respTG['parse_mode'] = 'HTML'
	else:
		respTG['parse_mode'] = __locals__['parse_mode']
		__locals__.pop('parse_mode')
	respTG.update(__locals__)
	print(json.dumps(respTG))
	return json.dumps(respTG)

def RespFlask(response=False, status=200, headers='application/json'):
	if (headers != 'application/json'):	headers=headers
	else:	headers={'Content-Type':'application/json'}
	if (response):
		return flask.Response(response=response, headers=headers,status=200)
	else:
		return flask.Response(headers=headers,status=200)
