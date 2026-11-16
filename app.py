import streamlit as st
import requests

# عنوان الموقع
st.title("⚽ موقع لايف سكور الحقيقي - تونس")
st.markdown("مرحباً بك يا معلم! هنا تجد مباريات اليوم والنتائج الحية مباشرة.")

# دالة لجلب المباريات الحية (نستعملو API مجاني رياضي كمثال حي)
@st.cache_data(ttl=60) # باش يعاود يحدث البيانات كل دقيقة
def get_live_matches():
    # هنا نستعملو رابط عام مجاني لمتابعة النتائج الحية
    url = "https://www.thesportsdb.com/api/v1/json/3/eventsday.php?d=2026-11-16"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("events", [])
    except:
        return []

st.subheader("📅 مباريات اليوم الحية")

# جلب المباريات
matches = get_live_matches()

if matches:
    for match in matches:
        home_team = match.get("strHomeTeam", "فريق أ")
        away_team = match.get("strAwayTeam", "فريق ب")
        time = match.get("strTime", "توقيت غير محدد")
        score_home = match.get("intHomeScore", "0")
        score_away = match.get("intAwayScore", "0")
        
        # لو السكور فارغ نحطو 0
        if score_home is None: score_home = "0"
        if score_away is None: score_away = "0"

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"⏰ **{time}**")
        with col2:
            st.write(f"🏟️ {home_team} **VS** {away_team}")
        with col3:
            st.write(f"📊 **{score_home} - {score_away}**")
        st.divider()
else:
    st.info("لا توجد مباريات مسجلة اليوم أو جاري تحديث البيانات...")

# زر لتحديث البيانات يدوياً
if st.button("🔄 تحديث النتائج الآن"):
    st.rerun()
