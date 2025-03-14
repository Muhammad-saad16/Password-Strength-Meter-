import streamlit as st
import random
import string

# Function to calculate password strength
def calculate_strength(password):
    length = len(password)
    if length < 8:
        return "🔴Weak"
    elif 8 <= length < 12:
        return "🟡Moderate"
    else:
        return "🟢Strong"

# Function to generate a random password
def generate_password(length, use_numbers, use_symbols, use_uppercase):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# Streamlit UI Layout
st.set_page_config(page_title="Password Strength Meter", layout="wide")

st.sidebar.title("🔐 Password Strength Meter")

# Choose method for generating password
password_method = st.sidebar.radio(
    "Choose Password Option:",
    ('🎲 Generate Password', '✍️ Enter Password')
)

st.markdown("""
    <h1 style='text-align: center; color: #ffffff; background-color: #6c63ff; padding: 15px; border-radius: 10px;'>
        Password Strength Meter
    </h1>
""", unsafe_allow_html=True)

if password_method == '🎲 Generate Password':
    length = st.sidebar.slider('Password Length', 8, 32, 16)
    use_numbers = st.sidebar.checkbox('🔢 Include Numbers', value=True)
    use_symbols = st.sidebar.checkbox('💎 Include Symbols', value=True)
    use_uppercase = st.sidebar.checkbox('🔠 Include Uppercase Letters', value=True)

    if st.sidebar.button('🎲 Generate Password'):
        generated_password = generate_password(length, use_numbers, use_symbols, use_uppercase)
        st.success(f'🔐 Generated Password: `{generated_password}`')
        strength = calculate_strength(generated_password)
        st.info(f'💡 Password Strength: {strength}')

elif password_method == '✍️ Enter Password':
    entered_password = st.text_input('Enter your password', type='password')
    if entered_password:
        strength = calculate_strength(entered_password)
        st.info(f'💡 Password Strength: {strength}')

# Footer
st.markdown("""
    <footer style="text-align: center; padding: 20px; background-color: #6c63ff; color: white; border-radius: 15px; margin-top: 20px;">
        Made with ❤️ by Muhammad Saad | 💻 Powered by Python & Streamlit
    </footer>
""", unsafe_allow_html=True)
