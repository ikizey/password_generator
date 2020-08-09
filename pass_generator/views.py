from django.shortcuts import render
from .passw_gen import gen_lower, gen_lower_upper, gen_num, gen_char_num


def generate_password(request):
    lower = gen_lower()
    lower_upper = gen_lower_upper()
    num = gen_num()
    char_num = gen_char_num()
    pass_list = [lower, lower_upper, num, char_num]
    return render(request, "pass_generator/pass_generator.html", {'pass_list': pass_list})
