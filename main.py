import streamlit as st
from PIL import Image, ImageEnhance
from PIL.ExifTags import TAGS


stage = "main"

if "stage" not in st.session_state:
    st.session_state.stage = "main"

st.title("Imagify 2.0")

st.write(" ")
st.write(" ")

img = st.file_uploader("Uplaod File", type=["png", "jpg", "jpeg"])

def main():
    if img is not None:
        myimage = Image.open(img)

        st.write(" ")

        st.write(" ")

        st.image(myimage, width=400)

    st.write(" ")
    st.write(" ")

    if st.button("Extract Metadata"):
        st.session_state.stage = "metadata"






def metadata():
    st.header("Metadata")
    st.write(" ")

    st.write(" ")

    image = Image.open(img)

    st.write("Filename", img.name)

    st.write("Format", image.format)
    st.write("Width", image.width)

    st.write("height", image.height)

    st.write("Mode Colour : ", image.mode)

    st.write("file size", img.size)

    mp = image.width * image.height /1_000_000

    st.write("Megapixels", mp)

    st.write(" ")

    dpi = image.info.get("dpi")

    st.write("DPI : " ,dpi:.2f())

    data = image.getexif()

    for tag_id, value in data.items():
        tag_name = TAGS.get(
            tag_id ,
            tag_id
        )

        st.write(tag_name,":", value)
    
    st.write(" ")



def passport():
    pass


if st.session_state.stage == "main":
    main()

elif st.session_state.stage == "metadata":
    metadata()


