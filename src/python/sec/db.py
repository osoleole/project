# Sec db functions

import asyncio
import asyncpg

async def run():
    conn = await asyncpg.connect(user='postgres', password='17omB17fl',
                                 database='lamedoc', host='127.0.0.1')
    values = await conn.fetch('''SELECT * FROM sec_links
                              WHERE form_type = \'S-4\'
                              AND download_status = FALSE''')
    for value in values:
        print(value['link'])

    await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
