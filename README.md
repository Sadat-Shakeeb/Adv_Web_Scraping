# Smartphone Dataset Analysis

## About
This project involves data analysis on a smartphone dataset collected through **web scraping** from [Smartprix](https://www.smartprix.com/mobiles). The dataset has been processed and cleaned using **Pandas**, followed by **Exploratory Data Analysis (EDA)** to uncover insights.

## Steps Performed

### 1. Data Gathering
- Scraped smartphone data from **Smartprix** using web scraping techniques.
- Collected information such as model, price, ratings, processor, memory, battery, display, camera, and OS.

### 2. Data Cleaning
Performed a thorough assessment and cleaning of the dataset using **Pandas**:

#### **Data Assessing**
Identified **Quality Issues**:
- **Model:** Inconsistent brand names (e.g., "OPPO" written differently across entries).
- **Price:**
  - Unnecessary currency symbol **₹**.
  - Presence of commas in numerical values.
  - Incorrect pricing for certain models (e.g., **Namotel** listed at ₹99).
- **Ratings:** Missing values.
- **Processor:** Incorrect values for some **Samsung** phones at specific row numbers.
- **Memory, Battery, Display:** Incorrect values at multiple row indices.
- **Camera:**
  - Inconsistent representation of the number of cameras ("Dual", "Triple", "Quad").
  - Separation of front and rear cameras using `&`.
  - Incorrect data in multiple rows.
- **Card & OS:**
  - Some fields contain unrelated information (e.g., OS column containing Bluetooth/FM radio details).
  - OS version names are inconsistently formatted (e.g., "Lollipop").
- **Data Type Issues:**
  - Price and Rating stored as incorrect data types.

#### **Tidiness Issues**
Reformatted dataset to enhance clarity:
- **SIM:** Split into separate columns for `has_5G`, `has_NFC`, and `has_IR_Blaster`.
- **RAM:** Split into `RAM` and `ROM` columns.
- **Processor:** Extracted `Processor Name`, `Cores`, and `CPU Speed`.
- **Battery:** Separated into `Battery Capacity` and `Fast Charging Available`.
- **Display:** Split into `Size`, `Resolution Width`, `Resolution Height`, and `Frequency`.
- **Camera:** Split into `Front Camera` and `Rear Camera`.
- **Card Slot:** Separated into `Supported` and `Extended Up To`.

### 3. Exploratory Data Analysis (EDA)
Performed **surface-level analysis** using:
- **Univariate Analysis:** Distribution of numerical features.
- **Bivariate Analysis:** Relationship between price, RAM, battery capacity, and camera features.
- **Visualization Tools:**
  - **Matplotlib & Seaborn** for data visualization.
  - **Numpy & Pandas** for data manipulation.

## Dependencies
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- BeautifulSoup (for web scraping)
- Requests

## Installation
To run the project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the data analysis script:
   ```sh
   python analysis.py
   ```

## Usage
After running the scripts, users can explore:
- Cleaned and structured smartphone data.
- Summary statistics and insights from **EDA**.
- Possible future improvements, such as **predictive modeling** on smartphone prices.

