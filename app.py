import streamlit as st
import pickle
import pandas as pd
model = pickle.load(open('clf.pkl', 'rb'))
model2 = pickle.load(open('state_prediction.pkl', 'rb'))

st.title('NextBestState')

input_values = []
tab1, tab2 = st.tabs(['Longs&Lats', 'Prediction'])

with tab1:
    st.title('Predict The Tier!')

with tab2:
    prediction = []
    result = []
    st.title('New Prediction')
    pop_slider = float(st.slider(label='Population',
                                 min_value=10000,
                                 max_value=10000000))
    road_factor = float(st.slider(label="Road Quality",
                                  min_value=10000,
                                  max_value=1000000))
    economy = st.slider(label="Economy Index",
                        min_value=1000,
                        max_value=1000000)
    literacy_rate = st.slider(label="Literacy Rate",
                              min_value=0,
                              max_value=10)
    tier_value = st.selectbox('Tier Place you looking for?',
                              ('Top', 'Intermediate', 'Low'))

    if tier_value == 'Top':
        tier_value = 1
    elif tier_value == 'Intermediate':
        tier_value = 2
    else:
        tier_value = 3
    lst = [pop_slider, road_factor, tier_value,
           economy, literacy_rate]
    for x in lst:
        input_values.append(x)

    print(input_values)
    # st.write(input_values)

    if st.button('Predict'):
        prediction = model2.predict([input_values])
        # st.write(prediction[0])
        result = str(prediction[0]).strip()
        df = pd.read_csv('state_reading.csv')
        df['state'] = df['state'].str.replace(' ', '')
        matching_rows = df[df['state'] == f'{result}']
        st.write(matching_rows)
print(result)


# for x in df['state']:
#     if x == result and count <= 0:
#         col1, col2, col3, col4 = st.columns(4)
#         with col1:
#             st.write(df[x])
# with col2:
#     st.write(df['city'])
# with col3:
#     st.write(df['lats'])
# st.write(df['lats'])
# st.write(df[x]['longs'])
