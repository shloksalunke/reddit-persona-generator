# 🤖 Reddit User Persona Generator (BeyondChats Internship Assignment)

This project generates a detailed **User Persona** from any **Reddit user's profile URL** by analyzing their public posts and comments using **Mistral AI**.

---

## 📌 Features

- 🧠 Scrapes Reddit user’s public comments and submissions
- 🔍 Uses Mistral LLM to extract personality traits, motivations, frustrations, etc.
- 📄 Outputs structured persona in `.txt` format
- 💬 Each characteristic is supported with citations from user's actual posts/comments
- ✅ Handles Reddit profile URL input via CLI

---

## 🚀 Technologies Used

- Python 3.12+
- Mistral AI API (`mistralai`)
- PRAW (Python Reddit API Wrapper)
- dotenv for secure API key handling

---

## 🧾 Assignment Requirements Checklist

| Requirement                                                                      | ✅ Status |
|----------------------------------------------------------------------------------|----------|
| Input is a Reddit **user profile URL**                                           | ✅ Done   |
| Scrape **posts + comments** of user                                              | ✅ Done   |
| Generate **User Persona** with LLM                                               | ✅ Done   |
| Save output in structured `.txt` file                                            | ✅ Done   |
| Cite posts/comments for each persona point                                       | ✅ Done   |
| Sample outputs for `kojied` and `Hungry-Move-6603` included                      | ✅ Done   |
| Public GitHub repo with instructions and executable code                        | ✅ Done   |

---

## 🛠 How to Setup & Run

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/reddit-persona-generator.git
cd reddit-persona-generator
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add your Mistral API key to `.env` file
Create a file named `.env` in the root folder and paste:
```
MISTRAL_API_KEY=your_mistral_api_key_here
```

### 5️⃣ Run the script
```bash
python -m src.main
```

### 6️⃣ Paste Reddit user profile URL when prompted:
```
🔗 Enter Reddit user profile URL:
https://www.reddit.com/user/Hungry-Move-6603/
```

---

## 📁 Project Structure

```
beyondchat_project/
├── src/
│   ├── main.py                 # Entry point
│   ├── reddit_scraper.py       # Reddit scraping logic
│   ├── persona_generator.py    # Mistral persona generation logic
│   └── utils.py                # File saving helper
├── output/                     # Generated persona .txt files
│   ├── kojied_persona.txt
│   └── Hungry-Move-6603_persona.txt
├── requirements.txt
├── .env                        # (excluded in .gitignore)
└── README.md
```

---

## 🔍 Sample Users Tested

- [https://www.reddit.com/user/kojied/](https://www.reddit.com/user/kojied/)
- [https://www.reddit.com/user/Hungry-Move-6603/](https://www.reddit.com/user/Hungry-Move-6603/)

Each output is saved in the `output/` folder with proper persona structure and citations.

---

## ❗ Notes

- ❌ Do **not** use subreddit URLs like `/r/...`. Only `/user/username/` URLs are supported.
- 🔐 Keep your API key secret. Do not commit your `.env` file.
- 🧠 If the user has very little public content, the persona will be limited or may fail.

---

## 🙌 Author

**Shlok Salunke**  
Built as part of BeyondChats AI/LLM Internship Assignment 💼  
Contact via [Internshala profile or GitHub](https://github.com/shloksalunke)

---
