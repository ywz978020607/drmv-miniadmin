from django.shortcuts import render,redirect
from conf import env

def inject_session(request, local_dict):
    request.session.pop("render")
    request.session["render"] = request.session.get("render", {
        "forbase_username": request.user.username,
        "forbase_section": env.section
    })
    request.session["render"]["forbase_path"] = "/"+request.path.strip("/")+"/"
    for key in local_dict:
        if not key.startswith("__") and str(key) != 'request':
            request.session["render"][key] = local_dict[key]


def flush_and_render(request, target, local_dict):
    inject_session(request, local_dict)
    return render(request, target, request.session["render"])