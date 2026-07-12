<h1>
  <span class="prefix"></span>
  <span class="headline">Project 2: Exploratory Data Analysis</span>
</h1>

## About
Our first unit in the course covers:
- Basic statistics
- Many Python programming concepts
- Programmatically interacting with files and directories
- Visualizations
- EDA
- Working with Jupyter notebooks for development and reporting

You might wonder if you're ready to start doing data science. While you still have **tons** to learn, there are many aspects of the data science process that you're ready to tackle. This project aims to allow you to practice and demonstrate these skills.

---

## Prerequisites
- Write and run Python code in a Jupyter notebook.
- Create basic Python functions.
- Python programming skills including using modules and libraries.
- Understand what Exploratory Data Analysis is and how to do it using Python and `pandas`.

---

### Deliverables

All of your projects will comprise of a written technical report and a presentation. As we continue in the course, your technical report will grow in complexity, but for this project it will comprise:
- A Jupyter notebook that describes your data with visualizations & statistical analysis.
- A README markdown file that provides an introduction to and overview of your project.
- Your presentation slideshow rendered as a .pdf file.

**NOTE**: Your entire GitHub repository will be evaluated as your technical report. Make sure that your files and directories are named appropriately, that all necessary files are included, and that no unnecessary or incomplete files are included.

For your presentation, you'll be presenting to a **non-technical** audience. You should prepare a slideshow with appropriately scaled visuals to complement a compelling narrative. **Presentations should be about 5 minutes.** Time tends to fly when presenting, and doing a dry run for a friend or family member is a great way to practice.

---

### Data sets

**Important Note:** Your dataset has been pre-assigned to you by your instructor. Please find your name in the table below to see which data you will be working with for this project.

