# ejemplos de que colocar textos

    st.text('Fixed width text')
    st.markdown('_Markdown_') # see *
    st.caption('Balloons. Hundreds of them...')
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.write('Most objects') # df, err, func, keras!
    st.write(['st', 'is <', 3]) # see *
    
        
    # ejemplos de Lay out
    st.form('my_form_identifier')
    #st.form_submit_button('Submit to me')
    st.container()
    # st.columns(2)
    # col1, col2 = st.columns(2)
    # col1.subheader('Columnisation')
    st.expander('Expander')
    with st.expander('Expand'):
         st.write('Juicy deets')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")
    # ejemplos de mostrar datos
    st.dataframe(data)
    st.table(data.iloc[0:10])
    st.json({'foo':'bar','fu':'ba'})
    st.metric(label="Temp", value="273 K", delta="1.2 K")
    data2 = data[["x1"]]
    data3 = data[["x1","y1","z1"]]
    st.dataframe(data2)
    # Ejemplos Display charts
    st.line_chart(data2)
    st.area_chart(data2)
    st.bar_chart(data2)
    #st.pyplot(fig)
    st.altair_chart(data2)
    
    st.vega_lite_chart(data3, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'x1', 'type': 'quantitative'},
        'y': {'field': 'y1', 'type': 'quantitative'},
        'size': {'field': 'z1', 'type': 'quantitative'},
        'color': {'field': 'z1', 'type': 'quantitative'},
    },
    })
    #     # Input widgets
    st.title("trabajando con boton")
    result = st.button("Pulsar aqui")
    st.write(result)
    if result:
        st.write(":smile:")
        
    st.title("trabajando con seleccion")
    page_names = ["Checkbox","Button"]
    page = st.radio("Navegar", page_names)
    st.write("**valores**", page)
    
    if page == "Checkbox":
        st.subheader("Bienvenido a checkbox page")
        st.write("bien allí :wave:")
        check = st.checkbox("pulse aquí")
        st.write('estado del check', check)
    