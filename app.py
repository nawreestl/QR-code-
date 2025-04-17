import streamlit as st
import qrcode
from PIL import Image
import io

# Titre de l'application
st.title("Générateur de QR Code")

# Demander à l'utilisateur de saisir une URL ou du texte
user_input = st.text_input("Entrez le texte ou l'URL pour générer le QR code:")

# Bouton pour générer le QR code
if st.button("Générer QR Code"):
    if user_input:
        # Créer le QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(user_input)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        # Convertir l'image en bytes
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        # Afficher le QR code
        st.image(img_bytes, caption="Voici votre QR Code", use_container_width=True)

        # Option pour télécharger l'image du QR code
        img.save("QRCode.png")
        with open("QRCode.png", "rb") as file:
            st.download_button(
                label="Télécharger le QR Code",
                data=file,
                file_name="QRCode.png",
                mime="image/png"
            )
    else:
        st.error("Veuillez entrer un texte ou une URL pour générer le QR code.")
