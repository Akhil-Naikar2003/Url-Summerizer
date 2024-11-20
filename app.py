import validators,streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
import os 
from dotenv import load_dotenv
load_dotenv()
groq_api_key=st.secrets['GROQ_API_KEY']

## sstreamlit APP
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🤖")
st.title("🤖  Summarize Text From YT or Website")
st.subheader('Summarize URL')


## Get the Groq API Key and url(YT or website)to be summarized
with st.sidebar:
    if st.button("Return to Main Menu"):
            st.markdown("[Go Back](http//:192.168.142.1:3000/T2)", unsafe_allow_html=True)

    st.markdown("**Guide**")
    st.write("""
             1.Under the title and subheader, you'll see a text input field where you can enter a URL (YouTube video or website).\n
2.In the sidebar, there’s a guide explaining how to use the app.\n
3.Enter a valid URL in the text input field for the content you want to summarize (make sure it's either a YouTube video or a website link).\n
4.Once you've entered the URL, press the "Summarize the Content from YT or Website" button.\n
5.If the Groq API key and URL are valid, the app will fetch the content and summarize it using the Groq model (Gemma-7b-It).\n
6.The summary will appear on the screen once it's ready.\n""")


generic_url=st.text_input("URL",label_visibility="collapsed")

## Gemma Model USsing Groq API
llm =ChatGroq(model="Gemma-7b-It", groq_api_key=groq_api_key)

prompt_template="""
Summerize  the following content in  words possible in decent flow:
Content:{text}

"""
prompt=PromptTemplate(template=prompt_template,input_variables=["text"])

if st.button("Summarize the Content from YT or Website"):
    ## Validate all the inputs
    if not  generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid Url. It can may be a YT video utl or website url")

    else:
        try:
            with st.spinner("Waiting..."):
                ## loading the website or yt video data
                if "youtube.com" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=False)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()

                ## Chain For Summarization
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary=chain.run(docs)

                st.success(f'🤖:{output_summary}')
        except Exception as e:
            st.exception(f"Exception:{e}")
                    