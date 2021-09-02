from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django import forms
import hashlib, json, datetime, decimal, math
import module.pymodule, module.dbmodule, module.revised_reciperecommend

weekday_dict = {0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}

def login_session_check(request):
    if request.session.get('member_index'):
        return True
    else:
        return False

def setting_session_check(request):
    if request.session.get('is_setting'):
        return True
    else:
        return False

# Create your views here.
def index(request):
    if login_session_check(request) == False :
        return redirect('/login')
    if setting_session_check(request) == False :
        return redirect('/question')
    if request.GET.get('dt'):
        today = datetime.date.fromisoformat(request.GET['dt'])
    else:
        today = datetime.date.today()
    # 월요일
    monday = today - datetime.timedelta(days=(today.weekday() % 7))
    start_day = monday
    # 일요일
    sunday = monday + datetime.timedelta(days=6)

    week = {}
    g = 0
    while start_day <= sunday:
        week[g] = {
            'days' : start_day.day,
            'week' : weekday_dict[g],
            'ymd' : start_day.isoformat(),
        }
        g += 1
        start_day += datetime.timedelta(days=1)

    # 식단 가져오기
    mealplan = module.dbmodule.get_plan({ 'seq' : request.session['member_index'],'date' : today.isoformat() })
    start_day = monday
    if mealplan == [] or mealplan is None:
        setting = module.dbmodule.get_setting(request.session['member_index'])
        setPlan, vegelist = module.revised_reciperecommend.recommend_recipe_index(setting['VEGE_CLASS_SEQ'],setting['VEGE_DAILY'],setting['VEGE_WEEKLY'])
        plan_idx = 0
        for sp in setPlan:
            recipe = module.dbmodule.get_recipe(sp)
            if module.dbmodule.check_plan({
                'seq' : request.session['member_index'],
                'date' : start_day,
                'type' : plan_idx%3,
            }) == False:
                module.dbmodule.insert_plan({
                    'seq' : request.session['member_index'],
                    'rcp' : sp,
                    'date' : start_day,
                    'emissions' : recipe['INFO_EMISSIONS'],
                    'type' : plan_idx%3,
                    'isvege' : vegelist[plan_idx],
                })
            plan_idx += 1
            if plan_idx%3 == 0:
                start_day += datetime.timedelta(days=1)

        mealplan = module.dbmodule.get_plan({ 'seq' : request.session['member_index'],'date' : today.isoformat() })

    view_data = {
        'js_name' : 'main',
        'css_name' : 'main',
        'week' : week,
        'today' : today,
        'today_str' : today.isoformat(),
        'today_week' : weekday_dict[today.weekday()],
        'mealplan' : mealplan,
    }
    return render(request, 'main.html', view_data)

def login(request):
    if request.method == "POST":
        passwd = "H" + request.POST['password']
        enc = hashlib.md5()
        enc.update(passwd.encode('utf-8'))
        encPassword = enc.hexdigest()

        param = { 'email' : request.POST['email'], 'password' : encPassword }
        result = module.dbmodule.login_check(param)

        if result:
            request.session['member_index'] = result['MEM_SEQ']
            
            sets = module.dbmodule.get_setting(result['MEM_SEQ']);
            if sets:
                request.session['is_setting'] = True
                return redirect('/')
            else:
                return redirect('/question')

        else:
            return HttpResponse('<script>alert("로그인 실패"); history.back();</script>');
    elif request.method == "GET":
        return render(request, 'login.html', { 'js_name' : 'login', 'css_name' : 'login' })

def logout(request):
    del request.session['member_index']
    del request.session['is_setting']
    return redirect('/login')

def join(request):
    if request.method == "POST":
        # 이메일 중복체크
        if module.dbmodule.email_check(request.POST['email']):
            return HttpResponse('<script>alert("이메일이 중복됩니다."); history.back();</script>');
        passwd = "H" + request.POST['password']
        enc = hashlib.md5()
        enc.update(passwd.encode('utf-8'))
        encPassword = enc.hexdigest()
        param = { 'name' : request.POST['name'], 'email' : request.POST['email'], 'password' : encPassword, 'nick' : request.POST['nick'], 'birthday' : request.POST['birthday'], 'gender' : request.POST['gender'], 'contact' : request.POST['contact'] }

        module.dbmodule.insert_member(param)

        return redirect(f'/joinSuccess')
    elif request.method == "GET":
        return render(request, 'join.html', { 'js_name' : 'join', 'css_name' : 'join' })

