import streamlit as st

st.set_page_config(page_title="AI Code Translator", page_icon="🌐", layout="centered")

st.title("🌐 Multi-Language AI Code Translator")
st.write("Translate programming logic snippets seamlessly!")

source_lang = st.selectbox("From Language", ["Python", "JavaScript"])
target_lang = st.selectbox("To Language", ["C++", "Java"])

source_code = st.text_area("Enter Code Snippet:", height=150)

if st.button("Translate Code"):
    if source_code:
        st.subheader(f"🔄 Translated Code ({target_lang})")
        
        # Simulated translation translation logic
        translated = source_code.replace("print(", "std::cout << ").replace("def ", "// function in ").replace(";", "")
        
        if target_lang == "C++":
            st.code(f"// Translated to C++\n#iostream\nusing namespace std;\n\nint main() {{\n    {translated};\n    return 0;\n}}", language="cpp")
        else:
            st.code(f"// Translated to Java\npublic class Main {{\n    public static void main(String[] args) {{\n        {translated};\n    }}\n}}", language="java")
    else:
        st.warning("Please enter some code to translate.")
