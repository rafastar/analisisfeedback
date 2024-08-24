import streamlit as st
import joblib
import re
from sklearn.preprocessing import LabelEncoder

# Muat model yang sudah dilatih
model = joblib.load('best_model.pkl')
vectorizer=joblib.load('best_vectorizer.pkl')
# Form input feedback
st.title("Feedback Pelayanan")
feedback = st.text_area("Masukkan feedback:")

if st.button('Prediksi Sentimen'):
    if feedback:
        olahan = vectorizer.transform([feedback])
        prediction = model.predict(olahan)
        strring = str(prediction)
        text_cleaned = re.sub(r'[\[\]\'"]', '', strring)
        st.write(f"Prediksi Sentimen untuk feedback tersebut adalah {text_cleaned}")
        if text_cleaned == 'negatif':
            st.write(f"Perlu dilakukan perbaikan terhadap pelayanan yang dilakukan")
        elif text_cleaned == 'positif':
            st.write(f"Jangan berpuas diri, pertahankan pelayanan yang telah dilakukan")
        else:
            st.write(f"Tetap lakukan Evaluasi Pelayanan, tingkatkan sektor yang diperkirakan masih jauh dari ekspektasi pelayanan")        
    else:
        st.write("Masukkan feedback terlebih dahulu.")