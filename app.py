# app.py
import streamlit as st
from dotenv import load_dotenv
from src.chains import get_restaurant_name_chain, get_menu_idea_chain
from src.utils import load_cuisines, load_styles

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Restaurant Name & Menu Generator", layout="centered")
st.title("🍽️ Restaurant Name & Menu Generator")
st.markdown("Use the power of LLMs to generate creative restaurant names and menu ideas!")

# --- Load data for dropdowns ---
cuisines = load_cuisines()
styles = load_styles()

if not cuisines or not styles:
    st.error("Error loading cuisines or styles data. Please check 'data/' directory.")
    st.stop()

# --- Input Form ---
with st.form("generator_form"):
    st.header("Generate a Restaurant Name")
    selected_cuisine = st.selectbox("Select Cuisine:", options=[""] + cuisines, index=0)
    selected_style = st.selectbox("Select Style:", options=[""] + styles, index=0)

    name_submit_button = st.form_submit_button("Generate Name")

# --- Restaurant Name Generation ---
restaurant_name = None
if name_submit_button:
    if not selected_cuisine or not selected_style:
        st.warning("Please select both a cuisine and a style to generate a name.")
    else:
        with st.spinner("Generating restaurant name..."):
            name_chain = get_restaurant_name_chain()
            try:
                response = name_chain.invoke({"cuisine": selected_cuisine, "style": selected_style})
                restaurant_name = response.strip() # Corrected: response is a string
                st.success(f"**Suggested Restaurant Name:** {restaurant_name}")
                st.session_state["generated_name"] = restaurant_name
            except Exception as e:
                st.error(f"Error generating name. See details below and console output.")
                import traceback
                tb_str = traceback.format_exc()
                st.text_area("Detailed Error Information (Name Generation):", f"{type(e).__name__}: {str(e)}\n\n{tb_str}", height=300)
                print("--- Full Traceback for Name Generation Error ---")
                traceback.print_exc()
                print("--- End of Traceback ---")

# --- Menu Idea Generation (only if a name was generated) ---
if "generated_name" in st.session_state and st.session_state["generated_name"]:
    st.header("Generate Menu Ideas for Your Restaurant")
    st.markdown(f"Using generated restaurant name: **{st.session_state['generated_name']}**")

    # Offer an option to use the generated name or input a custom one
    use_generated_name = st.checkbox("Use the generated name", value=True, key="use_generated_name_checkbox")
    
    if not use_generated_name:
        custom_restaurant_name = st.text_input("Or enter a custom restaurant name:", key="custom_name_input")
        restaurant_name_for_menu = custom_restaurant_name if custom_restaurant_name else st.session_state["generated_name"]
    else:
        restaurant_name_for_menu = st.session_state["generated_name"]

    menu_cuisine = st.selectbox("Select Cuisine for Menu (can be different):", options=[""] + cuisines, index=cuisines.index(selected_cuisine) if selected_cuisine in cuisines else 0)

    menu_submit_button = st.button("Generate Menu Ideas")

    if menu_submit_button:
        if not restaurant_name_for_menu or not menu_cuisine:
            st.warning("Please provide a restaurant name and select a cuisine for menu generation.")
        else:
            with st.spinner("Generating menu ideas..."):
                menu_chain = get_menu_idea_chain()
                try:
                    response = menu_chain.invoke({"restaurant_name": restaurant_name_for_menu, "cuisine": menu_cuisine})
                    menu_ideas = response.strip() # Corrected: response is a string
                    st.subheader("Suggested Menu Items:")
                    st.markdown(menu_ideas)
                except Exception as e:
                    st.error(f"Error generating menu ideas. See details below and console output.")
                    import traceback
                    tb_str = traceback.format_exc()
                    st.text_area("Detailed Error Information (Menu Generation):", f"{type(e).__name__}: {str(e)}\n\n{tb_str}", height=300)
                    print("--- Full Traceback for Menu Idea Generation Error ---")
                    traceback.print_exc()
                    print("--- End of Traceback ---")
else:
    st.info("Generate a restaurant name first to get menu ideas!")

st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit, Langchain, and Gemini API.")