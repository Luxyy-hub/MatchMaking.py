from files.workers.api import *
@app.route('fortnite/api/matchmaking/session/<sid>', methods=['POST', 'GET'])
async def test(request,sid: str):
    reqbody = request.body
    reqheader = request.headers
    paramz = request.args
    res = requests.get('https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/matchmaking/session/'+sid+'', headers=reqheader)
    resjson = json.loads(res.text)
    resheaders = res.headers
    return sanic.response.json(resjson, headers=resheaders)
@app.route('fortnite/api/matchmaking/session/<sid>/<met>', methods=['POST', 'GET'])
async def test(request,sid: str,met: str):
    reqbody = request.body
    reqheader = request.headers
    paramz = request.args
    res = requests.get('https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/matchmaking/session/'+sid+'', params=paramz, headers=reqheader)
    resheaders = res.headers
    return sanic.response.json(json.loads(res.text), headers=resheaders)
@app.route('fortnite/api/game/v2/matchmakingservice/ticket/player/<sid>/', methods=['POST', 'GET'])
async def test(request,sid: str):
    reqbody = request.body
    reqheader = request.headers
    request.args['player.platform'] = 'Windows'
    paramz = request.args
    res = requests.get('https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/matchmakingservice/ticket/player/'+sid+'', params=paramz, headers=reqheader)
    resjson = json.loads(res.text)
    resheaders = res.headers
    #open('files/cache/bearer.json','w+').truncate(0)
    #open('files/cache/bearer.json','w+').write('\n'+reqheader['authorization'])
    return sanic.response.text(res.text, headers=resheaders)
