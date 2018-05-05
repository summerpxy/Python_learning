import requests
import sys

KEY = "3ac0514ead0e4a7181295c4309cd69d3"


def get_weather_now(city):
    request_url = "https://free-api.heweather.com/s6/weather/now?location=" + city + "&key=" + KEY
    response = requests.get(request_url)
    if response.status_code == requests.codes.ok:
        weather = response.json()
        main_weather = weather["HeWeather6"][0]
        if main_weather["status"] == 'ok':
            update_time = main_weather["update"]['loc']
            now_tmp = main_weather["now"]["tmp"]
            now_tmp_txt = main_weather["now"]["cond_txt"]
            print(city)
            print("update time:" + update_time)
            print("current tmp:" + now_tmp)
            print(now_tmp_txt)

        else:
            print("call failed")
        print("=====================================")


def get_weather_focast(city):
    request_url = "https://free-api.heweather.com/s6/weather/forecast?location=" + city + "&key=" + KEY
    response = requests.get(request_url)
    if response.status_code == requests.codes.ok:
        weather = response.json()
        main_weather = weather["HeWeather6"][0]
        if main_weather["status"] == 'ok':
            update_time = main_weather["update"]['loc']
            forcasts = main_weather["daily_forecast"]
            print("************************************************************************************")
            for current in forcasts:
                cond_data = current["date"]
                cond_txt_d = current["cond_txt_d"]
                cond_txt_n = current["cond_txt_n"]
                tmp_max = current["tmp_max"]
                tmp_min = current["tmp_min"]
                print(
                    "date:" + cond_data + ",day:" + cond_txt_d + ",night:" + cond_txt_n + "max tmp:" + tmp_max + ",min tmp:" + tmp_min)
            print("************************************************************************************")

        else:
            print("call failed")


if __name__ == "__main__":
    print("should provider twp args: city and type!!")
    if len(sys.argv) == 2:  # 提供城市名称
        city_name = sys.argv[1]
        get_weather_now(city_name)
    elif len(sys.argv) == 3:  # 提供城市和查询种类(now/forcast)
        city_name = sys.argv[1]
        type = sys.argv[2]
        if type == 'now':
            get_weather_now(city_name)
        elif type == 'forcast':
            get_weather_focast(city_name)
        else:
            get_weather_now(city_name)
    else:
        get_weather_now("上海市")
