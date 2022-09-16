import streamlit as st

def intro():
    import streamlit as st

    st.write("# Accidents routiers en France ")
    #st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        L’objectif de ce projet est d’essayer de prédire la gravité des accidents routiers en France.
        Les prédictions seront basées sur les données historiques.


        ### Data

        - Bases de données annuelles des accidents corporels de la circulation routière [data.gouv.fr](https://www.data.gouv.fr/en/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/)
        - test1
        - test2
        ### titre 2

    """
    )

def Dataviz():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk
    import pandas as pd
    import numpy as np

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    st.markdown(
        """ 
        
        hsdjqflhgjlqshgdjkqsghjskqghqskjlmghkqls


    """)


    HEXAGON_LAYER_DATA = ('https://raw.githubusercontent.com/GuillaumeGrrd/Projet_Accident/master/data/map/Map.csv')
    #HEXAGON_LAYER_DATA = 'data/map/Map.csv'

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=46.0,
            longitude=2,
            zoom=5,
            pitch=35,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                HEXAGON_LAYER_DATA,
                get_position= ['long', 'lat'],
                auto_highlight=True,
                radius=800,
                elevation_scale=70,
                pickable=True,
                elevation_range=[0, 3000],
                extruded=True,
                coverage=1,
            ),           
        ],
    ))


def Modelisation():
    import streamlit as st
    import time
    import numpy as np

    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write(
        """
        This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!
"""
    )

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")



def Proto():
    import streamlit as st
    import pandas as pd
    import altair as alt

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    st.write(
        """
        This demo shows how to use `st.write` to visualize Pandas DataFrames.

(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
"""
    )

    @st.cache
    def get_UN_data():
        AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
        return df.set_index("Region")

    try:
        df = get_UN_data()
        countries = st.multiselect(
            "Choose countries", list(df.index), ["China", "United States of America"]
        )
        if not countries:
            st.error("Please select at least one country.")
        else:
            data = df.loc[countries]
            data /= 1000000.0
            st.write("### Gross Agricultural Production ($B)", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="year:T",
                    y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                    color="Region:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

page_names_to_funcs = {
    "Présentation du projet": intro,
    "Data Visualisation": Dataviz,
    "Modélisation": Modelisation,
    "Prototype": Proto
}

demo_name = st.sidebar.selectbox("Navigation", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()