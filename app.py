import streamlit as st
import anthropic

def main():
    st.set_page_config(page_title="Love Poet")
    st.header("Love Poet💕")
    st.text("Made with ❤ For MenteE ☺")
    st.divider()
    
    user_question = st.text_input("Ask me to write poetry:")
    
    # Chat with GPT-3.5
    if user_question:
        # Call GPT-3.5 for fine-tuning
        with st.spinner("Wait a bit MenteE ☺, Poetry is on th way..."):
            client = anthropic.Anthropic()
            message = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=200,
                temperature=0.7,  
                system="Your personal love poet",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f'{user_question} (always use Urdu, if user did not specify the langauge)'
                            }
                        ]
                    }
                ]
            )

        # Display response
        st.write(f"Response: {message.content[0].text}\n")

if __name__ == "__main__":
    main()