import requests
import flet as ft

# YahooAPIのエンドポイントとクライアントID
endpoint = "https://map.yahooapis.jp/weather/V1/place"
client_id = "dj00aiZpPWJtdXY5bjhWeVVqUCZzPWNvbnN1bWVyc2VjcmV0Jng9NDM-"

def get_weather():
    # パラメータの設定
    params = {
        'appid': client_id,
        'coordinates': '139.732293,35.663613',  # 東京の座標例
        'output': 'json'
    }

    # リクエストを送信
    response = requests.get(endpoint, params=params)

    # レスポンスの確認
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main(page: ft.Page):
    page.title = "東京天気情報"
    
    weather_data = get_weather()
    
    if weather_data:
        weather = weather_data.get('Feature', [{}])[0].get('Property', {}).get('WeatherList', {}).get('Weather', [{}])[0].get('Rainfall', 0)
        if weather > 0:
            weather_info = ft.Row([
                ft.Text("天気情報: 雨"),
                ft.Icon(name=ft.icons.UMBRELLA)  # 雨のアイコンを表示
            ])
        else:
            weather_info = ft.Row([
                ft.Text("天気情報: 晴れ"),
                ft.Icon(name=ft.icons.WB_SUNNY)  # 晴れのアイコンを表示
            ])
    else:
        weather_info = ft.Text("天気情報の取得に失敗しました。")
    
    page.add(weather_info)

ft.app(target=main)