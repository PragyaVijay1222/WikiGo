# WikiGo - Summary at Your Fingertips

**WikiGo** is a web application designed to read through an entire Wikipedia article and provide a concise summary in about 50 lines. This tool leverages powerful NLP techniques, ensuring you get the most important information quickly and efficiently.

---

## 🚀 Features

- Summarizes entire Wikipedia articles into approximately 50 lines.
- Utilizes advanced natural language processing (NLP) pipelines.
- Lightweight, easy-to-use interface for smooth user interaction.
- Asynchronous handling of requests for enhanced performance.

---

## 🛠️ Tech Stack

- **Backend**: Flask (`flask`, `request`, `jsonify`, `render_template`)
- **NLP**: Transformers (`pipeline`)  
- **Asynchronous Processing**: `asyncio`, `aiohttp`
- **Deep Learning**: Torch (`torch`)  
- **Frontend**: HTML, CSS

---

## 📂 Directory Structure

```plaintext
WikiGo/
├── static/
│   └── styles.css        # Contains CSS for styling the frontend
├── templates/
│   └── index.html        # HTML for the website structure
├── app.py                # Main Flask application
```
---

## 🌟 How It Works

**Input**: Users provide a Wikipedia article name through the interface.
**Processing**:  - The Flask app handles the request.
                 - The transformers library processes the text to generate a summary.
                 - Asynchronous techniques (asyncio, aiohttp) optimize performance.
**Output**: A concise, readable summary is presented in the frontend.

---

## 🚀 Getting Started

**1️⃣ Prerequisites**

Make sure you have the following installed:

Python 3.9+

`pip` package manager

**2️⃣ Installation**

Clone the repository and install dependencies:

git clone https://github.com/your-username/WikiGo.git
cd WikiGo
pip install -r requirements.txt

3️⃣ Running the App
Run the Flask development server:

python app.py

Access the site locally at: http://localhost:5000

---

🖼️ Screenshots
Include a screenshot of your project interface for better visualization:


Make sure the screenshot is saved as project_screenshot.png in the static/ folder to display it properly.

---

📚 Future Enhancements
Add support for multilingual Wikipedia summaries.

Include graphical visualizations for article insights.

Implement user authentication for personalized summaries.

---

🤝 Contributing
Contributions are welcome! Follow these steps to contribute:

Fork the repository.

Create a new branch: `git checkout -b feature-name`.

Commit your changes: `git commit -m 'Add some feature'`.

Push to the branch: `git push origin feature-name`.

Open a pull request.

---

📄 License
This project is licensed under the MIT License.

---

🙌 Acknowledgements
Wikipedia for the content.

Hugging Face Transformers for the NLP library.

Flask for the web framework.

---

🖇️ Contact
If you have any questions or feedback, feel free to reach out!

Author: Pragya Email: [Your Email Here] Portfolio: [Your Portfolio Website Link]
