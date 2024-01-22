import streamlit as st
import requests

# Replicate API endpoint
REPLICATE_API_URL = "https://api.replicate.ai/graphql"

# Function to run Replicate and return the output
def run_replicate(prompt):
    api_token = "r8_T0roiahzy2mO6x5cDu2uXZIZPRhzJoZ1pgQvr"  # Replace with your Replicate API token
    headers = {"Authorization": f"Bearer {api_token}"}

    query = """
    mutation RunReplicate($model: String!, $input: JSON!) {
        run(model: $model, input: $input) {
            id
            state
            output
        }
    }
    """

    model = "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4"

    variables = {
        "model": model,
        "input": {
            "prompt": prompt,
        },
    }

    response = requests.post(REPLICATE_API_URL, json={"query": query, "variables": variables}, headers=headers)
    result = response.json()

    return result["data"]["run"]["output"]

# Streamlit app
def main():
    st.title("Replicate Streamlit App")

    prompt = st.text_area("Enter your prompt", "a vision of paradise. unreal engine")

    if st.button("Run Replicate"):
        with st.spinner("Running Replicate..."):
            output = run_replicate(prompt)
            st.success("Replicate Run Complete!")
            st.code(output, language="json")

if __name__ == "__main__":
    main()
