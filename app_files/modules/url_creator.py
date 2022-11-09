def get_url(location):
    """makes the url for api requests"""
    my_key = "V7CK4U8J5FYGWDCU7UBCAE4SU"
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    days = f"/next7days?unitGroup=metric&include=datetime%2Cname%2Caddress%2Ctempmax%2Ctempmin%2Ctemp%2Chumidity%2Cicon&include=days&key={my_key}&contentType=json"
    return f"{base_url}{location}{days}"