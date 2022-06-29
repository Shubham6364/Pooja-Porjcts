from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Register,Ownsale,Ownrent
from .models import Office_Staff
from django.core.paginator import Paginator

def layout(request):

    return render(request, 'layout.html')

def index(request):
        return render(request, 'index.html')

def search(request):
    ownsale = Ownsale.objects.all().order_by('-sale_id')
    ownrent = Ownrent.objects.all().order_by('-rent_id')
    if request.method == "POST":
        prop = request.POST.get('prop')
        search = request.POST.get('search')

        find = Ownsale.objects.filter(prop_type__icontains=prop)
        find1 = Ownsale.objects.filter(location__icontains=search)

        data = {
            'ownsale': ownsale,
            'ownrent': ownrent,
            'find': find,
            'find1': find1,
        }

        return render(request, 'search.html',data)


def plans(request):
    return render(request, 'plans.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        number1 = request.POST['number1']
        number2 = request.POST['number2']
        pin = request.POST['pin']
        cpin = request.POST['cpin']

        register = Register(fname=fname,lname=lname,uname=uname,email=email,number1=number1,number2=number2,pin=pin,cpin=cpin)
        register.save()

        messages.success(request, 'User has been registered successfully')
        return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        try:
            Registerdetails = Register.objects.get(uname=request.POST['user'], pin=request.POST['pin'])
            print("uname=", Registerdetails)
            request.session['user'] = Registerdetails.user
            return redirect('/')
        except Register.DoesNotExist as e:
            messages.success(request, 'Username / Password Invalid..!')
    return render(request, 'login.html',)

def forgot(request):
    return render(request, 'forgot.html')

def user_account(request):
    return render(request, 'user_account.html')

def logout(request):
    try:
        del request.session['uname']
    except:
        return redirect('login')
    return render(request, 'index.html')

def ownrent(request):
    if request.method == 'POST':
        rent = request.POST['rent']
        prop_type = request.POST['prop_type']
        area = request.POST['area']
        car_built = request.POST['car_built']
        floor = request.POST['floor']
        total_floor = request.POST['total_floor']
        prop_age = request.POST['prop_age']
        prop_status = request.POST['prop_status']
        landmark = request.POST['landmark']
        location = request.POST['location']
        ask_rent = request.POST['ask_rent']
        deposit = request.POST['deposit']
        avail = request.POST.get('avail')
        furnish = request.POST['furnish']
        lift = request.POST.get('lift')
        gym = request.POST.get('gym')
        swimming_pool = request.POST.get('swimming_pool')
        pets_allowed = request.POST.get('pets_allowed')
        wifi_internet = request.POST.get('wifi_internet')
        camera = request.POST.get('camera')
        club_house = request.POST.get('club_house')
        fire_safety = request.POST.get('fire_safety')
        two_wheeler = request.POST.get('two_wheeler')
        four_wheeler = request.POST.get('four_wheeler')
        gas_pipe = request.POST.get('gas_pipe')
        phone_intercom = request.POST.get('phone_intercom')
        power_backup = request.POST.get('power_backup')
        servant_room = request.POST.get('servant_room')
        security_guard = request.POST.get('security_guard')
        house_keeping = request.POST.get('house_keeping')
        air_conditioning = request.POST.get('air_conditioning')
        children_ground = request.POST.get('children_ground')
        rent_img = request.FILES.get('imagerent')
        imagerent1 = request.FILES.get('imagerent1', None)
        imagerent2 = request.FILES.get('imagerent2', None)
        comment = request.POST['comment']

        ownrent = Ownrent(rent=rent,prop_type=prop_type, area=area, car_built=car_built, floor=floor, total_floor=total_floor, prop_age=prop_age,
                          prop_status=prop_status,landmark=landmark,location=location,ask_rent=ask_rent,deposit=deposit,avail=avail,furnish=furnish,
                          lift=lift, gym=gym, swimming_pool=swimming_pool, pets_allowed=pets_allowed,wifi_internet=wifi_internet, camera=camera,
                          club_house=club_house, fire_safety=fire_safety, two_wheeler=two_wheeler,four_wheeler=four_wheeler, gas_pipe=gas_pipe,
                          phone_intercom=phone_intercom, power_backup=power_backup, servant_room=servant_room,security_guard=security_guard,
                          house_keeping=house_keeping, air_conditioning=air_conditioning,children_ground=children_ground,rent_img=rent_img,
                          imagerent1=imagerent1,imagerent2=imagerent2,comment=comment)
        ownrent.save()
        messages.success(request, 'Form Submitted successfully')
        return redirect('ownrent')
    return render(request, 'ownrent.html')

def ownsale(request):
    if request.method == 'POST':
        sale = request.POST['sale']
        prop_type = request.POST['prop_type']
        area = request.POST['area']
        car_built = request.POST['car_built']
        floor = request.POST['floor']
        total_floor = request.POST['total_floor']
        prop_age = request.POST['prop_age']
        prop_status = request.POST['prop_status']
        landmark = request.POST['landmark']
        location = request.POST['location']
        selling_price = request.POST['selling_price']
        avail = request.POST['avail']
        furnish = request.POST['furnish']
        lift = request.POST.get('lift')
        gym = request.POST.get('gym')
        swimming_pool = request.POST.get('swimming_pool')
        pets_allowed = request.POST.get('pets_allowed')
        wifi_internet = request.POST.get('wifi_internet')
        camera = request.POST.get('camera')
        club_house = request.POST.get('club_house')
        fire_safety = request.POST.get('fire_safety')
        two_wheeler = request.POST.get('two_wheeler')
        four_wheeler = request.POST.get('four_wheeler')
        gas_pipe = request.POST.get('gas_pipe')
        phone_intercom = request.POST.get('phone_intercom')
        power_backup = request.POST.get('power_backup')
        servant_room = request.POST.get('servant_room')
        security_guard = request.POST.get('security_guard')
        house_keeping = request.POST.get('house_keeping')
        air_conditioning = request.POST.get('air_conditioning')
        children_ground = request.POST.get('children_ground')
        sale_img = request.FILES.get('imagesale',None)
        imagesale1 = request.FILES.get('imagesale1',None)
        imagesale2 = request.FILES.get('imagesale2',None)
        comment = request.POST['comment']

        ownsale = Ownsale(sale=sale,prop_type=prop_type, area=area, car_built=car_built, floor=floor, total_floor=total_floor, prop_age=prop_age,
                          prop_status=prop_status,landmark=landmark,location=location,selling_price=selling_price,avail=avail,furnish=furnish,
                          lift=lift,gym=gym,swimming_pool=swimming_pool,pets_allowed=pets_allowed,wifi_internet=wifi_internet,camera=camera,
                          club_house=club_house,fire_safety=fire_safety,two_wheeler=two_wheeler,four_wheeler=four_wheeler,gas_pipe=gas_pipe,
                          phone_intercom=phone_intercom,power_backup=power_backup,servant_room=servant_room,security_guard=security_guard,
                          house_keeping=house_keeping,air_conditioning=air_conditioning,children_ground=children_ground,sale_img=sale_img,
                          imagesale1=imagesale1,imagesale2=imagesale2,comment=comment)

        ownsale.save()
        messages.success(request, 'Form Submitted successfully')
        return redirect('ownsale')
    return render(request, 'ownsale.html')

def displayrent(request, rent_id):
    context = {
                'ownrent': Ownrent.objects.get(rent_id=rent_id)
    }
    return render(request, 'displayrent.html',context)

def displaysale(request, sale_id):
    context = {
                'ownsale': Ownsale.objects.get(sale_id=sale_id)
    }
    return render(request, 'displaysale.html', context)

def payment(request):
    return render(request, 'payment.html')

#=========================office_staff_panel============================================================================
def office_login(request):
    if request.method == 'POST':
       try:
           Officedetails = Office_Staff.objects.get(username=request.POST['username'],password=request.POST['password'])
           print("username=",Officedetails)
           request.session['username']= Officedetails.username
           return redirect('office_index')
       except Office_Staff.DoesNotExist as e:
           messages.success(request,'Username / Password Invalid..!')
    return render(request, 'office_login.html')

def office_logout(request):
    try:
        del request.session['username']
    except:
        return render(request, 'office_login.html')
    return render(request, 'office_login.html')

def office_layout(request):
    return render(request, 'office_layout.html')

def office_index(request):
    data = {
        'ownsale': Ownsale.objects.all().order_by('-sale_id'),
    }
    return render(request, 'office_index.html',data)

def office_rentdb(request):
    data1 = {
        'ownrent': Ownrent.objects.all().order_by('-rent_id'),
    }
    return render(request, 'office_rentdb.html',data1)

def rent_edit(request,rent_id):
    context = {
        'ownrent': Ownrent.objects.get(rent_id=rent_id)
    }

    return render(request, 'rent_edit.html',context)

def sale_edit(request,sale_id):
    ownsale = Ownsale.objects.get(sale_id=sale_id)

    if request.method=='POST':
        landmark = request.POST['landmark']
        comment = request.POST['comment']
        ownsale.landmark = landmark
        ownsale.comment = comment
        ownsale.save()
        messages.success(request,'Form Has Been Edited Successfully')
        return redirect('office_index')
    return render(request, 'sale_edit.html', {'ownsale':ownsale})

def office_view(request):
    return render(request, 'office_view.html')



def office_rentblock(request):
    return render(request, 'office_rentblock.html')

def office_saleblock(request):
    return render(request, 'office_saleblock.html')

def ssent(request):
    return render(request, 'ssent.html')
