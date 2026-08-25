import os
import json
import re

import streamlit as st
from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error(
        "GEMINI_API_KEY is missing. Please create a .env file and add your Gemini API key."
    )
    st.stop()

client = genai.Client(api_key=API_KEY)


st.set_page_config(
    page_title="Intelligent Code Reviewer & Explainer",
    page_icon="🔍",
    layout="wide"
)


st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .subtitle {
            font-size: 18px;
            color: #777777;
            margin-bottom: 25px;
        }

        .section-title {
            font-size: 26px;
            font-weight: 650;
            margin-top: 20px;
            margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="main-title">🔍 Intelligent Code Reviewer & Explainer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze code, detect bugs, understand logic, and generate optimized code using Generative AI.</div>',
    unsafe_allow_html=True
)


with st.sidebar:
    st.header("⚙️ Project Information")

    st.write(
        """
        This AI-powered developer utility provides:

        - 🐞 Bug detection
        - 🧠 Code explanation
        - 💡 Improvement suggestions
        - ⚡ Optimized code
        - 📊 Code summary
        - 📋 Structured analysis
        """
    )

    st.divider()

    st.subheader("📁 Supported Files")

    st.write("🐍 Python: `.py`")
    st.write("🟨 JavaScript: `.js`")
    st.write("☕ Java: `.java`")

    st.divider()

    st.caption("DecodeLabs Generative AI Internship")
    st.caption("Project 4")


def get_language(extension):
    languages = {
        ".py": "python",
        ".js": "javascript",
        ".java": "java"
    }

    return languages.get(extension, "text")


def extract_json(response_text):
    response_text = response_text.strip()

    if response_text.startswith("```"):
        response_text = re.sub(
            r"^```(?:json)?\s*",
            "",
            response_text,
            flags=re.IGNORECASE
        )

        response_text = re.sub(
            r"\s*```$",
            "",
            response_text
        )

    try:
        return json.loads(response_text)

    except json.JSONDecodeError:
        start = response_text.find("{")
        end = response_text.rfind("}")

        if start != -1 and end != -1 and end > start:
            json_text = response_text[start:end + 1]
            return json.loads(json_text)

        raise


def build_system_instruction():
    return """
You are an expert software engineer, debugger, code reviewer,
software architect, and code optimization specialist.

Analyze the source code provided by the user.

Your responsibilities are:

1. Understand the purpose of the code.
2. Identify syntax errors.
3. Identify logical bugs.
4. Identify runtime errors.
5. Identify potential edge cases.
6. Identify security problems when relevant.
7. Identify inefficient or unnecessary code.
8. Explain the code in simple language.
9. Suggest practical improvements.
10. Generate a complete optimized version of the code.

Return ONLY valid JSON.

Do not write anything before the JSON.
Do not write anything after the JSON.
Do not use Markdown code fences around the JSON.

The response MUST follow exactly this structure:

{
    "summary": "Short overall assessment of the source code.",
    "bugs": [
        {
            "title": "Bug title",
            "severity": "Low",
            "description": "Detailed explanation of the problem.",
            "suggestion": "Specific recommendation to fix the problem."
        }
    ],
    "explanation": "Plain-language explanation of what the code does.",
    "improvements": [
        "Improvement suggestion 1",
        "Improvement suggestion 2"
    ],
    "optimized_code": "Complete optimized source code."
}

Severity MUST be one of:

Low
Medium
High
Critical

If no bugs are found, return:

"bugs": []

The optimized_code field MUST contain the complete source code.

Do not truncate the optimized code.

Preserve the original programming language.

Do not change the intended functionality unless required to fix a bug
or improve the implementation.
"""


uploaded_file = st.file_uploader(
    "📁 Upload a source code file",
    type=["py", "js", "java"],
    help="Supported files: Python (.py), JavaScript (.js), and Java (.java)"
)


