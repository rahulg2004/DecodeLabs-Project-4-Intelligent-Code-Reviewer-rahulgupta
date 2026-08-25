# 🔍 Intelligent Code Reviewer & Explainer

An AI-powered developer utility built with **Python, Streamlit, and Google Gemini** that automatically analyzes source code, identifies bugs, explains code in plain language, suggests improvements, and generates an optimized version.

This project was developed as **Project 4: Intelligent Code Reviewer & Explainer** for the **DecodeLabs Generative AI Internship**.

---

## 📌 Project Overview

The **Intelligent Code Reviewer & Explainer** is a Generative AI-based developer utility designed to automate common code-review tasks.

The application allows a user to upload a raw source-code file in supported programming languages. The uploaded code is read as a string and provided to a Generative AI model as code context.

The AI then analyzes the code and returns a structured review containing:

* 🐞 Bug Report
* 🧠 Plain-Language Explanation
* 💡 Improvement Suggestions
* ⚡ Optimized Code
* 📊 Overall Code Summary
* 📋 Structured JSON Response

The project focuses on **code-as-context management, structured outputs, and code analysis pipelines**, which are the key skills specified in the Project 4 brief. 

---

## 🎯 Project Objective

The primary objective is to build a developer utility that can:

1. Accept a raw source-code file.
2. Read the uploaded code as a string.
3. Provide the code to a Generative AI model as contextual input.
4. Analyze the code for potential bugs and issues.
5. Explain the code in simple language.
6. Generate practical improvement suggestions.
7. Produce an optimized version of the code.
8. Return the analysis in a structured format.
9. Display the results in a clear and developer-friendly interface.

The official project brief describes the goal as building a utility that analyzes a code block, identifies bugs, and explains the code in plain language. 

---

# ✨ Key Features

## 📁 1. Source Code Upload

The application provides a file uploader that accepts source-code files.

### Supported languages

| Language      | Extension |
| ------------- | --------- |
| 🐍 Python     | `.py`     |
| 🟨 JavaScript | `.js`     |
| ☕ Java        | `.java`   |

The project brief specifically requires ingestion of `.py`, `.js`, and `.java` files as strings. 

---

## 📄 2. Source Code Preview

After uploading a file, the application displays:

* File name
* Programming language
* Character count
* Complete source code
* Syntax highlighting
* Line numbers

This allows the user to verify the uploaded code before running the AI analysis.

---

## 🤖 3. Generative AI Code Analysis

The uploaded source code is passed to the **Google Gemini** model for analysis.

The application uses a carefully designed system instruction that tells the model to behave as an expert:

* Software engineer
* Debugger
* Code reviewer
* Software architect
* Code optimization specialist

The model analyzes the actual uploaded source code rather than relying on a predefined example.

---

## 🐞 4. Bug Detection

The AI reviews the source code for different types of potential problems, including:

* Syntax errors
* Logical bugs
* Runtime errors
* Potential edge cases
* Security concerns when relevant
* Inefficient or unnecessary code

Each identified bug can include:

* Bug title
* Severity
* Description
* Suggested fix

### Severity levels

The application uses:

* 🟢 Low
* 🟡 Medium
* 🟠 High
* 🔴 Critical

If no major problems are identified, the application displays an appropriate success message.

---

## 🧠 5. Plain-Language Code Explanation

The application generates a simple explanation of what the submitted code does.

This helps users understand unfamiliar code without manually analyzing every function, statement, or block.

The project brief specifically requires the tool to explain the analyzed code in plain language. 

---

## 💡 6. Improvement Suggestions

The AI provides practical suggestions for improving the submitted source code.

Suggestions can relate to:

* Readability
* Efficiency
* Maintainability
* Error handling
* Code structure
* Performance
* Reliability
* Security when applicable

These suggestions are displayed separately from the bug report.

---

## ⚡ 7. Optimized Code Generation

After analyzing the source code, the AI generates a complete optimized version.

The optimized code:

* Preserves the original programming language
* Attempts to preserve intended functionality
* Addresses identified issues
* Improves the implementation where appropriate
* Is displayed with syntax highlighting
* Includes line numbers

The project requirements specifically call for the model to output a distinct bug report and an optimized code block. 

---

## 📊 8. Analysis Summary

The application provides an overall assessment of the submitted source code.

The summary gives the user a quick understanding of the code quality and the main issues identified by the AI.

---

## 📋 9. Structured AI Output

Instead of relying on an unrestricted text response, the application instructs Gemini to return a predefined JSON structure.

The expected structure is:

```json
{
    "summary": "Short overall assessment",
    "bugs": [
        {
            "title": "Bug title",
            "severity": "High",
            "description": "Description of the problem",
            "suggestion": "Suggested fix"
        }
    ],
    "explanation": "Plain-language explanation",
    "improvements": [
        "Improvement suggestion"
    ],
    "optimized_code": "Complete optimized source code"
}
```

