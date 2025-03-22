import streamlit as st
import requests


HEROKU_API_URL = "https://app-oc-stackoverflow-6669189936dc.herokuapp.com/prediction"

st.title("Test de l'application de sugggestion de tags")
st.write("Cette interface permet d'envoyer des requêtes à l'application déjà déployée sur Heroku.")

# User input
user_input = st.text_area(
    "Copiez le post StackOverFlow pour lequel vous souhaitez obtenir une suggestion de tags :",
    height=200,
    placeholder="Saisissez ou collez du texte ici..."
)

if st.button("Demander une suggestion"):
    if not user_input.strip():
        st.error("Veuillez entrer un texte avant de faire une prédiction !")
    else:
        # prepare request
        payload = {"data": user_input}

        # call API
        try:
            with st.spinner("Envoi de la requête, veuillez patienter..."):
                response = requests.post(HEROKU_API_URL, json=payload)

            # handle response
            if response.status_code == 200:
                predictions = response.json().get("predictions", [])
                if predictions:
                    st.success("Tags suggérés :")
                    for label, prob in predictions:
                        st.write(f"- **{label}** (probabilité: {int(prob*100)}%)")
                else:
                    st.warning("Aucune suggestion de tag")
            else:
                st.error(f"Error during request : {response.status_code}")
                st.write(response.text)
        except Exception as e:
            st.error("Error when connecting to the API.")
            st.write(e)