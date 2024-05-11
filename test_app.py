import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('House_price_pred_ridge_cv.pkl')  # Replace with your model file path
st.image(r"C:\Users\user\Desktop\Project\House_Price_prediction\house.jpeg",caption='house image',use_column_width=True)
# Add navigation links in the sidebar
selected_page = st.sidebar.selectbox("Navigation", ['Home', 'About', 'Contact'])

# Define the Home Page
def home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

# Define the Streamlit app
def main():
    st.title('House Price Prediction App')

    # Display input fields for user input
    area = st.number_input('Area (in square feet)', value=1000)
    bedrooms = st.number_input('Number of Bedrooms', value=2)
    bathrooms = st.number_input('Number of Bathrooms', value=2)
    stories = st.number_input('Number of Stories', value=1)
    parking = st.number_input('Number of Parking Spots', value=1)
    mainroad = st.selectbox('Main Road Proximity', ['No', 'Yes'])
    guestroom = st.selectbox('Guest Room Availability', ['No', 'Yes'])
    basement = st.selectbox('Basement Availability', ['No', 'Yes'])
    hotwaterheating = st.selectbox('Hot Water Heating', ['No', 'Yes'])
    airconditioning = st.selectbox('Air Conditioning', ['No', 'Yes'])
    prefarea = st.selectbox('Preferred Area', ['No', 'Yes'])
    furnishingstatus = st.selectbox('Furnishing Status', ['Unfurnished', 'Semi-Furnished', 'Furnished'])

    # Prepare input features
    input_features = {
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'stories': stories,
        'parking': parking,
        'mainroad_no': 1 if mainroad == 'No' else 0,
        'mainroad_yes': 1 if mainroad == 'Yes' else 0,
        'guestroom_no': 1 if guestroom == 'No' else 0,
        'guestroom_yes': 1 if guestroom == 'Yes' else 0,
        'basement_no': 1 if basement == 'No' else 0,
        'basement_yes': 1 if basement == 'Yes' else 0,
        'hotwaterheating_no': 1 if hotwaterheating == 'No' else 0,
        'hotwaterheating_yes': 1 if hotwaterheating == 'Yes' else 0,
        'airconditioning_no': 1 if airconditioning == 'No' else 0,
        'airconditioning_yes': 1 if airconditioning == 'Yes' else 0,
        'prefarea_no': 1 if prefarea == 'No' else 0,
        'prefarea_yes': 1 if prefarea == 'Yes' else 0,
        'furnishingstatus_furnished': 1 if furnishingstatus == 'Furnished' else 0,
        'furnishingstatus_semi-furnished': 1 if furnishingstatus == 'Semi-Furnished' else 0,
        'furnishingstatus_unfurnished': 1 if furnishingstatus == 'Unfurnished' else 0
    }

    # # Display the selected page based on user's choice
    # if selected_page == 'Home':
    #     home()
    # elif selected_page == 'About':
    #     st.title('About Page')
    #     st.write('This is the About Page.')
    # elif selected_page == 'Contact':
    #     st.title('Contact Page')
    #     st.write('You can reach us at dukundesaint@gmail.com')

    # Prepare input as a numpy array
    input_array = np.array(list(input_features.values())).reshape(1, -1)

    # Make predictions using the loaded model
    if st.button('Predict Price'):
        prediction = model.predict(input_array)[0]
        st.success(f'Predicted Price: ${prediction:.2f}')

# Run the Streamlit app
if __name__ == '__main__':
    main()