The application parses this JSON and displays each section independently.

This demonstrates the **structured outputs** concept highlighted in the project requirements. 

---

# 🎨 10. Syntax Highlighting

The application uses Streamlit's code rendering to display both the original and optimized code with syntax highlighting.

For example:

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

The language is automatically selected based on the uploaded file extension.

This satisfies the requirement to render code snippets with formatting and syntax highlighting. 

---

# 🔄 Application Workflow

The complete workflow is:

```text
                 👤 User
                    │
                    ▼
           📁 Upload Source File
                    │
                    ▼
             📄 Read File
                    │
                    ▼
         🔎 Validate File Content
                    │
                    ▼
       📝 Convert Code to String
                    │
                    ▼
       🧠 Add System Instructions
                    │
                    ▼
           🤖 Gemini AI Model
                    │
                    ▼
           📋 Structured JSON
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       🐞 Bugs   🧠 Explain   💡 Improve
          │         │         │
          └─────────┼─────────┘
                    ▼
             ⚡ Optimized Code
                    │
                    ▼
           🎨 Streamlit UI
                    │
                    ▼
              👤 User Review
```

---

# 🧩 Core Generative AI Concepts

## 1. Code-as-Context Management

The uploaded source code is read from the user's file and supplied to the Generative AI model as contextual information.

The model therefore performs its analysis based on the actual source code provided by the user.

---

## 2. Structured Outputs

The AI is instructed to return a predefined JSON format instead of an unrestricted response.

This makes it possible for the application to reliably separate:

```text
Summary
    ↓
Bug Report
    ↓
Explanation
    ↓
Improvements
    ↓
Optimized Code
```

---

## 3. Code Analysis Pipeline

The application implements a complete code-analysis pipeline:

```text
File Upload
    ↓
File Reading
    ↓
Input Validation
    ↓
Code Context Creation
    ↓
AI Analysis
    ↓
JSON Parsing
    ↓
Result Validation
    ↓
Result Rendering
```

These concepts correspond directly to the key skills identified in the Project 4 document: **Code-as-context management, structured outputs, and code analysis pipelines**. 

---

# 🛠️ Technologies Used

## Programming Language

### 🐍 Python

Used for:

* Application logic
* File processing
* Gemini API integration
* JSON processing
* Error handling

---

## 🎨 User Interface

### Streamlit

Used to build the interactive web interface.

Streamlit provides:

* File uploader
* Buttons
* Expandable sections
* Metrics
* Code rendering
* Syntax highlighting
* Status messages
* Responsive layout

---

## 🤖 Generative AI

### Google Gemini

Used for:

* Code analysis
* Bug identification
* Code explanation
* Improvement suggestions
* Code optimization
* Structured output generation

---

## 📦 Google Gen AI SDK

The Google Gen AI SDK is used to communicate with the Gemini API from Python.

---

## 🔐 Environment Variables

### python-dotenv

Used to load the Gemini API key securely from the `.env` file.

---

## 📋 JSON

Used as the structured communication format between the AI analysis layer and the Streamlit interface.

---

# 📂 Project Structure

```text
Intelligent-Code-Reviewer/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
└── venv/
```

### File Description

| File               | Purpose                                                   |
| ------------------ | --------------------------------------------------------- |
| `app.py`           | Main Streamlit application                                |
| `.env`             | Stores Gemini API key                                     |
| `.gitignore`       | Prevents sensitive/unnecessary files from being committed |
| `requirements.txt` | Python dependencies                                       |
| `README.md`        | Project documentation                                     |
| `venv/`            | Python virtual environment                                |

---

# ⚙️ System Requirements

Before running the project, make sure you have:

* Windows, macOS, or Linux
* Python 3.x
* Internet connection
* VS Code or another Python IDE
* Gemini API key
* Git, if you want to upload the project to GitHub

---

# 🚀 Installation Guide

## Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

---

## Step 2: Open the Project

```bash
cd Intelligent-Code-Reviewer
```

---

## Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

---

## Step 4: Activate the Virtual Environment

### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Key Configuration

The application requires a Gemini API key.

Create a file named:

```text
.env
```

in the root project directory.

