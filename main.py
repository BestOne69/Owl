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

    st.write(" ")

    if st.button("Create passport ones"):
        st.session_state.stage = "passport"






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

    st.write("DPI : " ,dpi)

    data = image.getexif()

    for tag_id, value in data.items():
        tag_name = TAGS.get(
            tag_id ,
            tag_id
        )

        st.write(tag_name,":", str(value))
    
    st.write(" ")
    st.write(" ")

    if st.button("Return home"):
        st.session_state.stage = "main"

        



def passport():
    st.header("Passport Photos")

    st.write(" ")

    image = Image.open(img)



    width = 413
    height = 531

    passpor = image.resize((width, height))


    st.image(passpor)

    st.write(" ")

    copies = st.slider("Number of Copies : ", 1, 8, 20)

    sheet = Image.new("RGB", (1200,1800), "white")

    x = 50

    y = 50

    for i in range(copies):
        sheet.paste(passpor, (x,y))

        x += passpor.width + 20
        
        if x + passpor.width > 1200:
            x = 50

            y += passpor.height + 20

    
    st.image(sheet)
            
def social():
    st.header("Social Media Resizer")

    st.write(" ")
    st.write(" ")

    if st.button("1. Instagram Post"):
        st.session_state.stage = "ipost"

    st.write(" ")

    if st.button("2. Instagram Story"):
        st.session_state.stage = "istory"
    st.write(" ")

    if st.button("3. Youtube Thumb"):

        st.session_state.stage = "ythumb"

    st.write(" ")

    if st.button("4. LinkedIn"):
        st.session_state.stage = "link"

    st.write(" ")
    if st.button("5. Facebook Banner"):
        st.session_state.stage = "face"


def ipost():
    st.header("Instagram Post")

    image = Image.open(img)

    st.write(" ")

    w = 1080
    h = 1080

    size = image.resize((w, h))

    st.image(size)

    st.write(" ")

    if st.button("Return home"):
        st.session_state.stage = "main"


def istory():
    st.header("Instagram Story")

    st.write(" ")

    image = Image.open(img)

    w = 1080
    h = 1920

    size = image.resize((w,h))

    st.write(" ")

    st.image(size)

    st.write(" ")

    if st.button("Return home"):
        st.session_state.stage = "main"

def ythumb():
    st.header("Youtube Thumbnail")
    st.write(" ")

    image = Image.open(img)

    wi = 1280

    hi = 720

    size = image.resize((wi,hi))

    st.write(" ")

    st.image(size)

    st.write(" ")

    if st.button("Return Home"):
        st.session_state.stage = "main"

def link():
    image = Image.open(img)

    st.header("LinkedIn Banner")
    st.write(" ")

    wi = 1584

    hi = 396

    resize = image.resize((wi, hi))

    st.write(" ")

    st.image(resize)

    st.write(" ")

    if st.button("Return Home"):
        st.session_state.stage = "main"

def face():
    st.header("Facebook Banner")

    st.write(" ")

    image = Image.open(img)

    w = 820
    h = 312

    size = image.resize((w, h))

    st.image(size)

    st.write(" ")

    if st.button("Return Home"):
        st.session_state.stage = "main"




if st.session_state.stage == "main":
    main()

elif st.session_state.stage == "metadata":
    metadata()

elif st.session_state.stage == "passport":
    passport()

elif st.session_state.stage == "ipost":
    ipost()

elif st.session_state.stage == "istory":
    istory()

elif st.session_state.stage == "ythumb":
    ythumb()

elif st.session_state.stage== "face":
    face()

elif st.session_state.stage == "link":
    link()



