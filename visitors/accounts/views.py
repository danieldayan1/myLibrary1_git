from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages 
from .models import Visitor 
from .forms import ProfileForm
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    
    context = {'form': UserCreationForm()}
    entrance_from = request.session.get("entrance_from")

    if request.method == 'POST':
        form_filled = UserCreationForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()

            u_username = form_filled.cleaned_data['username']
            u_password = form_filled.cleaned_data['password1']
            user = authenticate(username = u_username, password = u_password)  

            if user :
                if entrance_from == 'staff':
                    #ADD STAFF
                    user.is_staff = True
                    user.save()
                    Visitor.objects.get(user=user).delete()
                    return HttpResponse("<h1>worker added to staff succefuly !<h1>")
                else:
                    #ADD VISITOR
                    login(request, user)
                    return redirect('update-profile') 
            else:
                messages.add_message(request, messages.WARNING, "User not authenticated!")
        else:
            return render(request, 'register.html', {'form': form_filled})

    return render(request, 'register.html', context)

def user_login(request):

    if request.user.is_staff:
        #homepage for staff
        return redirect('Home_staff')
    elif request.user.is_authenticated:
        #homepage for visitor
        return redirect('Home_visitors')
    
    if 'SignUp' in request.GET:
        request.session["entrance_from"] = "regular"
        return redirect('register')
    else:
        u_username = request.GET.get('username')
        u_password = request.GET.get('password')
        user = authenticate(username = u_username, password = u_password)
      
        if user:
            login(request, user)
            if user.is_staff:
                next_url = 'Home_staff'
            else:
                next_url = 'Home_visitors'
            next = request.GET.get('next', next_url)
            return redirect(next)
        else:
            form = AuthenticationForm(request.GET)
            context = {'form': form}
            messages.add_message(request, messages.WARNING, "User not authenticated!")
            return render(request, 'login.html', context)

    context = {'form': AuthenticationForm}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def update_profile(request):
  
    profile = request.user.customer
    form = ProfileForm(request.POST  or None, instance=profile)
    context = {'form': form}

    if 'back' in request.POST:
        return redirect('profile')
    elif form.is_valid():
        form.save()
        return redirect('profile')
    else:
        context['errors'] = form.errors


    return render(request, 'update_profile.html', context)