Add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
```

Replace the placeholder with your actual API key.

### Important Security Rule

Never commit your `.env` file to GitHub.

The `.gitignore` file already contains:

```text
.env
```

to help prevent accidental exposure of the API key.

---

# ▶️ Running the Application

After activating the virtual environment, run:

```bash
streamlit run app.py
```

Streamlit will provide a local URL similar to:

```text
http://localhost:8501
```

Open the URL in your browser.

---

# 🖥️ Using the Application

## Step 1: Open the Application

Launch the Streamlit application.

You will see:

```text
🔍 Intelligent Code Reviewer & Explainer
```

---

## Step 2: Upload Code

Click:

```text
📁 Upload a source code file
```

Select one of:

```text
.py
.js
.java
```

---

## Step 3: Review the Source Code

The application displays:

* File name
* Programming language
* Character count
* Original source code

---

## Step 4: Start Analysis

Click:

```text
🔎 Analyze Code
```

The application sends the source code to Gemini.

---

## Step 5: View the Summary

The AI provides an overall assessment of the code.

---

## Step 6: Review Bugs

Open the bug-report sections to view:

* Bug title
* Severity
* Description
* Suggested fix

---

## Step 7: Read the Explanation

The application provides a plain-language explanation of the code.

---

## Step 8: Review Improvements

The AI provides suggestions for improving the implementation.

---

## Step 9: Review Optimized Code

The application displays the complete optimized source code with syntax highlighting.

---

## Step 10: View Structured JSON

The final section allows you to inspect the structured AI response.

---

# 🧪 Testing

## 🐍 Python Test

Create a file named:

```text
test.py
```

Use:

```python
def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


values = [10, 20, 30]

print("Average:", calculate_average(values))

print(undefined_variable)
```

Upload it and click:

```text
🔎 Analyze Code
```

The AI should identify the undefined variable and provide a code explanation and optimized version.

---

## 🟨 JavaScript Test

Create:

```text
test.js
```

Use:

```javascript
function calculateTotal(price, quantity) {
    let total = price * quantity;
    console.log(total);
}

calculateTotal("100", 2);
```

Upload the file and analyze it.

---

## ☕ Java Test

Create:

```text
test.java
```

Use:

```java
public class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 0;

        System.out.println(a / b);
    }
}
```

Upload the file and analyze it.

---

# 🛡️ Error Handling

The application includes handling for several common problems.

### Missing API Key

If `GEMINI_API_KEY` is not found:

```text
GEMINI_API_KEY is missing.
```

The application stops until the API key is configured.

### Empty File

If the uploaded source file contains no code:

```text
The uploaded file is empty.
```

### Invalid File Encoding

If the application cannot decode the uploaded source file:

```text
The uploaded file could not be decoded as UTF-8.
```

### AI API Error

If the Gemini request fails, the application displays the returned error instead of crashing silently.

### Invalid AI Response

If Gemini does not return valid JSON, the application displays the raw response for debugging.

### Missing Optimized Code

If the AI does not return optimized code, the application displays a warning.

---

# 🔐 Security Considerations

The Gemini API key is stored in an environment variable.

The project does **not** hard-code the API key inside `app.py`.

The `.env` file is excluded from Git using:

```text
.env
```

in `.gitignore`.

### Never commit:

```text
.env
API keys
Passwords
Access tokens
Private credentials
```

---

# 📊 Example Output

After analyzing a source file, the application produces a result similar to:

```text
📊 Analysis Summary
The program calculates an average but contains an undefined variable.

🐞 Bug Report

Bug 1
Severity: High

Description:
The variable undefined_variable has not been declared.

Suggested Fix:
Define the variable before using it.

🧠 Code Explanation

The program calculates the average of a list of numbers
and prints the result.

💡 Suggested Improvements

- Add input validation.
- Handle empty lists.
- Use clearer variable names.

⚡ Optimized Code

