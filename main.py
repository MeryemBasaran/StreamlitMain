import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt







background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("data:image/jpeg;base64,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");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)



input_style = """
<style>
input[type="text"] {
    background-color: transparent;
    color: #a19eae;  // This changes the text color inside the input box
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}
</style>A
"""
st.markdown(input_style, unsafe_allow_html=True)
st.snow()

st.title('Meryem Başaran')
st.header('BONUS ASSIGNMENTS')
st.subheader('*DETERMINING THE FORCE TYPE*')
st.text('This is a website that gives you support reactions and moment diagrams')
st.text('in line with some information you give after choosing your load type.')
st.success('# CHOOSE YOUR LOAD TYPE')
select= st.selectbox('Your Load Type', ['Point', 'Distributed'])
st.write('You selected:', select)
if select == 'Point':
    st.write("Your load is point")

    st.image('pointload.jpg', caption=('THIS IS THE SYSTEM YOU HAVE CHOSEN'))
    F = st.slider('What is your force value ', 0,100, step = 1)
    st.write("Force :" , F)

    L = st.slider('What is your length value?', 1,100 , step = 1)
    st.write("Length :" , L)

    X = st.slider('What is your force distance?', 0,100, step = 1)
    st.write("Force Distance :" , X)

    x = int(X)
    l = int(L)
    f = int(F)

    a = l - x
    b = f * a
    Ay = b / l
    st.write('Your support reaction in A point   Ay:', Ay)

    By = f * x / l
    st.write('Your support reaction in B point   By:', By)

    Mmax = f * a * x / l
    st.write('Your Maximum Moment Value   Mmax:', Mmax)

    graphl = [0, Mmax, 0]
    graphll = [0, x, l]
    xpoints = graphll
    ypoints = graphl

    fig=plt.figure()


    plt.plot(xpoints, ypoints, color='C5')
    st.write(fig)

elif select == 'Distributed':
    st.write("your load is distributed")


    st.image("distributedload.jpg", caption=('THIS IS THE SYSTEM YOU HAVE CHOSEN'))

    W = st.slider("What is your distributed load value?", 1,100 , step= 1)
    st.write("Distributed load :" , W)

    S = st.slider("What is your distributed load length ", 0,100 , step= 1)
    st.write("distributed load length :" , S)

    L = st.slider("What is your length value?", 1,100 , step= 1)
    st.write("Length :", L)

    X = st.slider("What is your distributed load length from support A distance?", 0,100 , step=1)
    st.write("Force Distance :", X)

    x = int(X)
    l = int(L)
    s = int(S)
    w = int(W)

    z = l - x - s
    d = l - x
    Ay = w * s * (2 * z + s) / (2 * l)

    By = w * s * (2 * x + s) / (2 * l)

    st.write('Your support reaction in A point   Ay:', Ay)
    st.write('Your support reaction in B point   By:', By)

    Mmax1 = (Ay * (x + (Ay / (2 * w))))
    st.write('Your Maximum Moment Value   Mmax:', Mmax1)
    kl = 1
    while kl < l + 2:
        k = np.arange(kl)

        print(k)
        print(kl)
        kl = kl + 1

    i = 0
    Mx = []
    while i < l + 1:
        if (k[i] <= x):
            Mx.append(Ay * k[i])
            print(Mx)
            print(k[i])

        elif (k[i] > x) and (k[i] <= (x + s)):
            Mx.append(((Ay * k[i])) - ((w / 2) * ((k[i] - x) ** 2)))
            print(Mx)
            print(k[i])

        elif (k[i] > (x + s)):
            Mx.append(By * (l - k[i]))
            print(Mx)
            print(k[i])

        i = i + 1

    print(k)

    st.write('The moment values in your system per meter are as follows: ', Mx)

    fig1 = plt.figure()

    xpoints = k
    ypoints = Mx
    plt.plot(k, Mx)
    plt.xlim(min(xpoints), max(xpoints))
    plt.ylim(min(ypoints), max(ypoints))

    st.write(fig1)