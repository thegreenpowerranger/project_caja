import streamlit as st
import db

def write_guestbook():
    st.title("Digitals Gäschtebuäch :woman-raising-hand: :man-raising-hand:")
    st.write("""
        Erzähle etwas von deinen Highlights:
        - beste oder empfehlenswerte Restaurants oder Bars
        - lässige Trips und Routen
        - tolle Strände oder Plätze
        - wunderschöne Ausflugsorte
        - oder was du sonst gerne loswerden möchtest!
        """)
    entries = db.get_entries()

    name = st.text_input("Name")
    message = st.text_area("Message")
    if st.button("Vorschau"):
        st.write(message)
        if st.button("Abschickä"):
            db.add_entry(name, message)
            entries = db.get_entries()  # Refresh entries after adding a new one
            st.success("Your entry has been added!")
    st.header("All Entries")
    if not entries:
        st.info("There are no entries yet.")
    else:
        for entry in entries:
            st.markdown(f"<p><b>{entry['name']}:</b> {entry['message']} ({str(entry['created_at'])})</p>", unsafe_allow_html=True)            
            st.write('---')

def write_admin():

    st.title("Guestbook Admin Panel")
    
    # Prompt the user for the admin password
    password = st.text_input("Enter the admin password:", type="password")
    
    entries = []
    # Check if the password is correct
    if password == "9999":
        st.header("Guestbook Entries")
        entries = db.get_entries()

    # Display all entries with a checkbox for each one
    delete_ids = []
    for entry in entries:
        if st.checkbox(f"{entry['id']}: {entry['name']}: {entry['message']} ({str(entry['created_at'])})"):
            delete_ids.append(entry['id'])

    if delete_ids:
        if st.button('Are you sure to delete this comment?'):
            db.delete_entries(delete_ids)
            st.success("Selected entries have been deleted.")
        else:
            st.write('Nothing done')
    elif entries:
        st.info("There are no entries to delete.")

    if not entries:
        st.info("There are no entries yet.")
        
    # Prompt the user to enter the password if there are no entries yet
    if not entries and password != "":
        st.warning("Incorrect password. Please try again.")


# App
st.set_page_config(page_title="Guestbook App", page_icon=":book:", layout="centered",initial_sidebar_state='collapsed')

menu = ["Guestbook", "Admin Panel"]
choice = st.sidebar.selectbox("Select a page", menu)

st.image('Bildschirm­foto 2023-04-17 um 12.34.02 PM.png')

if choice == "Guestbook":
    write_guestbook()
else:
    write_admin()



