from django.db import connection

# fetch 쿼리 dict 형태로 변경
def fetchDict(cursor):
    columns = [col[0] for col in cursor.description]
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return rows

# 이메일 중복 체크
def email_check(email):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM members WHERE " \
                "MEM_EMAIL = '{}' ".format(email)

        cursor.execute(query)
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        return result[0]
    except:
        return None

# 회원 등록
def insert_member(param):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO members SET " \
                "MEM_NM = '{name}'," \
                "MEM_EMAIL = '{email}'," \
                "MEM_PASSWORD = '{password}'," \
                "MEM_NNM = '{nick}'," \
                "MEM_BD = '{birthday}'," \
                "MEM_GENDER = '{gender}'," \
                "MEM_CONTACT = '{contact}'".format_map(param)
        result = cursor.execute(query)
        connection.commit()
        connection.close()

        return result
    except:
        return None

# 이메일/패스워드 체크
def login_check(param):
    try:
        cursor = connection.cursor()
        query = "SELECT MEM_SEQ FROM members WHERE " \
                "MEM_EMAIL = '{email}' AND " \
                "MEM_PASSWORD = '{password}' ".format_map(param)

        cursor.execute(query)
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        return result[0]
    except:
        return None

# 회원정보 가져오기
def get_member(seq):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM members WHERE " \
                "MEM_SEQ = '{}'".format(seq)

        cursor.execute(query)
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        return result[0]
    except:
        return None

# 회원정보 수정
def member_update(param):
    try:
        cursor = connection.cursor()
        query = "UPDATE members SET " \
                "{} = '{}' " \
                "WHERE MEM_SEQ = '{}'".format(param['type'], param['val'], param['seq'])
        cursor.execute(query)
        connection.commit()
        connection.close()

        return True
    except:
        return False

# 회원질의 가져오기
def get_setting(seq):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM settings WHERE " \
                "MEM_SEQ = '{}'".format(seq)

        cursor.execute(query)
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        return result[0]
    except:
        return None

# 회원질의 등록
def setting_insert(param):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO settings SET " \
                "MEM_SEQ = '{seq}'," \
                "MEM_HEIGHT = '{height}'," \
                "MEM_WEIGHT = '{weight}'," \
                "MEM_ACTIVITY = '{activity}'," \
                "VEGE_CLASS_SEQ = '{vegeclass}'," \
                "VEGE_DAILY = '{vegedaily}'," \
                "VEGE_WEEKLY = '{vegeweekly}'".format_map(param)
        result = cursor.execute(query)
        connection.commit()
        connection.close()

        return result
    except:
        return None

# 회원질의 수정
def setting_update(param):
    try:
        cursor = connection.cursor()
        query = "UPDATE settings SET " \
                "{} = '{}' " \
                "WHERE MEM_SEQ = '{}'".format(param['type'], param['val'], param['seq'])
        cursor.execute(query)
        connection.commit()
        connection.close()

        return True
    except:
        return False

# 채식주의 분류 가져오기
def get_vegeclass():
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM vegeClass WHERE VEGE_CLASS_SEQ != 0 "

        cursor.execute(query)
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        return result
    except:
        return None

# 식단 가져오기
def get_plan(param):
    try:
        cursor = connection.cursor()
        query = "SELECT mealPlan.PLAN_SEQ, mealPlan.RCP_SEQ, mealPlan.PLAN_TYPE, mealPlan.IS_ACTION, mealPlan.IS_VEGE, recipe.RCP_NM, recipe.RCP_PARTS_DTLS ,recipe.ATT_FILE_NO_MAIN, recipe.INFO_EMISSIONS FROM mealPlan " \
                "LEFT JOIN recipe ON recipe.RCP_SEQ = mealPlan.RCP_SEQ " \
                "WHERE mealPlan.MEM_SEQ = '{seq}' AND " \
                "mealPlan.PLAN_DATE = '{date}' " \
                "ORDER BY mealPlan.PLAN_TYPE ASC ".format_map(param)

        cursor.execute(query)
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        return result
    except:
        return None

# 탄소배출량 계산
def get_plan_emissions(param):
    try:
        cursor = connection.cursor()
        params = {}
        params['seq'] = param['seq']
        query = "SELECT SUM(INFO_EMISSIONS) as `EMISSIONS` FROM mealPlan " \
                "WHERE MEM_SEQ = '{seq}' "

        if 'date' in param.keys():
            query += "AND PLAN_DATE = '{date}' "
            params['date'] = param['date']

        if 'action' in param.keys():
            query += "AND IS_ACTION = 1 "
        
        if 'foot' in param.keys():
            query += "AND IS_VEGE = 1 "

        cursor.execute(query.format_map(param))
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        return result[0]
    except:
        return None

def check_plan(param):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM mealPlan WHERE " \
                "PLAN_DATE = '{date}' AND " \
                "MEM_SEQ = '{seq}' AND " \
                "PLAN_TYPE = '{type}' ".format_map(param)

        cursor.execute(query)
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        if result:
            return True
        else:
            return False
    except:
        return False

def insert_plan(param):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO mealPlan SET " \
                "PLAN_DATE = '{date}'," \
                "MEM_SEQ = '{seq}'," \
                "RCP_SEQ = '{rcp}'," \
                "INFO_EMISSIONS = '{emissions}'," \
                "PLAN_TYPE = '{type}'," \
                "IS_ACTION = 0," \
                "IS_VEGE = '{isvege}'".format_map(param)
        result = cursor.execute(query)
        connection.commit()
        connection.close()

        return result
    except:
        return None

# 레시피 초기화
def reset_plan(param):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM mealPlan WHERE " \
                "PLAN_DATE = '{date}' AND " \
                "MEM_SEQ = '{seq}' ".format_map(param)
        result = cursor.execute(query)
        connection.commit()
        connection.close()

        return True
    except:
        return False

def get_emissions_avg(seq):
    try:
        cursor = connection.cursor()
        query = "SELECT AVG(a.EMISSIONS) AS `AVG_EMISSIONS` FROM (SELECT SUM(mealPlan.INFO_EMISSIONS) AS `EMISSIONS` FROM mealPlan " \
                "WHERE MEM_SEQ = '{}' " \
                "AND IS_ACTION = 1 " \
                "GROUP BY PLAN_DATE) AS a ".format(seq)

        cursor.execute(query)
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        return result[0]
    except:
        return 0
# 레시피 가져오기
def get_recipe(seq):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM recipe WHERE " \
                "RCP_SEQ = '{}'".format(seq)

        cursor.execute(query)
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        return result[0]
    except:
        return None

# 레시피 가져오기
def get_recipe_list():
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM recipe "

        cursor.execute(query)
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        return result
    except:
        return None

def plan_action_update(param):
    try:
        cursor = connection.cursor()
        query = "UPDATE mealPlan SET " \
                "IS_ACTION = '{val}' " \
                "WHERE PLAN_SEQ = '{seq}'".format_map(param)
        cursor.execute(query)
        connection.commit()
        connection.close()

        return True
    except:
        return False

def get_emissions(nm):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM carbonEmissions_Ingredients WHERE ING_NM = '{}' limit 1".format(nm)

        cursor.execute(query)
        result = fetchDict(cursor)
        connection.commit()
        connection.close()

        return result[0]['EMISSIONS']
    except:
        return 0
    
def recipe_emissions(seq,val):
    try:
        cursor = connection.cursor()
        query = "UPDATE recipe SET " \
                "INFO_EMISSIONS = '{}' " \
                "WHERE RCP_SEQ = '{}'".format(val,seq)
        cursor.execute(query)
        connection.commit()
        connection.close()

        return True
    except:
        return False