def joinSuccess(request):
    return render(request, 'joinSuccess.html', { 'js_name' : 'joinSuccess' })

def profile(request):
    if login_session_check(request) == False :
        return redirect('/login')
    if setting_session_check(request) == False :
        return redirect('/question')
    if request.method == "POST":
        val = request.POST['value']
        if request.POST['type'] == 'email':
            col = 'MEM_EMAIL'
            if module.dbmodule.email_check(val):
                return HttpResponse(json.dumps({ 'result' : False, 'msg' : '중복된 이메일입니다.' }));
        elif request.POST['type'] == 'name':
            col = 'MEM_NM'
        elif request.POST['type'] == 'password':
            passwd = "H" + request.POST['value']
            enc = hashlib.md5()
            enc.update(passwd.encode('utf-8'))
            encPassword = enc.hexdigest()
            var = encPassword
            col = 'MEM_PASSWORD'
        elif request.POST['type'] == 'nick':
            col = 'MEM_NNM'
        elif request.POST['type'] == 'birthday':
            col = 'MEM_BD'
        elif request.POST['type'] == 'gender':
            col = 'MEM_GENDER'
        elif request.POST['type'] == 'contact':
            col = 'MEM_CONTACT'
        param = {
            'type' : col,
            'val' : val,
            'seq' : request.session['member_index'],
        }

        result = module.dbmodule.member_update(param)
        return HttpResponse(json.dumps({ 'result' : result, 'msg' : '' }))
    else:
        view_data = {
            'js_name' : 'profile',
            'css_name' : 'profile',
            'title' : 'Profile',
            'user' : module.dbmodule.get_member(request.session['member_index']),
        }
        return render(request, 'profile.html', view_data)

def setting(request):
    if login_session_check(request) == False :
        return redirect('/login')
    if setting_session_check(request) == False :
        return redirect('/question')
    if request.method == "POST":
        val = request.POST['value']
        if request.POST['type'] == 'height':
            col = 'MEM_HEIGHT'
        elif request.POST['type'] == 'weight':
            col = 'MEM_WEIGHT'
        elif request.POST['type'] == 'activity':
            col = 'MEM_ACTIVITY'
        elif request.POST['type'] == 'vegeclass':
            col = 'VEGE_CLASS_SEQ'
        elif request.POST['type'] == 'vegedaily':
            col = 'VEGE_DAILY'
        elif request.POST['type'] == 'vegeweekly':
            col = 'VEGE_WEEKLY'
        param = {
            'type' : col,
            'val' : val,
            'seq' : request.session['member_index'],
        }

        result = module.dbmodule.setting_update(param)
        return HttpResponse(json.dumps({ 'result' : result, 'msg' : '' }))
    else:
        view_data = {
            'js_name' : 'setting',
            'css_name' : 'setting',
            'title' : 'Settings',
            'user' : module.dbmodule.get_setting(request.session['member_index']),
            'vegeclass' : module.dbmodule.get_vegeclass(),
        }
        return render(request, 'setting.html', view_data)

def insight(request):
    if login_session_check(request) == False :
        return redirect('/login')
    if setting_session_check(request) == False :
        return redirect('/question')

    today = datetime.date.today()

    # 오늘 식단 발자국
    todayEmission = module.dbmodule.get_plan_emissions({
        'seq' : request.session['member_index'],
        'date' : today,
        'action' : True,
    })
    if todayEmission['EMISSIONS'] is None:
        todayEmission['EMISSIONS'] = 0

    # 전체 식단 발자국
    allEmission = module.dbmodule.get_plan_emissions({
        'seq' : request.session['member_index'],
        'action' : True,
    })
    if allEmission['EMISSIONS'] is None:
        allEmission['EMISSIONS'] = 0

    today_carbon = todayEmission['EMISSIONS'] * decimal.Decimal('0.001')
    all_carbon = allEmission['EMISSIONS'] * decimal.Decimal(0.001)
    avg_carbon = module.dbmodule.get_emissions_avg(request.session['member_index'])
    if avg_carbon['AVG_EMISSIONS'] is None:
        avg_carbon['AVG_EMISSIONS'] = 0
    carbon_contribution = round(avg_carbon['AVG_EMISSIONS'], 0)
    if carbon_contribution <= 1500:
        carbon_contribution = 1500
    elif 1500 * math.pi <= carbon_contribution:
        carbon_contribution = round(1500 * math.pi, 0)

    view_data = {
        'js_name' : 'insight',
        'css_name' : 'insight',
        'title' : 'Carbon_Diet',
        'user' : module.dbmodule.get_member(request.session['member_index']),
        # 기여도
        'carbon_contribution' : round(carbon_contribution / 100, 0),
        'today_contribution' : round(today_carbon,2),
        'all_contribution' : round(all_carbon,2),
        'car_carbon' : round(all_carbon * decimal.Decimal('4.17'),2),
        'tree_count' : round(all_carbon * decimal.Decimal('0.15281'),2),
    }
    return render(request, 'insight.html', view_data)

