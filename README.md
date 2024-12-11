
# 🚀 **Reddit Data Analysis with Spark** 📝🔥

Welcome to the **Reddit Data Analysis Project**, where we harness the power of **Apache Spark** for big data processing and transform Reddit posts into meaningful insights using **word clouds**. 🌟  

![Word Cloud Example](content/word_cloud_sample.png)  
*Visualizing trends and hot topics from a Subreddit discussions.*

---

## 🧐 **Project Overview**

Reddit is a goldmine of user-generated content across thousands of communities. This project focuses on:  
- **Data Collection**: Extracting Reddit comments via APIs.  
- **Data Processing**: Using **Apache Spark** to filter, clean, and analyze large datasets.  
- **Data Visualization**: Creating visually appealing **word clouds** to highlight trending topics.  

---

## ✨ **Features**
- 🚀 **High-Performance Processing**: Apache Spark ensures scalability for analyzing millions of comments.  
- 🧹 **Data Cleaning**: Removes noise, stop words, and keep nouns for meaningful analysis.  
- 🎨 **Interactive Word Clouds**: Visualize key trends and hot topics in vibrant, dynamic word clouds.  
<!-- - 🔄 **Automation**: Scheduled workflows using **Airflow** for regular updates.   -->

---

## 🔧 **Tech Stack**
- **Big Data Framework**: Apache Spark  
- **Programming Language**: Python  
- **Visualization**: WordCloud, Matplotlib  
<!-- - **Task Scheduling**: Apache Airflow   -->
<!-- - **Data Sources**: Reddit API   -->
<!-- - **Deployment**: Docker, AWS (optional for scalability)   -->

---
## 📂 **Project Structure**

```plaintext
.
├── data/                  # Raw and processed data files
├── notebooks/             # Jupyter Notebooks for exploration
├── src/                   # Source code for the project
│   ├── api/               # Scripts for extracting Reddit data
│   ├── processing/        # Spark scripts for data cleaning and analysis
│   ├── visualization/     # Scripts to generate word clouds
│   └── utils/             # Utility scripts for reusable components
├── airflow/               # Airflow DAGs for scheduling tasks
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

## 🚀 **Getting Started**

### 1️⃣ Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:t07902301/Reddit-Topics.git
   cd Reddit-Topics
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Spark
   3. Install Spark:
      Follow the instructions on the [Apache Spark Installation Guidance](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/05-batch#52-installation) to download and install Spark.

### 2️⃣ Run the Project
1. execute [run.sh](run.sh) 

   To analyze word freq of 100 most recent posts in *r/travel*, use this example command. 

   ```bash
   ./run.sh https://www.reddit.com/r/travel.json?limit=100 content/test.png
   ```

   Use *run.sh -h* for more info. 

2. check the word freq analysis result on the [destination path](content/test.png). 

<!-- ### 3️⃣ Set Up Reddit API -->
<!-- - Get your API keys from [Reddit's API](https://www.reddit.com/dev/api/).  
- Add your credentials to a `.env` file:
  ```plaintext
  CLIENT_ID=your-client-id
  CLIENT_SECRET=your-client-secret
  USER_AGENT=your-user-agent
  ```

### 4️⃣ Run the Project
1. Fetch Reddit data:
   ```bash
   python src/api/fetch_reddit_data.py
   ```
2. Process data with Spark:
   ```bash
   spark-submit src/processing/analyze_data.py
   ```
3. Generate word clouds:
   ```bash
   python src/visualization/generate_wordcloud.py
   ```
4. View the results:
   Open the generated word cloud image in `output/`.

---

## 📊 **Example Output**
Here’s an example of what you can achieve with this project:  
![Word Cloud](https://via.placeholder.com/600x300.png?text=Sample+Word+Cloud)  

---

## 🌟 **Future Enhancements**
- Add sentiment analysis for deeper insights.  
- Support additional data sources like Twitter or YouTube comments.  
- Deploy a real-time dashboard using **Streamlit** or **Flask**.  

---

## 🤝 **Contributing**
We welcome contributions! Feel free to:
1. Fork the repository.
2. Create a feature branch:  
   ```bash
   git checkout -b feature-branch
   ```
3. Submit a pull request.

--- -->

## 📄 **License**
This project is licensed under the [MIT License](LICENSE).

---

## ❤️ **Acknowledgments**
- [Reddit API](https://www.reddit.com/dev/api/) for providing data.  
- [Apache Spark](https://spark.apache.org/) for its powerful big data processing.  
- [WordCloud](https://github.com/amueller/word_cloud) library for stunning visualizations.  
- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) for detailed intructions on the set-up and the use of Spark. 
---

Let’s uncover the trends in Reddit conversations! 🚀  
Feel free to reach out for questions or feedback! 😊