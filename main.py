import streamlit as st
from PIL import Image, ImageEnhance
from PIL.ExifTags import TAGS
from io import BytesIO


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

    if st.button("Extract Metadata", type="primary"):
        st.session_state.stage = "metadata"

    st.write(" ")

    if st.button("Create passport ones", type="primary"):
        st.session_state.stage = "passport"

    st.write(" ")

    if st.button("Social media ", type="primary"):
        st.session_state.stage = "social"


    st.write(" ")

    if st.button("Metadata Cleaner", type="primary"):
        st.session_state.stage = "cleaner"





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
    st.write(" ")

    if st.button("Return Home"):
        st.session_state.stage = "main"
            
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

    st.write(" ")
    st.write(" ")

    if st.button("Return Home", type="primary"):
        st.session_state.stage = "social"


def ipost():
    st.header("Instagram Post")

    image = Image.open(img)

    st.write(" ")

    w = 1080
    h = 1080

    size = image.resize((w, h))

    st.image(size, caption="Instagram Post 1080x1080")

    st.write(" ")

    if st.button("Return", type="primary"):
        st.session_state.stage = "social"


def istory():
    st.header("Instagram Story")

    st.write(" ")

    image = Image.open(img)

    w = 1080
    h = 1920

    size = image.resize((w,h))

    st.write(" ")

    st.image(size, caption="Instagram Story 1080x1920")

    st.write(" ")

    if st.button("Return", type="primary"):
        st.session_state.stage = "social"

def ythumb():
    st.header("Youtube Thumbnail")
    st.write(" ")

    image = Image.open(img)

    wi = 1280

    hi = 720

    size = image.resize((wi,hi))

    st.write(" ")

    st.image(size, caption="Youtube Thumbnail 1280x720")

    st.write(" ")

    if st.button("Return", type="primary"):
        st.session_state.stage = "social"

def link():
    image = Image.open(img)

    st.header("LinkedIn Banner")
    st.write(" ")

    wi = 1584

    hi = 396

    resize = image.resize((wi, hi))

    st.write(" ")
 
    st.image(resize, caption="Linkedin 1584x396")

    st.write(" ")

    if st.button("Return"):
        st.session_state.stage = "social"

def face():
    st.header("Facebook Banner")

    st.write(" ")

    image = Image.open(img)

    w = 820
    h = 312

    size = image.resize((w, h))

    st.image(size, caption= "Facebook 820x312")

    st.write(" ")

    if st.button("Return"):
        st.session_state.stage = "social"

def cleaner():
    st.header("Metadata")

    st.write(" ")
    st.write(" ")

    image = Image.open(img)

    st.image(image)

    st.subheader("original metadata")

    data = image.getexif()

    for tag_id, value in data.items():
        tag_name = TAGS.get(
            tag_id,
            tag_id
    

        )

        st.write(tag_name,":",int(value))

        clean = Image.new(image.mode, image.size)

        st.write(" ")

        clean.putdata(list(image.getdata()))

        st.image(clean)
        st.write(" ")

        buffer = BytesIO()

        
        clean =   clean.convert("RGB")

        clean.save(buffer, format="JPEG")

        st.download_button("Download Clean one", buffer.getvalue())

        st.write(" ")

        if st.button("Return Home", type="primary"):
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

elif st.session_state.stage == "social":
    social()
elif st.session_state.stage == "cleaner":
    cleaner()


