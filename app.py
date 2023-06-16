import streamlit as st

from widget.band_list import get_band_list
from widget.band_detail import get_band_detail

st.title("🎸BAND")
#st.image("img/day6-modified.png")

def make_band(name, img, desc, music, link):
    return dict(name=name, img=img, desc=desc, music=music, link=link)
group1 = make_band(
    "소란", "img/soran-modified.png",
    "**함께 하는 매 순간이 특별한 기념일, 번뜩이는 위트와 따뜻한 위로 소란**. "\
    "멤버는 고영배(리더, 보컬, 키보드, 어쿠스틱 기타)"\
    "이태욱(기타, 코러스)"\
    "서면호(베이스 기타, 코러스)"\
    "편유일(드럼)이 있다.",
    "img/soran_m2.jpg",
    "https://youtu.be/oi1IGsVOnTs",
)
group2 = make_band(
    "데이식스", "img/day6-modified.png",
    "**2015년 9월 7일에 데뷔한 JYP엔터테인먼트 소속 4인조 밴드. JYP에서 밴드로 데뷔한 최초의 아티스트**, "\
    "멤버는 성진(리더, 보컬, 기타), Young K(보컬, 랩, 베이스), 원필(보컬, 키보드, 신디사이저), 도운(드럼, 보컬)으로, 멤버 전원이 악기와 보컬을 맡고 있다는 점이 특징이다.",
    "img/day6_m2.jpg",
    "https://youtu.be/vnS_jn2uibs",
)
group3 = make_band(
    "루시", "img/lucy-modified.png",
    "**미스틱스토리에서 선보이는 첫 밴드이자 4인조 보이밴드. 2019년 밴드 오디션 프로그램 JTBC 슈퍼밴드에서 처음 결성되어 준우승을 차지하였다.** "\
    "멤버는 신예찬(리더, 바이올린), 최상엽(보컬, 기타), 조원상(베이스, 프로듀싱), 신광일(드럼, 보컬)이 있다.",
    "img/lucy_m.jpg",
    "https://youtu.be/wFJxzoljf10",
)
group4 = make_band(
    "페퍼톤스", "img/peppertones-modified.png",
    "**우울증을 위한 뉴테라피 2인조 밴드**, "\
    "신재평(기타)과 이장원(베이스)으로 이루어진 남성 2인조 밴드이자 프로듀싱 유닛이다. 2003년 의기투합해 페퍼톤스를 결성, 2004년에 EP앨범 《A PREVIEW》로 데뷔했다",
    "img/p_m.jpg",
    "https://youtu.be/U6dTSMCqlp4",
)
group5 = make_band(
    "터치드", "img/touched-modified.png",
    "**당신의 마음을 감동시킬 밴드 터치드(Touched)**, "\
    "강한 에너지의 전통 록 사운드, 때로는 미디엄 템포의 감성적이고 섬세한 모던록 사운드를 선보이고 있다."\
    "멤버 모두 서울예술대학교 실용음악과 동문 출신이다."\
    "멤버는 윤민(보컬, 기타), 김승빈(리더, 드럼), 존비킴(베이스), 디온(리드깉타), 채도현(키보드)이 있다.",
    "img/t_M.jpg",
    "https://youtu.be/ywQXK0a9-DM",
)
groups = [group1, group2, group3, group4, group5]

if 'detail' not in st.session_state:  # key를 확인해서
    st.session_state['detail'] = ""  # 초기값
    st.session_state['music'] = ""  # 초기값
    st.session_state['link'] = ""  # 초기값

# 밴드 리스트
get_band_list(groups)

# 밴드 상세보기
if st.session_state['detail']:  # 초기값의 빈 문자열
    get_band_detail()  # 처음에는 실행하지 않고... 클릭했을 때 반응해서 그려지게

