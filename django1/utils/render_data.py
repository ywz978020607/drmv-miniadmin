from django.shortcuts import render,redirect
from django.conf import settings

def inject_session(request, local_dict):
    # request.session.pop("render")
    request.session["render"] = request.session.get("render", {"forbase_section": settings.SECTION if request.user.is_authenticated else settings.SECTION_NOLOGIN})
    request.session["render"]["title"] = local_dict.get("title", settings.PATH_NAME_CACHE.get(request.path, request.path.rstrip("/")))
    request.session["render"]["forbase_path"] = "/"+request.path.strip("/")+"/"
    for key in local_dict:
        if not key.startswith("__") and str(key) != 'request':
            request.session["render"][key] = local_dict[key]


def flush_and_render(request, target, local_dict):
    inject_session(request, local_dict)
    return render(request, target, request.session["render"])