| No. | Topic | Assigned Students | Info |
| :--- | :--- | :--- | :--- |
| **1** | **World Development Statistics** | Reem AlShehabi<br>Zainab<br>Mohamed Shawqi<br>Mohammed Hejairi | There are 3 data files included for this specific topic. You are required to use **at least two** of these files to complete your analysis. Feel free to use all three if you would like, or add other relevant datasets you find online.<br>We're going to take a look at World Development Statistics from [Gapminder](https://www.gapminder.org/about/), an independent Swedish foundation that aims to make data about the world more accessible and reliable. A good introduction on Gapminder is this [Ted Talk](https://www.ted.com/talks/hans_rosling_the_best_stats_you_ve_ever_seen) from Hans Rosling, which also shows how effective data visualization can be for your audience.<br>**Access:** [Google Drive Link](https://drive.google.com/drive/folders/…?usp=drive_link) (Includes the datasets). |
| **2** | **Olympics** | Ali Husain<br>Mohamed Salah<br>Reem Hussain<br>Zahra | This is a historical dataset on the modern Olympic Games, including all the Games from Athens 1896 to Rio 2016.<br>Scraped from [sports-reference](http://www.sports-reference.com) in May 2018.<br>Note that the Winter and Summer Games were held in the same year up until 1992. After that, they staggered them such that Winter Games occur on a four year cycle starting with 1994, then Summer in 1996, then Winter in 1998, and so on. A common mistake people make when analyzing this data is to assume that the Summer and Winter Games have always been staggered.<br>**Access:** [Google Drive Link](https://drive.google.com/drive/folders/…?usp=drive_link) (Includes the dataset). |
| **3** | **Startup Investments** | Ali AlSaboodi<br>Meqdad<br>Ohood<br>Qaem<br>Ali Radhi | This dataset, sourced from Crunchbase, offers a comprehensive look into the global startup ecosystem. It contains historical funding records for tens of thousands of companies worldwide, providing valuable insights into venture capital trends, industry growth, and startup success rates. Each entry includes information such as company name, market category, geographic location, funding rounds, total funding raised (in USD), founding date, and current operating status (e.g., operating, acquired, IPO, or closed).<br>**Access:** [Google Drive Link](https://drive.google.com/drive/folders/…?usp=drive_link) (Includes the dataset and a data dictionary). |
| **4** | **Bahrain Imports** | Mohamed Jasim<br>Sayed Ali Mahmood<br>Fatema Shamlooh<br>Fatima Jaffer<br>Malak Adel | This dataset, sourced from the [Bahrain Open Data Portal](https://www.data.gov.bh/explore/?disjunctive.theme&sort=modified), offers a detailed overview of the Kingdom's international trade activities from 2021 to 2025. It contains monthly transaction-level records of imports, providing valuable insights into trade patterns, commodity flows, and economic relationships. Each entry includes information such as partner country, commodity type, transaction value, weight (in kilograms), quantity, and unit of measure.<br>For further reference, [Bahrain Customs Affairs](https://www.customs.gov.bh/en) serves as the primary source of this information. Additionally, [this HS Code reference](https://www.foreign-trade.com/reference/hscode.htm) is helpful to understand the commodity categories.<br>**Access:** [Google Drive Link](https://drive.google.com/drive/folders/…?usp=drive_link) (Includes a data dictionary). |
| **5** | **Wind Turbines** | Gana<br>Sayed Ali Murtadha<br>Hawraa<br>Kawthar<br>Malak Mahdi | Main file (`wind-turbines.csv`): Data on wind turbines in the U.S. (location, which plant they are in, how much power they generate, etc.). It is from the [U.S. Wind Turbine Database](https://emp.lbl.gov/publications/us-wind-turbine-database-files).<br>Secondary file Power Plant: Data on operators within the U.S. energy space. Data is from [EIA-923](https://www.eia.gov/electricity/data/eia923/).<br>**Access:** [Google Drive Link](https://drive.google.com/drive/folders/…?usp=drive_link) (Includes the dataset, extra datasets, and a data dictionary). |
| **6** | **Stack Overflow** | Fatema AlSabah<br>Sara AlNajjar<br>Elias<br>Fatima Mahdi<br>Hajar | This dataset, sourced from the annual Stack Overflow Developer Survey, offers a comprehensive look into the global software development community. It contains responses from tens of thousands of developers worldwide, providing valuable insights into industry trends, technology adoption, and compensation patterns. Each entry includes information such as demographics, education, employment status, popular programming languages, tools used, and salary details.<br>For further reference, the [Stack Overflow Developer Survey](https://survey.stackoverflow.co/) serves as the primary source of this information.<br>**Access:** [Google Drive Link](https://drive.google.com/drive/folders/…?usp=drive_link) (Includes a data dictionary). |

#### Additional Data
You are welcome to add any other data sources you find online to support your analysis, but this is **not required**.

---
### Problem Statement

Based on your assigned topic above, select one of the corresponding problem statement approaches below to guide your analysis.

| No. | Topic | Problem Statement |
| :--- | :--- | :--- |
| **1** | **World Development Statistics** | **1st Approach: Targeted Funding for "Hollow Growth" Regions**<br>Problem Statement: Top-level economic growth often masks underlying crises, such as rapid population expansion diluting wealth or rising incomes failing to improve life expectancy. The Policy Steering Committee needs to analyze historical population, GNI per capita, and life expectancy trends (1960-2020) to identify nations trapped in these hollow growth cycles. Pinpointing these disconnects will allow the agency to accurately target a $100M intervention fund to countries suffering from stalled human development.<br><br>**2nd Approach: Human Capital Strategy & Philanthropy**<br>Problem Statement: A philanthropic foundation lacks clear historical blueprints to design effective human development programs. The Strategy Director needs to evaluate combined historical trends of population, life expectancy, and GNI to identify countries that successfully transitioned from low-income and low-lifespan to high-income and high-lifespan statuses. Uncovering these proven baselines will allow the foundation to implement evidence-based programs modeled after these successful nations. |
| **2** | **Olympics** | **1st Approach: Historical Evolution of Athlete Specialization**<br>Problem Statement: A sports institute needs to analyze how the physical sizes of winning Olympic athletes have changed over time. Discovering the modern ideal body type for each sport will help the institute accurately direct $5M in grants to youth programs that train athletes to match these winning physical profiles.<br><br>**2nd Approach: Strategic Investment in "Open" Sports**<br>Problem Statement: Developing nations often waste limited funds competing in Olympic sports dominated by a few global superpowers. As a sports analytics agency consulting for a developing National Olympic Committee (NOC), we need to analyze historical medal data to identify open events with a wide variety of past winners. Pinpointing these less predictable sports will allow us to advise the NOC on where to strategically invest their budget for the highest chance of winning a breakthrough medal. |
| **3** | **Startup Investments** | **Approach: Optimal Funding Trajectories for Follow-On Investment**<br>Problem Statement: A venture capital firm struggles to reliably select seed-stage startups that will eventually secure follow-on funding, resulting in a portfolio of stalled companies. The Investment Analytics team needs to analyze historical funding data across industry categories, funding round counts, time between rounds, and geographic regions to identify the patterns most strongly associated with startups that successfully raise additional capital. Uncovering these historical trajectories will allow the firm to accurately refine its $10M seed-stage investment criteria and target startups with the highest odds of advancing. |
| **4** | **Bahrain Imports** | **Approach: Direct Import Feasibility for Local Business**<br>Problem Statement: A local business currently relies on costly third-party distributors to source [Commodity/Product], inflating operational costs and limiting margins. The procurement team needs to analyze the last five years of import data (2021-2025) to identify historical volume trends, seasonal fluctuations, and the most cost-effective countries of origin. Finding these historical patterns will allow the business to build a direct-import strategy to bypass middlemen and reduce overall procurement costs. |
| **5** | **Wind Turbines** | **Approach: Renewable Energy Private Equity Investment**<br>Problem Statement: A private equity firm focused on renewable energy aims to acquire U.S. wind farms but requires deeper insight into the specific structural characteristics and geographic locations that drive peak energy efficiency. To guide these acquisitions, the Investment Committee must evaluate historical Net Generation (MWh) data across various Census Regions, segmented by turbine specifications and technical details. By spotting niche opportunities, distinguishing the physical configurations and regions with the strongest historical performance, the firm can strategically target assets that meet proven benchmarks for high energy output. |
| **6** | **Stack Overflow** | **1st Approach: Curriculum Optimization for High-Yield Tech Stacks**<br>Problem Statement: A leading coding bootcamp wants to maximize its graduates' earning potential, but the software engineering landscape is crowded with constantly shifting frameworks and tools. The curriculum development team needs to analyze the last two years of survey data (2024-2025), specifically isolating **the US** to control for global wage disparities, to identify which programming languages historically yield the highest median compensation and steepest year-over-year salary growth. Pinpointing these high-momentum tech stacks will allow the bootcamp to restructure its upcoming curriculum, aiming for a 10% increase in alumni starting salaries by teaching the exact skills most valued by the current market.<br><br>**2nd Approach: Efficient Career Pathways and Talent Sourcing**<br>Problem Statement: An enterprise tech recruiting agency struggles to determine whether traditional university degrees or non-traditional/bootcamp pathways produce more successful, rapid-growth developers. The talent acquisition team must segment historical survey data (2024-2025) for **the US** to quantify how formal education levels, years of professional experience, and pre-professional self-taught coding experience interact to drive long-term compensation trajectories. Uncovering these efficient career pathways will allow the agency to adjust its talent sourcing strategy, targeting a 15% increase in high-value placements by recruiting directly from proven, data-backed developer demographics. |

---
### Technical Report Template

Future projects will require you to decide on the entire structure of your technical report. Here, we provide you with a simple EDA template (inside the .zip file) in a Jupyter notebook that will help to guide your data exploration and analysis. **If you choose to edit the core structure of this notebook, make sure you don't exclude any of the requested operations**.

---

### Style Guide and Suggested Resources

[Project Overview Guidelines](./project-overview-guidelines.md) have been included for you in this repository. Some recommendations are geared toward future projects (which will include modeling and span multiple notebooks), but generally these are great recommendations.

In addition, the [Problem Statement](#problem-statement) section provides examples and advice for writing a problem statement and structuring your readme file. 

__Note:__ in order for your readme to automatically display in github, it must be named `README.md`. So, before submitting, make sure to delete this one and replace it with your own!

Here's a link on [how to give a good lightning talk](https://www.semrush.com/blog/16-ways-to-prepare-for-a-lightning-talk/), which provides some good recommendations for short presentations.

[Here's a great summary](https://towardsdatascience.com/storytelling-with-data-a-data-visualization-guide-for-business-professionals-97d50512b407) of the main points of the book _Storytelling with Data_, which I can't recommend enough. [Here's a blog post](http://www.storytellingwithdata.com/blog/2017/8/9/my-guiding-principles) by the author about his guiding principles for visualizations.

---

### Submission

**Materials must be submitted by the date and in the method outlined by your instructor.**

Your technical report will be hosted on your GitHub. Make sure it includes:

- A `README.md` (that isn't this file)
- Jupyter notebook(s) with your analysis (renamed to describe your project)
- Presentation slides
- Any other necessary files (images, etc.)

**Please clone to your local machine, and submit a link to your GitHub repo as per guidelines from your instructor.**

---

### Rubric
Your instructors will evaluate your project (for the most part) using the following criteria. You should make sure that you consider and/or follow most if not all of the considerations/recommendations outlined below **while** working through your project.

**Scores will be out of 21 points based on the 7 items in the rubric.** <br>
*3 points per section*<br>

| Score | Interpretation |
| :--- | :--- |
| **0** | *Project fails to meet the minimum requirements for this item.* |
| **1** | *Project meets the minimum requirements for this item, but falls significantly short of portfolio-ready expectations.* |
| **2** | *Project exceeds the minimum requirements for this item, but falls short of portfolio-ready expectations.* |
| **3** | *Project meets or exceeds portfolio-ready expectations; demonstrates a thorough understanding of every outlined consideration.* |

**Project Organization**
- Are modules imported correctly (using appropriate aliases)?
- Are data imported/saved using relative paths?
- Does the README provide a good executive summary of the project?
- Is markdown formatting used appropriately to structure notebooks?
- Are there an appropriate amount of comments to support the code?
- Are files & directories organized correctly?
- Are there unnecessary files included?
- Do files and directories have well-structured, appropriate, consistent names?

**Clarity of Message**
- Is the problem statement clearly presented?
- Does a strong narrative run through the project?
- Does the student provide appropriate context to connect individual steps back to the overall project?
- Is it clear how the final recommendations were reached?
- Are the conclusions/recommendations clearly stated?

**Python Syntax and Control Flow**
- Is care taken to write human readable code?
- Is the code syntactically correct (no runtime errors)?
- Does the code generate desired results (logically correct)?
- Does the code follows general best practices and style guidelines?
- Are Pandas functions used appropriately?
- Does the student demonstrate mastery masking in Pandas?
- Does the student demonstrate mastery sorting in Pandas?

**Data Cleaning and EDA**
- Does the student fix data entry issues?
- Are data appropriately labeled?
- Are data appropriately typed?
- Are datasets combined correctly?
- Are appropriate summary statistics provided?
- Are steps taken during data cleaning and EDA framed appropriately?

**Visualizations**
- Are the requested visualizations provided?
- Do plots accurately demonstrate valid relationships?
- Are plots labeled properly?
- Plots interpreted appropriately?
- Are plots formatted and scaled appropriately for inclusion in a notebook-based technical report?

**Research and Conceptual Understanding**
- Were useful insights gathered from outside sources?
- Are sources clearly identified?
- Does the student provide appropriate interpretation with regards to descriptive and inferential statistics?

**Presentation**
- Is the problem statement clearly presented?
- Does a strong narrative run through the presentation building toward a final conclusion?
- Are the conclusions/recommendations clearly stated?
- Is the level of technicality appropriate for the intended audience?
- Is the student substantially over or under time?
- Does the student appropriately pace their presentation?
- Does the student deliver their message with clarity and volume?
- Are appropriate visualizations generated for the intended audience?
- Are visualizations necessary and useful for supporting conclusions/explaining findings?

In order to pass the project, students must earn a minimum score of 1 for each category.
- Earning below a 1 in one or more of the above categories would result in a failing project.
- While a minimum of 1 in each category is the required threshold for graduation, students should aim to earn at least an average of 1.5 across each category. An average score below 1.5, while it may be passing, means students may want to solicit specific feedback in order to significantly improve the project before showcasing it as part of a portfolio or the job search.

### REMEMBER:

This is a learning environment and you are encouraged to try new things, even if they don't work out as well as you planned! While this rubric outlines what we look for in a _good_ project, it is up to you to go above and beyond to create a _great_ project. **Learn from your failures and you'll be prepared to succeed in the workforce**.

---

## Important note
Please ignore the `_layouts` folder and the `config.yml` file in the root of this repo. They are needed to make sure the repo renders well; please don't change them or delete them and your repo will work fine :)