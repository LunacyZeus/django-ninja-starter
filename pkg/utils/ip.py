def get_ip(request):
    if "HTTP_X_FORWARDED_FOR" in request.META:
        ip = request.META["HTTP_X_FORWARDED_FOR"]
        if "," in ip:
            ips = ip.split(",")
            ip = ips[0]
    else:
        ip = request.META["REMOTE_ADDR"]

    return ip