@login_required(login_url='login')
def profile(request):

    COUNTRIES = (
        (None, _('None')),
        ('AD', _('Andorra')),
        ('AE', _('United Arab Emirates')),
        ('AF', _('Afghanistan')),
        ('AG', _('Antigua & Barbuda')),
        ('AI', _('Anguilla')),
        ('AL', _('Albania')),
        ('AM', _('Armenia')),
        ('AN', _('Netherlands Antilles')),
        ('AO', _('Angola')),
        ('AQ', _('Antarctica')),
        ('AR', _('Argentina')),
        ('AS', _('American Samoa')),
        ('AT', _('Austria')),
        ('AU', _('Australia')),
        ('AW', _('Aruba')),
        ('AZ', _('Azerbaijan')),
        ('BA', _('Bosnia and Herzegovina')),
        ('BB', _('Barbados')),
        ('BD', _('Bangladesh')),
        ('BE', _('Belgium')),
        ('BF', _('Burkina Faso')),
        ('BG', _('Bulgaria')),
        ('BH', _('Bahrain')),
        ('BI', _('Burundi')),
        ('BJ', _('Benin')),
        ('BM', _('Bermuda')),
        ('BN', _('Brunei Darussalam')),
        ('BO', _('Bolivia')),
        ('BR', _('Brazil')),
        ('BS', _('Bahama')),
        ('BT', _('Bhutan')),
        ('BV', _('Bouvet Island')),
        ('BW', _('Botswana')),
        ('BY', _('Belarus')),
        ('BZ', _('Belize')),
        ('CA', _('Canada')),
        ('CC', _('Cocos (Keeling) Islands')),
        ('CF', _('Central African Republic')),
        ('CG', _('Congo')),
        ('CH', _('Switzerland')),
        ('CI', _('Ivory Coast')),
        ('CK', _('Cook Iislands')),
        ('CL', _('Chile')),
        ('CM', _('Cameroon')),
        ('CN', _('China')),
        ('CO', _('Colombia')),
        ('CR', _('Costa Rica')),
        ('CU', _('Cuba')),
        ('CV', _('Cape Verde')),
        ('CX', _('Christmas Island')),
        ('CY', _('Cyprus')),
        ('CZ', _('Czech Republic')),
        ('DE', _('Germany')),
        ('DJ', _('Djibouti')),
        ('DK', _('Denmark')),
        ('DM', _('Dominica')),
        ('DO', _('Dominican Republic')),
        ('DZ', _('Algeria')),
        ('EC', _('Ecuador')),
        ('EE', _('Estonia')),
        ('EG', _('Egypt')),
        ('EH', _('Western Sahara')),
        ('ER', _('Eritrea')),
        ('ES', _('Spain')),
        ('ET', _('Ethiopia')),
        ('FI', _('Finland')),
        ('FJ', _('Fiji')),
        ('FK', _('Falkland Islands (Malvinas)')),
        ('FM', _('Micronesia')),
        ('FO', _('Faroe Islands')),
        ('FR', _('France')),
        ('FX', _('France, Metropolitan')),
        ('GA', _('Gabon')),
        ('GB', _('United Kingdom (Great Britain)')),
        ('GD', _('Grenada')),
        ('GE', _('Georgia')),
        ('GF', _('French Guiana')),
        ('GH', _('Ghana')),
        ('GI', _('Gibraltar')),
        ('GL', _('Greenland')),
        ('GM', _('Gambia')),
        ('GN', _('Guinea')),
        ('GP', _('Guadeloupe')),
        ('GQ', _('Equatorial Guinea')),
        ('GR', _('Greece')),
        ('GS', _('South Georgia and the South Sandwich Islands')),
        ('GT', _('Guatemala')),
        ('GU', _('Guam')),
        ('GW', _('Guinea-Bissau')),
        ('GY', _('Guyana')),
        ('HK', _('Hong Kong')),
        ('HM', _('Heard & McDonald Islands')),
        ('HN', _('Honduras')),
        ('HR', _('Croatia')),
        ('HT', _('Haiti')),
        ('HU', _('Hungary')),
        ('ID', _('Indonesia')),
        ('IE', _('Ireland')),
        ('IL', _('Israel')),
        ('IN', _('India')),
        ('IO', _('British Indian Ocean Territory')),
        ('IQ', _('Iraq')),
        ('IR', _('Islamic Republic of Iran')),
        ('IS', _('Iceland')),
        ('IT', _('Italy')),
        ('JM', _('Jamaica')),
        ('JO', _('Jordan')),
        ('JP', _('Japan')),
        ('KE', _('Kenya')),
        ('KG', _('Kyrgyzstan')),
        ('KH', _('Cambodia')),
        ('KI', _('Kiribati')),
        ('KM', _('Comoros')),
        ('KN', _('St. Kitts and Nevis')),
        ('KP', _('Korea, Democratic People\'s Republic of')),
        ('KR', _('Korea, Republic of')),
        ('KW', _('Kuwait')),
        ('KY', _('Cayman Islands')),
        ('KZ', _('Kazakhstan')),
        ('LA', _('Lao People\'s Democratic Republic')),
        ('LB', _('Lebanon')),
        ('LC', _('Saint Lucia')),
        ('LI', _('Liechtenstein')),
        ('LK', _('Sri Lanka')),
        ('LR', _('Liberia')),
        ('LS', _('Lesotho')),
        ('LT', _('Lithuania')),
        ('LU', _('Luxembourg')),
        ('LV', _('Latvia')),
        ('LY', _('Libyan Arab Jamahiriya')),
        ('MA', _('Morocco')),
        ('MC', _('Monaco')),
        ('MD', _('Moldova, Republic of')),
        ('MG', _('Madagascar')),
        ('MH', _('Marshall Islands')),
        ('ML', _('Mali')),
        ('MN', _('Mongolia')),
        ('MM', _('Myanmar')),
        ('MO', _('Macau')),
        ('MP', _('Northern Mariana Islands')),
        ('MQ', _('Martinique')),
        ('MR', _('Mauritania')),
        ('MS', _('Monserrat')),
        ('MT', _('Malta')),
        ('MU', _('Mauritius')),
        ('MV', _('Maldives')),
        ('MW', _('Malawi')),
        ('MX', _('Mexico')),
        ('MY', _('Malaysia')),
        ('MZ', _('Mozambique')),
        ('NA', _('Namibia')),
        ('NC', _('New Caledonia')),
        ('NE', _('Niger')),
        ('NF', _('Norfolk Island')),
        ('NG', _('Nigeria')),
        ('NI', _('Nicaragua')),
        ('NL', _('Netherlands')),
        ('NO', _('Norway')),
        ('NP', _('Nepal')),
        ('NR', _('Nauru')),
        ('NU', _('Niue')),
        ('NZ', _('New Zealand')),
        ('OM', _('Oman')),
        ('PA', _('Panama')),
        ('PE', _('Peru')),
        ('PF', _('French Polynesia')),
        ('PG', _('Papua New Guinea')),
        ('PH', _('Philippines')),
        ('PK', _('Pakistan')),
        ('PL', _('Poland')),
        ('PM', _('St. Pierre & Miquelon')),
        ('PN', _('Pitcairn')),
        ('PR', _('Puerto Rico')),
        ('PT', _('Portugal')),
        ('PW', _('Palau')),
        ('PY', _('Paraguay')),
        ('QA', _('Qatar')),
        ('RE', _('Reunion')),
        ('RO', _('Romania')),
        ('RU', _('Russian Federation')),
        ('RW', _('Rwanda')),
        ('SA', _('Saudi Arabia')),
        ('SB', _('Solomon Islands')),
        ('SC', _('Seychelles')),
        ('SD', _('Sudan')),
        ('SE', _('Sweden')),
        ('SG', _('Singapore')),
        ('SH', _('St. Helena')),
        ('SI', _('Slovenia')),
        ('SJ', _('Svalbard & Jan Mayen Islands')),
        ('SK', _('Slovakia')),
        ('SL', _('Sierra Leone')),
        ('SM', _('San Marino')),
        ('SN', _('Senegal')),
        ('SO', _('Somalia')),
        ('SR', _('Suriname')),
        ('ST', _('Sao Tome & Principe')),
        ('SV', _('El Salvador')),
        ('SY', _('Syrian Arab Republic')),
        ('SZ', _('Swaziland')),
        ('TC', _('Turks & Caicos Islands')),
        ('TD', _('Chad')),
        ('TF', _('French Southern Territories')),
        ('TG', _('Togo')),
        ('TH', _('Thailand')),
        ('TJ', _('Tajikistan')),
        ('TK', _('Tokelau')),
        ('TM', _('Turkmenistan')),
        ('TN', _('Tunisia')),
        ('TO', _('Tonga')),
        ('TP', _('East Timor')),
        ('TR', _('Turkey')),
        ('TT', _('Trinidad & Tobago')),
        ('TV', _('Tuvalu')),
        ('TW', _('Taiwan, Province of China')),
        ('TZ', _('Tanzania, United Republic of')),
        ('UA', _('Ukraine')),
        ('UG', _('Uganda')),
        ('UM', _('United States Minor Outlying Islands')),
        ('US', _('United States of America')),
        ('UY', _('Uruguay')),
        ('UZ', _('Uzbekistan')),
        ('VA', _('Vatican City State (Holy See)')),
        ('VC', _('St. Vincent & the Grenadines')),
        ('VE', _('Venezuela')),
        ('VG', _('British Virgin Islands')),
        ('VI', _('United States Virgin Islands')),
        ('VN', _('Viet Nam')),
        ('VU', _('Vanuatu')),
        ('WF', _('Wallis & Futuna Islands')),
        ('WS', _('Samoa')),
        ('YE', _('Yemen')),
        ('YT', _('Mayotte')),
        ('YU', _('Yugoslavia')),
        ('ZA', _('South Africa')),
        ('ZM', _('Zambia')),
        ('ZR', _('Zaire')),
        ('ZW', _('Zimbabwe')),
        ('ZZ', _('Unknown or unspecified country')),
    ) 
  
    if request.user.is_staff:
        return redirect('admin:index')
    
    visitor = get_object_or_404(Visitor,user=request.user)
    context={'profile': str(visitor).split(',')}
    context['country_to_show'] = dict(COUNTRIES)[visitor.country]
    
    return render(request, 'profile.html', context)