[Syntax-highlighted optimized source code]
```

---

# 📈 Possible Future Enhancements

The current implementation focuses on the requirements of Project 4. The following features could be added in future versions:

## 🔗 GitHub Integration

Allow users to analyze:

* Individual GitHub files
* GitHub repositories
* Multiple source files

---

## 📊 Code Quality Score

Add an overall score based on:

* Bugs
* Readability
* Maintainability
* Complexity
* Performance
* Security

---

## 🔒 Security Analysis

Add dedicated detection for:

* Hard-coded credentials
* Unsafe input handling
* Injection vulnerabilities
* Insecure functions
* Weak authentication patterns

---

## 🧪 AI-Generated Unit Tests

Automatically generate unit tests based on the submitted code.

---

## 📑 Downloadable Reports

Allow users to export the code review as:

* PDF
* Markdown
* JSON
* TXT

---

## 🔄 Side-by-Side Comparison

Display:

```text
Original Code        Optimized Code
-------------        --------------
Original line 1      Improved line 1
Original line 2      Improved line 2
Original line 3      Improved line 3
```

---

## 🌐 More Programming Languages

Potential future support:

* C
* C++
* C#
* Go
* Rust
* PHP
* TypeScript
* Kotlin
* Swift

---

## 🧪 Code Execution Sandbox

A secure sandbox could be added to test generated code before presenting it to users.

This should only be implemented with appropriate isolation and security controls.

---

# 🎓 Skills Demonstrated

This project demonstrates practical experience with:

* 🐍 Python Programming
* 🤖 Generative AI
* 🧠 Prompt Engineering
* 🔗 Gemini API Integration
* 📦 Google Gen AI SDK
* 📋 Structured AI Outputs
* 📄 JSON Processing
* 📁 File Handling
* 🔎 Automated Code Analysis
* 🐞 Debugging
* ⚡ Code Optimization
* 🎨 Streamlit UI Development
* 📝 Markdown Rendering
* 🛡️ Error Handling
* 🔐 Environment Variable Management
* 🌐 Git & GitHub
* 💻 Developer Utility Development

The official project identifies **Code-as-context management, structured outputs, and code analysis pipelines** as the key skills demonstrated by this project. 

---

# 🏗️ Architecture

```text
┌─────────────────────────────┐
│       Streamlit UI          │
│                             │
│  File Upload + User Input   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       File Processing       │
│                             │
│  Read + Validate Source     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Prompt Construction     │
│                             │
│ System Instructions         │
│ + Source Code Context       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Google Gemini         │
│                             │
│ Code Analysis + Generation  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Structured JSON         │
│                             │
│ Summary                     │
│ Bugs                        │
│ Explanation                 │
│ Improvements                │
│ Optimized Code              │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Result Renderer       │
│                             │
│ Bug Report                  │
│ Explanation                 │
│ Improvements                │
│ Optimized Code              │
└─────────────────────────────┘
```

---

# 📋 Project Requirements Mapping

| Project Requirement        | Implementation                    |
| -------------------------- | --------------------------------- |
| Ingest raw code file       | Streamlit file uploader           |
| `.py` support              | ✅                                 |
| `.js` support              | ✅                                 |
| `.java` support            | ✅                                 |
| Read code as string        | Python file decoding              |
| Code analysis              | Gemini                            |
| Bug identification         | AI-generated bug report           |
| Plain-language explanation | AI-generated explanation          |
| Structured output          | JSON response                     |
| Optimized code             | AI-generated optimized source     |
| Markdown/code rendering    | Streamlit rendering               |
| Syntax highlighting        | `st.code()`                       |
| Code-as-context            | Uploaded code passed to Gemini    |
| Code analysis pipeline     | Upload → Analyze → Parse → Render |

The mapping above is based on the requirements stated in the supplied Project 4 document. 

---

# 🏆 Project Outcome

The completed application demonstrates how Generative AI can be integrated into a practical developer utility.

Instead of simply generating isolated code snippets, the application takes an existing source file, uses it as AI context, analyzes the implementation, produces structured findings, explains the code, recommends improvements, and generates an optimized version.

The DecodeLabs brief describes this project as an **optional mastery phase** focused on demonstrating developer utilities that manage code-as-context and structured outputs. 

---

# 📸 Suggested Screenshots for GitHub

For a strong GitHub README, consider adding screenshots of:

### Screenshot 1

🏠 Main application interface

### Screenshot 2

📄 Uploaded source code

### Screenshot 3

🐞 Bug Report

### Screenshot 4

🧠 Code Explanation

### Screenshot 5

💡 Suggested Improvements

### Screenshot 6

⚡ Optimized Code

### Screenshot 7

📋 Structured JSON Response

Example README section:

```markdown
## 📸 Screenshots

### 🏠 Application Interface

![Application Interface](screenshots/home.png)

### 🐞 Bug Analysis

![Bug Analysis](screenshots/bug-report.png)

### ⚡ Optimized Code

![Optimized Code](screenshots/optimized-code.png)
```

You can create a `screenshots` folder:

```text
Intelligent-Code-Reviewer/
│
├── screenshots/
│   ├── home.png
│   ├── bug-report.png
│   └── optimized-code.png
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 👨‍💻 Author

**Rahul Gupta**

🎓 B.Sc. (Hons) Computer Science
🏫 University of Delhi
🤖 Generative AI & Data Science Enthusiast

---

# 📜 Internship

**DecodeLabs**

**Program:** Generative AI Internship

**Project:** Project 4 - Intelligent Code Reviewer & Explainer

The supplied project document identifies this as the fourth project and describes it as an optional mastery phase. 

---

# ⭐ Conclusion

The **Intelligent Code Reviewer & Explainer** demonstrates a complete Generative AI application workflow:

```text
Raw Code
   ↓
Code-as-Context
   ↓
Generative AI
   ↓
Structured Output
   ↓
Bug Analysis
   ↓
Code Explanation
   ↓
Improvement Suggestions
   ↓
Optimized Code
   ↓
Developer-Friendly Interface
```

The project provides practical experience in building an AI-powered developer utility rather than using Generative AI only for basic text generation.

---

## 📄 License

This project is developed for educational and internship purposes.