def question(request):
    if login_session_check(request) == False :
        return redirect('/login')
    if request.method == "POST":
        param = {
            'seq' : request.session['member_index'],
            'height' : request.POST['height'],
            'weight' : request.POST['weight'],
            'activity' : request.POST['activity'],
            'vegeclass' : request.POST['vegeclass'],
            'vegedaily' : request.POST['vegedaily'],
            'vegeweekly' : request.POST['vegeweekly'],
        }

        result = module.dbmodule.setting_insert(param)
        if result:
            r = True
        else:
            r = False
        
        request.session['is_setting'] = r

        return HttpResponse(json.dumps({ 'result' : r, 'msg' : '' }))

    else:
        view_data = {
            'js_name' : 'question',
            'css_name' : 'question',
            'title' : 'Settings',
            'user' : module.dbmodule.get_setting(request.session['member_index']),
            'vegeclass' : module.dbmodule.get_vegeclass(),
        }
        return render(request, 'question.html', view_data)

def recipe(request):
    if login_session_check(request) == False :
        return redirect('/login')
    if setting_session_check(request) == False :
        return redirect('/question')
    if request.method == "POST":
        val = request.POST['value']
    if request.GET.get('seq') is None:
        return redirect('/')

    result = module.dbmodule.get_recipe(request.GET.get('seq'))
    view_data = {
        'js_name' : 'recipe',
        'css_name' : 'recipe',
        'title' : 'Recipe',
        'recipe' : result,
    }
    return render(request, 'recipe.html', view_data)

def planaction(request):
    if login_session_check(request) == False :
        return redirect('/login')
    if setting_session_check(request) == False :
        return redirect('/question')
    if request.method == "POST":
        result = module.dbmodule.plan_action_update({
            'seq' : request.POST['seq'],
            'val' : request.POST['val'],
        })
        return HttpResponse(json.dumps({ 'result' : result, 'msg' : '' }))
    else:
        return redirect('/')

def waiting(request):
    if login_session_check(request) == False :
        return redirect('/login')
    if setting_session_check(request) == False :
        return redirect('/question')

    # 식단 초기화
    today = datetime.date.today()
    # 월요일
    monday = today - datetime.timedelta(days=(today.weekday() % 7))
    start_day = today + datetime.timedelta(days=1)
    # 일요일
    sunday = monday + datetime.timedelta(days=6)

    while start_day <= sunday:
        module.dbmodule.reset_plan({ 'seq' : request.session['member_index'],'date' : start_day.isoformat() });
        start_day += datetime.timedelta(days=1)

    return render(request, 'waiting.html', { 'js_name' : 'waiting', 'css_name' : 'waiting' })

def store(request):
    if login_session_check(request) == False :
        return redirect('/login')
    if setting_session_check(request) == False :
        return redirect('/question')
    return render(request, 'store.html', { 'js_name' : 'store', 'css_name' : 'store', 'title' : ' ' })
#def test(request):
    #for i in range(876,995):
    #    module.dbmodule.recipe_emissions(i,module.pymodule.parts_calc_carbon(i))
    #module.dbmodule.recipe_emissions(request.GET['seq'],module.pymodule.parts_calc_carbon(request.GET['seq']))
    #result = module.revised_reciperecommend.recommend_recipe_index(6,3,3)
    #return HttpResponse(result)
    #return HttpResponse(json.dumps({ 'result' : module.pymodule.parts_calc_carbon(request.GET['seq']), 'msg' : '' }, ensure_ascii=False))