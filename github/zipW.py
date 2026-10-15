import streamlit as st
import base64

# --- メイン画面とサイドバーの両方に背景を設定する関数 ---
def set_bg_images(main_bg_file, sidebar_bg_file=None):
    # ① メイン背景の処理
    with open(main_bg_file, "rb") as f:
        main_encoded = base64.b64encode(f.read()).decode()
    
    # ② サイドバー背景の処理
    sidebar_css = ""
    if sidebar_bg_file:
        with open(sidebar_bg_file, "rb") as f:
            sidebar_encoded = base64.b64encode(f.read()).decode()
        
        sidebar_css = f"""
        [data-testid="stSidebar"] {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("data:image/jpeg;base64,{sidebar_encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        """

    # ③ CSSの適用
    st.markdown(
        f"""
        <style>
        /* メイン背景領域（黒フィルター0.6で暗く表示） */
        [data-testid="stAppViewContainer"] {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url("data:image/jpeg;base64,{main_encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        /* サイドバー背景領域 */
        {sidebar_css}
        
        /* 上部ヘッダーの透明化 */
        [data-testid="stHeader"] {{
            background-color: rgba(0, 0, 0, 0);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
set_bg_images("Whiskey1.jpg", "zunda.jpg")
st.title("ウイスキー紹介")
whiskey_list=["アランシェリーカスク","マクリームーア","カリラ12年","ダークネス8年","ソガイニ","ロッホローモンド","イーグルレア","ラッキーキャットチョコ&ルナ"]
whiskey_=[
    "アラン シェリーカスクは、ファーストフィルのシェリー樽（オロロソ・シェリーホグスヘッド）の原酒を100%使用したシングルモルトです。",
    "マクリー・ムーア（Machrie Moor）は、スコットランドのアラン島にあるロックランザ蒸溜所（旧アラン蒸溜所）が製造する、ピーテッド麦芽（フェノール値20ppm）を使用したシングルモルト・スコッチウイスキーです。アランの特徴であるフ ルーティーさに、心地よいピートスモークが調和した個性的な銘柄です。",
    "カリラ 12年は、スコットランドのアイラ島にあるカリラ蒸留所が作る、代表的なシングルモルト・スコッチウイスキーです。アルコール度数は43度、容量は700mlです。強いスモーキーさとフルーティーな甘みが調和した、アイラモルトの入門としても人気がある1本です。",
    "ダークネスシリーズのシングルモルトスコッチウイスキーです。",
    "「SOGAINI（ソガイニ）」は、広島県のサクラオブルワリーアンドディスティラリーが2025年10月1日に発売した、2000円台で買える高コスパなブレンデッドジャパニーズウイスキーです。名前は広島方言の「そんなに」に由来し、品質やこだわりを「そんなに」詰め込んだという意味が込められています。",
    "ロッホローモンド シングルグレーン ピーテッドは、大麦麦芽100%を原料にフェノール値約50ppmのヘビリーピーテッド麦芽を使用し、特殊な連続式蒸留機で蒸留した珍しいシングルグレーンウイスキーです。バーボン樽による柔らかなバニラや果実の甘みに、力強いスモーキーさが調和しています。",
    "「イーグル・レア（Eagle Rare）」は、アメリカ・ケンタッキー州のバッファロー・トレース蒸留所が造る、気品あるプレミアム・バーボン・ウイスキーです。国鳥の「白頭鷲（イーグル）」と「希少（レア）」に由来し、10年以上の長期熟成によるまろやかで複雑な味わいが特徴です。",
    "「ザ・ラッキーキャット ダブル インディヴィジュアルズ チョコ＆ルナ」は、本坊酒造がマルスウイスキーで製造するブレンデッドウイスキーのシリーズ第十二弾です。オーナーの愛猫である「チョコ」と「ルナ」の2匹をモチーフにし、甘いフレーバーと野性味ある余韻が調和した味わいが特徴です。",
]
whiskey_jpg=["Aran.jpg","macry.jpg","caol.jpg","darkness.jpg","sogaini.jpg","loch.jpg","eagle.jpg","neko.jpg"]
option=st.selectbox("ウイスキーを選んでね",whiskey_list,
                   index=None,placeholder="ウイスキーを選択"
)
whiskies=list(zip(whiskey_list,whiskey_,whiskey_jpg))
for title, description, image in whiskies:
    if title == option:
     st.subheader(title)
     st.image(image, width=300)
     st.write(description)

menu = st.sidebar.selectbox(
    "💡 ウイスキーの基礎知識",
    ["選択してください", "スモーキーとは?","フェノール値（PPM）とは?", "麦芽（モルト）とは?"]
)
if menu == "フェノール値（PPM）とは?":
    st.sidebar.write("ウイスキーのスモーキーさ（ピート感）を表す数値です。数値が大きいほど煙っぽい香りが強くなります！")

elif menu == "麦芽（モルト）とは?":
    st.sidebar.write("発芽させた大麦のこと。ウイスキーの原料となり、味のベースとなる甘みやコクを生み出します。")
elif menu == "スモーキーとは?":
    st.sidebar.write("ウイスキーのスモーキーとは、燻製（くんせい）や焚き火のような香ばしい煙の香りのことです")
#option =st.radio(
    #"ウイスキーを選んでね：",
    #("アランシェリーカスク","マクリームーア","カリラ12年","ダークネス8年","ソガイニ","ロッホローモンド","イーグルレア","ラッキーキャットチョコ&ルナ","ディメンション"),
    #index=None)
#if option =="アランシェリーカスク":
        #st.write("ここにアランシェリーカスクの説明を書く")
#elif option=="マクリームーア":
        #st.write("ここにマクリームーアの説明を書く")