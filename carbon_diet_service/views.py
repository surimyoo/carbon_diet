<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django import forms
import hashlib, json, datetime
import module.pymodule, module.dbmodule

weekday_dict = {0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}

def login_session_check(request):
    if request.session.get('member_index'):
        return True
    else:
        return False

# Create your views here.
def index(request):
    if login_session_check(request) == False :
        return redirect('/login')
    if request.GET.get('dt'):
        today = datetime.date.fromisoformat(request.GET['dt'])
    else:
        today = datetime.date.today()
    # 월요일
    monday = today - datetime.timedelta(days=(today.weekday() % 7))
    # 일요일
    sunday = monday + datetime.timedelta(days=6)

    week = {}
    g = 0
    while monday <= sunday:
        week[g] = {
            'days' : monday.day,
            'week' : weekday_dict[g],
            'ymd' : monday.isoformat(),
        }
        g += 1
        monday += datetime.timedelta(days=1)

    # 식단 가져오기
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
            return redirect('/')
        else:
            return HttpResponse('<script>alert("로그인 실패"); history.back();</script>');
    elif request.method == "GET":
        return render(request, 'login.html', { 'js_name' : 'login', 'css_name' : 'login' })

def logout(request):
    del request.session['member_index']
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
    view_data = {
        'js_name' : 'insight',
        'css_name' : 'insight',
        'title' : 'Insight',
    }
    return render(request, 'insight.html', view_data)
height= [x for x in range(140,200)]
def question(request):
    if login_session_check(request) == False :
        return redirect('/login')
    if request.method == "POST":
        val = request.POST['value']
        if request.POST['type'] == 'height':
            col = 'MEM_HEIGHT'
    param = {
            'type' : col,
            'val' : val,
            'seq' : request.session['member_index'],
        }

        result = module.dbmodule.setting_update(param)
        return HttpResponse(json.dumps({ 'result' : result, 'msg' : '' }))
        
    'MEN_HEIGHT'=height 
    col = 'MEM_HEIGHT'
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
    if request.method == "POST":
        val = request.POST['value']
    #if request.GET.get('seq') is None:
        #return redirect('/')
    
        

    result = module.dbmodule.get_recipe(1)
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
    if request.method == "POST":
        result = module.dbmodule.plan_action_update({
            'seq' : request.POST['seq'],
            'val' : request.POST['val'],
        })
        return HttpResponse(json.dumps({ 'result' : result, 'msg' : '' }))
    else:
        return redirect('/')

def test(request):
    #for i in range(1,811):
    #    if i == 181 or i == 246 or i == 295:
    #        continue
    #    module.dbmodule.recipe_emissions(i,module.pymodule.parts_calc_carbon(i))
    #return HttpResponse(json.dumps({ 'result' : 'ok', 'msg' : '' }, ensure_ascii=False))
    return HttpResponse(json.dumps({ 'result' : module.pymodule.parts_calc_carbon(request.GET['seq']), 'msg' : '' }, ensure_ascii=False))
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 3128f53d2a75ea65a7c373844860465fa416ea76
