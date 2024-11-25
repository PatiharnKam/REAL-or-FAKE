import streamlit as st
from streamlit_option_menu import option_menu
from Home import show_home
from About import show_about
from Upload import show_upload
from Visual import show_visual

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Visual", "Upload", "About us"],
        icons=["house", "eye", "upload", "info-circle"], 
        menu_icon="cast",
        default_index=0 
    )


def switch_case(option):
    if option == "Home":
        show_home()
    elif option == "Visual":
        show_visual()
    elif option == "Upload":
        show_upload()
    elif option == "About us":
        show_about()
    else:
        st.error("Page not found!")

def main():
    switch_case(selected)

if __name__ == "__main__":
    main()
