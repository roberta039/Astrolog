import os
import requests

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def save_chart(birth_data, chart):
    url = f"{SUPABASE_URL}/rest/v1/birth_charts"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal",
    }
    payload = {"birth_data": birth_data, "chart": chart}
    try:
        requests.post(url, headers=headers, json=payload, timeout=10)
    except Exception as e:
        # log but don't raise to avoid breaking API for users
        print('Failed to save to Supabase:', e)

def get_chart(user_id):
    url = f"{SUPABASE_URL}/rest/v1/birth_charts?user_id=eq.{user_id}"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
    }
    r = requests.get(url, headers=headers, timeout=10)
    try:
        return r.json()
    except Exception:
        return []
