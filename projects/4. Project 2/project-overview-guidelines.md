# Project Overview Guidelines

This is intended to provide a high-level guideline that can be applied to all projects, with the goal of creating portfolio-ready repos that you will be proud to share with recruiters and future employers.

There should be a clear flow from one notebook to the next. The entire project tells the story. Viewers of your project shouldn’t have to search through notebook after notebook looking for specific parts. It should be very clear from markdown, code comments, and your executive summary. 

We like to see how you think and work, but that is why we have labs! Project repositories should be well polished and have a logical flow. This means that projects should be:
* Well organized
* Easy to follow (commenting and markdown really helps here!)
* Replicable (relative file paths and error-free)

---

## File Structure

| Directory / File | Expected Contents & Guidelines |
| :--- | :--- |
| **`README.md`** | **Problem Statement:** 1-2 sentences.<br>**Executive Summary:** 2-3 paragraphs including a brief overview of your process, important findings, conclusions, and recommendations.<br>**File Directory:** Table of contents with clearly labeled descriptive names.<br>**Data & Data Dictionary:** A sentence or two about the source of your data (with a link if data isn't in the repo). Include all features in your final cleaned file and any engineered features.<br>**Conclusions & Recommendations.**<br>**Areas for Further Research/Study.**<br>**Sources.**<br>**Important Visualizations:** Include a few that highlight your findings (can be in the Executive Summary, Conclusions, or its own section). |
| **`Data/` folder** | Original data files.<br>Cleaned data files. |
| **`Code/` folder** | `01_Data_Collection`<br>`02_Data_Cleaning`<br>`03_EDA`<br>`04_Modeling` _(**Note:** This is not applicable to this project, but it will be for future projects. This can be multiple notebooks, for example: `04a_Logistic_Regression_Models`, `04b_Naive_Bayes_Models`)_ |
| **`Presentation/` folder** | Presentation `.pdf` file.<br>Images folder (if needed). |
| **`Scratch/` folder** | Any of your work that you want to save, but do not want to be evaluated on. |

---

## Presentation Structure

**You must be ready to present your findings by the start of class on the date set by your instructor.**

**Make it clean and professional:**

| Section | What to Include |
| :--- | :--- |
| **1. Cover Page** | Project Title, name, date, and cohort details. |
| **2. Introduction & Background** | Give a high-level overview of the industry or topic you are exploring so the audience understands the context. |
| **3. Problem Statement & Project Goals** | Clearly define the specific challenge or pain point you are tackling. What is the core question you are trying to answer, and what are the goals of this project? |
| **4. Data & Methodology** | Briefly explain your data source, its scope, and how you approached the analysis. The audience needs to trust your process before they look at your results! |
| **5. Agenda (Roadmap)** | A quick breakdown of the main pillars or areas you will be discussing. Give the audience a map of the journey ahead. |
| **6. Deep Dive: Analysis & Key Insights** | This is the heart of your presentation. For each main point on your agenda, present your charts, patterns, and—most importantly—your insights. Don't just show data; explain what it actually means. |
| **7. Summary of Findings (Conclusion)** | Tie everything together. What are the absolute biggest takeaways from your analysis? Summarize the core truth the data revealed. |
| **8. Recommendations & Next Steps** | Translate your data into action. Based on your insights, what strategic decisions or concrete steps should the business or stakeholder take next? |

---

## Notebook Cleanup: Before You Submit

* **Remove erroneous libraries:** Only import the libraries you need for this specific notebook.
* **Remove erroneous cells:** Did you create a function that you don’t use? Remove it! Did you create visualizations that don’t add to your data storytelling? Remove them!
* **Restart and run all:** It is good practice to restart your kernel and run all cells before submitting. This is a great way to double check for errors and remove those.
* **Keep notebooks siloed:** Data Science is recursive. You might get through EDA, start modeling, and then realize there are more features to explore. That's great! However, all EDA should be in the EDA notebook, all modeling in the modeling notebook, etc. The idea is to capture the workflow, rather than your flow of thought.

> **Note:** Remember, these are guidelines! Your structure will change from project to project, but this is a great baseline format to follow. Now let's get to work on some portfolio-worthy projects!