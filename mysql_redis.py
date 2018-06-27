#
#
#

import pymysql.cursors
import redis

# connection_api = pymysql.connect(host='172.17.12.60',
#                                  user='xxxxx',
#                                  password='xxxxx',
#                                  db='my_block_chain_api',
#                                  charset='utf8mb4',
#                                  cursorclass=pymysql.cursors.DictCursor)

connection_calc = pymysql.connect(host='172.17.12.60',
                                  user='xxxxx',
                                  password='xxxxx',
                                  db='my_block_chain_calc',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

try:
    # with connection_api.cursor() as cursor:
    #     sql = "select * from api_user where phone=18501605006"
    #     cursor.execute(sql)
    #     result = cursor.fetchone()
    #     print(result)
    #
    # with connection_api.cursor() as cursor:
    #     sql = "select * from api_user_jfx where uid=95393516"
    #     cursor.execute(sql)
    #     result = cursor.fetchone()
    #     print(result)

    with connection_calc.cursor() as cursor:
        sql = "select * from jfx_draw_record_201806 where uid=95393516"
        cursor.execute(sql)
        result = cursor.fetchone()
        print('[ uid ]:           ', result['uid'])
        print('[ draw_time ]:     ', result['draw_time'])
        draw = str(result['draw_num'])[:-8] + '.' + str(result['draw_num'])[-8:]
        print('[ draw_num ]:      ', result['draw_num'], '  >>>>>>  ', draw)
        print('[ trade_address ]: ', result['trade_address'])
        get_hash = result['trade_address']
        print('\n', end='')

finally:
    # connection_api.close()
    connection_calc.close()

r = redis.StrictRedis(host='172.17.12.58', port=6379, password='xxxxxx', db=0)
tx_hash = 'tx:' + get_hash
from_hash = str(r.hget(tx_hash, 'from'), encoding='utf8')
print('[ from ]:          ', from_hash)
to_hash = str(r.hget(tx_hash, 'to'), encoding='utf8')
print('[ to ]:            ', to_hash)
jfx_value = str(r.hget(tx_hash, 'value'), encoding='utf8')
draw_jfx = jfx_value[:-18] + '.' + jfx_value[-18:]
print('[ jfx_value ]:     ', jfx_value, '  >>>>>>  ', draw_jfx)


