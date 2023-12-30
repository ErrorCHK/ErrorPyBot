import aiomysql

async def run_query(query=''):
    host_name  = 'sql12.freemysqlhosting.net'
    database   = 'sql12666065'
    user_name  = 'sql12666065'
    password   = 'g2BtmXhnEz'
    db = await aiomysql.connect(host=host_name, user=user_name, password=password, db=database, charset='utf8mb4')
    cursor = await db.cursor(aiomysql.DictCursor)
    await cursor.execute(query)
    if query.upper().startswith('SELECT') :
        data = await cursor.fetchall()
    else :
        await db.commit()
        data = None
    await cursor.close()
    db.close()
    return data
#ayncio.run(run_query("SELECT * FROM pruebas WHERE ID='1070166097'"))