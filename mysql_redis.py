#
#
#

import pymysql.cursors
import redis


def get_mbcapi_db_data(host, user, password, db, db_name, uid):
    connection_mbcapi_db = pymysql.connect(host=host,
                                           user=user,
                                           password=password,
                                           db=db,
                                           charset='utf8mb4',
                                           cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection_mbcapi_db.cursor() as cursor:
            sql = "select * from {} where uid={}".format(db_name, uid)
            cursor.execute(sql)
            result = cursor.fetchone()
    finally:
        connection_mbcapi_db.close()
    return result


def get_mbccalc_db_data(host, user, password, db, db_name, uid):
    connection_mbccalc_db = pymysql.connect(host=host,
                                            user=user,
                                            password=password,
                                            db=db,
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection_mbccalc_db.cursor() as cursor:
            sql = "select * from {} where uid={}".format(db_name, uid)
            cursor.execute(sql)
            result = cursor.fetchone()

    finally:
        connection_mbccalc_db.close()
    return result


def get_jfx_draw_value(host, port, password, db, get_hash):
    r = redis.StrictRedis(host=host, port=port, password=password, db=db)
    tx_hash = 'tx:' + get_hash
    from_xqlm = str(r.hget(tx_hash, 'from'), encoding='utf8')
    to_fast_wallet = str(r.hget(tx_hash, 'to'), encoding='utf8')
    jfx_value = str(r.hget(tx_hash, 'value'), encoding='utf8')
    draw_jfx = jfx_value[:-18] + '.' + jfx_value[-18:]
    return from_xqlm, to_fast_wallet, jfx_value, draw_jfx


if __name__ == '__main__':
    mysql_host = '172.17.12.60'
    mysql_user = '******'
    mysql_password = '******'
    mysql_db_mbcapi = 'my_block_chain_api'
    mysql_db_mbccalc = 'my_block_chain_calc'

    uid = 95393516
    db_user = 'api_user'
    db_jfx = 'api_user_jfx'
    db_jdr = 'jfx_draw_record_201806'

    print('{:>15}{:2}{}'.format('uid:', ' ', uid))
    print('\n', end='')

    db_name = db_user
    user_table = get_mbcapi_db_data(mysql_host, mysql_user, mysql_password, mysql_db_mbcapi, db_name, uid)
    # print(user_table)
    print('{:>15}{:2}{}'.format('mid:', ' ', user_table['mid']))
    print('{:>15}{:2}{}'.format('username:', ' ', user_table['username']))
    print('{:>15}{:2}{}'.format('phone:', ' ', user_table['phone']))
    print('{:>15}{:2}{}'.format('is_forbidded:', ' ', user_table['is_forbidded']))
    print('\n', end='')

    db_name = db_jfx
    jfx_table = get_mbcapi_db_data(mysql_host, mysql_user, mysql_password, mysql_db_mbcapi, db_name, uid)
    # print(jfx_table)
    print('{:>15}{:2}{}'.format('jfx_total:', ' ', jfx_table['jfx_total']))
    print('{:>15}{:2}{}'.format('total_draw_num:', ' ', jfx_table['total_draw_num']))
    print('\n', end='')

    db_name = db_jdr
    jdr_table = get_mbccalc_db_data(mysql_host, mysql_user, mysql_password, mysql_db_mbccalc, db_name, uid)
    # print(jdr_table)
    print('{:>15}{:2}{}'.format('draw_time:', ' ', jdr_table['draw_time']))
    draw_num = str(jdr_table['draw_num'])[:-8] + '.' + str(jdr_table['draw_num'])[-8:]
    print('{:>15}{:2}{}{:^9}{}'.format('draw_num:', ' ', jdr_table['draw_num'], '>>>>>', draw_num))
    print('{:>15}{:2}{}'.format('trade_address:', ' ', jdr_table['trade_address']))
    get_hash = jdr_table['trade_address']
    print('\n', end='')

    redis_host = '172.17.12.58'
    redis_port = 6379
    redis_password = '******'
    redis_db = 0
    jfx_draw = get_jfx_draw_value(redis_host, redis_port, redis_password, redis_db, get_hash)
    # jfx_draw[0] = from_xqlm
    print('{:>15}{:2}{}'.format('from:', ' ', jfx_draw[0]))
    # jfx_draw[1] = to_fast_wallet
    print('{:>15}{:2}{}'.format('to:', ' ', jfx_draw[1]))
    # jfx_draw[2] = jfx_value
    # jfx_draw[3] = draw_jfx
    print('{:>15}{:2}{}{:^9}{}'.format('jfx_value:', ' ', jfx_draw[2], '>>>>>', jfx_draw[3]))

    
    
