import streamlit as st
import pickle
import pandas as pd

teams = ['Royal Challengers Bangalore', 'Punjab Kings', 'Delhi Capitals',
       'Kolkata Knight Riders', 'Rajasthan Royals', 'Mumbai Indians',
       'Chennai Super Kings', 'Deccan Chargers', 'Pune Warriors',
       'Kochi Tuskers Kerala', 'Sunrisers Hyderabad', 'Gujarat Titans',
       'Rising Pune Supergiants']

venues = ['M. Chinnaswamy Stadium', 'Punjab Cricket Association Stadium','Arun Jaitley Stadium', 'Wankhede Stadium',
          'Eden Gardens','Sawai Mansingh Stadium','Rajiv Gandhi International Cricket Stadium','M. A. Chidambaram Stadium',
          'Dr DY Patil Sports Academy','Newlands', "St George's Park", 'Kingsmead', 'SuperSport Park','Buffalo Park',
	  'New Wanderers Stadium', 'De Beers Diamond Oval','OUTsurance Oval', 'Brabourne Stadium',
	  'Narendra Modi Stadium','Barabati Stadium', 'Vidarbha Cricket Association Stadium',
	  'Himachal Pradesh Cricket Association Stadium','Jawaharlal Nehru Stadium', 'Holkar Cricket Stadium',
	  'Subrata Roy Sahara Stadium','Shaheed Veer Narayan Singh International Stadium',
	  'JSCA International Cricket Stadium', 'Sheikh Zayed Stadium','Sharjah Cricket Stadium',
	  'Dubai International Cricket Stadium','Maharashtra Cricket Association Stadium','ACA-VDCA Stadium',
	  'Saurashtra Cricket Association Stadium', 'Green Park Stadium','Sheikh Zayed Cricket Stadium']

model = pickle.load(open('model.pkl','rb'))
st.title('IPL Win % Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

Venue = st.selectbox('Select Stadium',sorted(venues))

target = st.number_input('Target', step =0)

col_3,col_4,col_5,col_6, col_7 = st.columns(5)

with col_3:
    current_score = st.number_input('Current Score')
with col_4:
    overs = st.number_input('Overs done(works for over>5)', step = 0)
with col_5:
    ball = st.number_input('Ball of the over', step =0)
with col_6:
    wickets = st.number_input('Wickets out', step =0)

if st.button('Predict Probability'):
    runs_left = target - current_score
    balls = (overs*6 + ball)
    crr = current_score/(overs + (ball/6))
    rrr = (runs_left)/((126-balls)/6)

    input_df = pd.DataFrame({'venue':[Venue],'batting_team':[batting_team],'bowling_team':[bowling_team],'First innings score':[target],'crr':[crr],'rrr':[rrr],'wickets':[wickets],'balls':[balls]})

    result = model.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")

