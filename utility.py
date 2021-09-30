import json

defaultOptions = {
    "backgroundColor": "rgba(171, 184, 195, 1)",
    "code": "",
    "dropShadow": True,
    "dropShadowBlurRadius": "68px",
    "dropShadowOffsetY": "20px",
    "exportSize": "2x",
    "fontFamily": "Hack",
    "firstLineNumber": 1,
    "fontSize": "14px",
    "language": "auto",
    "lineNumbers": False,
    "paddingHorizontal": "56px",
    "paddingVertical": "56px",
    "squaredImage": False,
    "theme": "seti",
    "watermark": False,
    "widthAdjustment": True,
    "windowControls": True,
    "windowTheme": None,
}

optionToQueryParam = {
    "backgroundColor": "bg",
    "code": "code",
    "dropShadow": "ds",
    "dropShadowBlurRadius": "dsblur",
    "dropShadowOffsetY": "dsyoff",
    "exportSize": "es",
    "fontFamily": "fm",
    "firstLineNumber": "fl",
    "fontSize": "fs",
    "language": "l",
    "lineNumbers": "ln",
    "paddingHorizontal": "ph",
    "paddingVertical": "pv",
    "squaredImage": "si",
    "theme": "t",
    "watermark": "wm",
    "widthAdjustment": "wa",
    "windowControls": "wc",
    "windowTheme": "wt",
}

ignoredOptions = [
    # Can't pass these as URL (So no support now)
    "backgroundImage",
    "backgroundImageSelection",
    "backgroundMode",
    "squaredImage",
    "hiddenCharacters",
    "name",
    "lineHeight",
    "loading",
    "icon",
    "isVisible",
    "selectedLines",
]


def validateBody(body_):
    validatedBody = {}
    if not body_['code']:
        raise Exception("code is required for creating carbon")

    for option in body_:
        if option in ignoredOptions:
            print(f"Unsupported option: {option} found. Ignoring!")
            continue
        if (not (option in defaultOptions)):
            continue
            print(f"Unexpected option: {option} found. Ignoring!")
            #raise Exception(f"Unexpected option: {option}")
        validatedBody[option] = body_[option]
    return validatedBody


def createURLString(validatedBody):
    base_url = "https://carbon.now.sh/"
    first = True
    url = ""
    try:
        if validatedBody['backgroundColor'].startswith('#') or checkHex(validatedBody['backgroundColor'].upper()) == True:
            validatedBody['backgroundColor'] = hex2rgb(
                validatedBody['backgroundColor'])
    except KeyError:
        pass
    for option in validatedBody:
        if first:
            first = False
            url = base_url + \
                f"?{optionToQueryParam[option]}={validatedBody[option]}"
        else:
            url = url + \
                f"&{optionToQueryParam[option]}={validatedBody[option]}"
    return url


def hex2rgb(h):
    h = h.lstrip('#')
    return ('rgb'+str(tuple(int(h[i:i+2], 16) for i in (0, 2, 4))))

def checkHex(s):
    for ch in s:
        if ((ch < '0' or ch > '9') and (ch < 'A' or ch > 'F')):  
            return False
    return True