if uploaded_file:

    file_name = uploaded_file.name
    file_extension = os.path.splitext(file_name)[1].lower()
    language = get_language(file_extension)

    try:
        code = uploaded_file.read().decode("utf-8")

    except UnicodeDecodeError:
        st.error(
            "❌ The uploaded file could not be decoded as UTF-8."
        )
        st.stop()

    if not code.strip():
        st.warning(
            "⚠️ The uploaded file is empty."
        )
        st.stop()

    st.divider()

    st.subheader("📄 Source Code")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "File",
            file_name
        )

    with col2:
        st.metric(
            "Language",
            language.title()
        )

    with col3:
        st.metric(
            "Characters",
            len(code)
        )

    st.code(
        code,
        language=language,
        line_numbers=True
    )

    st.divider()

    analyze_button = st.button(
        "🔎 Analyze Code",
        type="primary",
        use_container_width=True
    )

    if analyze_button:

        system_instruction = build_system_instruction()

        prompt = f"""
{system_instruction}

SOURCE FILE NAME:
{file_name}

SOURCE PROGRAMMING LANGUAGE:
{language}

SOURCE CODE:
{code}
"""

        with st.spinner(
            "🤖 Generative AI is analyzing your code..."
        ):

            try:

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

                result_text = response.text.strip()

            except Exception as error:

                st.error(
                    f"❌ AI analysis failed: {str(error)}"
                )

                st.stop()

        try:

            result = extract_json(result_text)

        except Exception:

            st.error(
                "❌ The AI returned an invalid structured response."
            )

            with st.expander(
                "🔎 View Raw AI Response"
            ):

                st.code(
                    result_text,
                    language="text"
                )

            st.stop()

        st.success(
            "✅ Code analysis completed successfully."
        )

        st.divider()

        st.subheader("📊 Analysis Summary")

        summary = result.get(
            "summary",
            "No summary was provided."
        )

        st.info(summary)

        st.divider()

        st.subheader("🐞 Bug Report")

        bugs = result.get(
            "bugs",
            []
        )

        if not isinstance(bugs, list):
            bugs = []

        if not bugs:

            st.success(
                "🎉 No major bugs were identified."
            )

        else:

            for index, bug in enumerate(
                bugs,
                start=1
            ):

                if not isinstance(
                    bug,
                    dict
                ):
                    continue

                title = bug.get(
                    "title",
                    f"Bug {index}"
                )

                severity = bug.get(
                    "severity",
                    "Unknown"
                )

                description = bug.get(
                    "description",
                    "No description provided."
                )

                suggestion = bug.get(
                    "suggestion",
                    "No suggestion provided."
                )

                with st.expander(
                    f"🐞 Bug {index}: {title} | Severity: {severity}",
                    expanded=True
                ):

                    st.markdown(
                        f"**Severity:** {severity}"
                    )

                    st.markdown(
                        f"**Description:** {description}"
                    )

                    st.markdown(
                        f"**Suggested Fix:** {suggestion}"
                    )

        st.divider()

        st.subheader("🧠 Code Explanation")

        explanation = result.get(
            "explanation",
            "No explanation was provided."
        )

        st.write(explanation)

        st.divider()

        st.subheader("💡 Suggested Improvements")

        improvements = result.get(
            "improvements",
            []
        )

        if isinstance(
            improvements,
            list
        ) and improvements:

            for improvement in improvements:

                st.markdown(
                    f"- {improvement}"
                )

        else:

            st.info(
                "No additional improvements were suggested."
            )

        st.divider()

        st.subheader("⚡ Optimized Code")

        optimized_code = result.get(
            "optimized_code",
            ""
        )

        if optimized_code:

            st.code(
                optimized_code,
                language=language,
                line_numbers=True
            )

        else:

            st.warning(
                "⚠️ The AI did not provide optimized code."
            )

        st.divider()

        st.subheader("📋 Structured Analysis")

        with st.expander(
            "View JSON Response"
        ):

            st.json(result)

else:

    st.info(
        "👆 Upload a Python, JavaScript, or Java source file to begin."
    )

    st.markdown(
        """
        ### 🚀 How It Works

        **1. Upload Code**

        Upload a `.py`, `.js`, or `.java` file.

        **2. Read Code**

        The application reads the uploaded file as a string.

        **3. AI Analysis**

        The source code is provided to Gemini as code context.

        **4. Bug Detection**

        The AI identifies bugs, runtime problems, logical issues,
        edge cases, and other potential problems.

        **5. Explanation**

        The AI explains the source code in plain language.

        **6. Improvements**

        The AI provides practical improvement suggestions.

        **7. Optimization**

        The AI generates an optimized version of the code.

        **8. Structured Results**

        The results are displayed in separate sections with
        syntax-highlighted code.
        """
    )