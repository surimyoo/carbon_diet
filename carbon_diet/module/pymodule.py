import decimal, re
import module.dbmodule

# 레시피 탄소배출량 계산
def parts_calc_carbon(seq):
    recipe = module.dbmodule.get_recipe(seq)
    if recipe is None:
        return 0

    rstr = recipe['RCP_PARTS_DTLS']
    carbon = decimal.Decimal('0.0')

    parts_arr = []
    rstr = rstr.replace('(',' ')
    rstr = rstr.replace('-',' ')
    rstr = rstr.replace(')','')
    rstr = re.sub(r'\[[^)]*\]',',', rstr)
    rstr = rstr.replace('½','0')
    rstr = rstr.replace('⅓','0')
    rstr = rstr.replace('⅔','0')
    rstr = rstr.replace('¼','0')
    rstr = rstr.replace('¾','0')
    rstr = rstr.replace('⅛','0')
    rstr = rstr.replace('⅜','0')
    rstr = rstr.replace('⅝','0')
    rstr = rstr.replace('⅞','0')
    rstr = re.sub(r' ?(\d+) ?', r' \1', rstr)
    if rstr.find('\r\n') > -1:
        str_arr = rstr.split('\r\n')
        for s in str_arr:
            if s.find(':') > -1:
                parr = s.split(':')
                for p in parr:
                    if p:
                        parts_arr.append(p)
            else:
                if s:
                    parts_arr.append(s)
    elif rstr.find(':') > -1:
        parr = rstr.split(':')
        for p in parr:
            if p:
                parts_arr.append(p)
    else:
        parts_arr.append(rstr)

    tarr = []
    for s in parts_arr:
        if s.find(',') > -1:
            parr = s.split(',')
            for p in parr:
                if p.find(' ') > -1:
                    sarr = p.split(' ')
                    for g in sarr:
                        if g:
                            tarr.append(g)
                else:
                    if p:
                        tarr.append(p)

        elif s.find(' ') > -1:
            if s.find('g') == -1:
                continue
            parr = s.split(' ')
            for p in parr:
                if p:
                    tarr.append(p)
        else:
            continue
    parts = []
    ingredient_text = ''
    ingredient_amount = ''
    temp_amount = ''
    for txt in tarr:
        if txt.find('g') > -1 or re.search(r'\d\.',txt) is not None:
            if re.search(r'\d\.',txt) is not None:
                temp_amount = txt
                continue
            ingredient_amount = decimal.Decimal(temp_amount + txt.replace('g',''))
            ingredient_amount = str(ingredient_amount)
            #ingredient_amount = temp_amount + txt

            parts.append(ingredient_text + '||' + ingredient_amount)

            ingredient_text = ''
            ingredient_amount = ''
            temp_amount = ''
        else:
            if txt == "약간" or txt.find('ml') > -1 or txt.find('적당량') > -1 or re.search(r'\d\D',txt) is not None or re.search(r'\d', txt) is not None:
                ingredient_text = ''
                continue

            if ingredient_text == '':
                ingredient_text = txt
            else:
                ingredient_text = ingredient_text + ' ' + txt

    for part in parts:
        ps = part.split('||')
        carbon += module.dbmodule.get_emissions(ps[0]) * decimal.Decimal(ps[1])

    return f"{carbon:.2f}"
