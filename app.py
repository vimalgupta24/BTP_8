from imports import *
from Gesture_Controller import gest
st.set_page_config(
    page_title="VMGest",
    menu_items={
        'About': "Developed by - https://github.com/vimalgupta24"
    },
    page_icon="🤖",
)

st.markdown("""
	<style>
	/* This is to hide hamburger menu completely */
	/* #MainMenu {visibility: hidden;} */
	/* This is to hide Streamlit footer */
	footer {visibility: hidden;}
	ul[data-testid=main-menu-list] > li:nth-of-type(4), /* Documentation */
	ul[data-testid=main-menu-list] > li:nth-of-type(5), /* Ask a question */
	ul[data-testid=main-menu-list] > li:nth-of-type(6), /* Report a bug */
	ul[data-testid=main-menu-list] > li:nth-of-type(7), /* Streamlit for Teams */
	ul[data-testid=main-menu-list] > div:nth-of-type(2) /* 2nd divider */
		{display: none; visibility:hidden;}
	</style>
""", unsafe_allow_html=True)


st.sidebar.title("What to do :)")
app = st.sidebar.selectbox("Choose the app mode -> Use 'Run Project' for demo interaction ",
                           ["Home","Features",  "Run Project"])
if app == "Home":
    st.title('About Our Project')
    st.markdown("In the field of Human Computer Interaction (HCI), a hand gesture recognition system provides an innovative approach towards nonverbal communication with your machines. The objective is to overcome the use of direct contact with the devices and make it easier to interact with computer. Gesture Controlled Virtual Mouse makes human computer interaction simple by making use of Hand Gestures.Such methods can also be used with voice controlled systems to make it more robust and useable. The computer requires almost no direct contact. All i/o operations can be virtually controlled by using static and dynamic hand gestures. This project makes use of the state-of-art Machine Learning and Computer Vision algorithms to recognize hand gestures, which works smoothly without any additional hardware requirements. It leverages models such as CNN implemented by MediaPipe running on top of pybind11. It consists of two modules: One which works direct on hands by making use of MediaPipe Hand detection, and other which makes use of Gloves of any uniform color. Currently it works on Windows platform.")
    st.divider()
    st.markdown('**:blue[Also Goal of this project is to provided the gesture recognition with an interface to interact with the project much easily!!]**')
elif app == "Run Project":
    st.balloons()
    ctx = webrtc_streamer(
        key="example",
        video_processor_factory=gest(),
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={
            "video": True,
            "audio": False
        }, async_processing=True, video_frame_callback=gest()
    )
    # gest()
    # subprocess.call(['python', 'Gesture_Controller.py'])
elif app== "Features":
    features=[" Easy to use Interface"," Gesture Recognition", " Neutral Gesture"," Move Cursor"," Left Click"," Right Click"," Double Click"," Scrolling"," Drag and Drop"," Multiple Item Selection", " Volume Control"," Brightness Control"]
    st.header(':red[Feautures of this project are:]')
    for item in features:
        st.text("->"+item)
