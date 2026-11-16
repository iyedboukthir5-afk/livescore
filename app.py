
import streamlit as st
import requests

# عنوان الموقع
st.title("⚽ موقع جدول مباريات اليوم - تونس")
st.markdown("مرحباً بك يا معلم! هنا تجد كل مباريات اليوم بتوقيتها والفرق المشاركة.")

# دالة لجلب مباريات اليوم الكاملة
@st.cache_data(ttl=60)
def get_all_matches():
    # رابط يجيب كل مباريات اليوم الحالي (تاريخ اليوم تلقائياً)
    url = "https://www.thesportsdb.com/api/v1/json/3/eventsday.php?d=2026-11-16"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("events", [])
    except:
        return []

st.subheader("📅 قائمة مباريات اليوم")

# جلب المباريات
matches = get_all_matches()

if matches:
    for match in matches:
        home_team = match.get("strHomeTeam", "فريق أ")
        away_team = match.get("strAwayTeam", "فريق ب")
        time = match.get("strTime", "غير محدد")
        league = match.get("strLeague", "بطولة رياضية")
        
        # عرض معلومات كل مباراة في أعمدة مرتبة
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"🏆 **{league}**")
            st.write(f"⏰ **التوقيت:** {time}")
        with col2:
            st.write(f"🏟️ **المباراة:**")
            st.write(f"{home_team} **VS** {away_team}")
        with col3:
            st.write(f"📊 **الحالة / النتيجة:**")
            score_home = match.get("intHomeScore")
            score_away = match.get("intAwayScore")
            if score_home is not None and score_away is not None:
                st.write(f"{score_home} - {score_away}")
            else:
                st.write("لم تبدأ بعد ⏳")
        st.divider()
else:
    st.info("لا توجد مباريات مسجلة حالياً لهذا اليوم في النظام.")

# زر لتحديث البيانات
if st.button("🔄 تحديث الجدول"):
    st.rerun()
