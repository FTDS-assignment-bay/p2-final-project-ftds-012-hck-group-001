# InsureWise Cam: Intelligent Vehicle Damage Detection System for Efficient Insurance Claims

![InsureWise Cam](https://r2.easyimg.io/8zf0odixl/insurewise.png)

InsureWise Cam revolutionizes vehicle insurance by employing cutting-edge computer vision technology to detect and identify damages on customers' vehicles. Integrated with user history, it empowers InsureWise insurance company to accurately determine customers' eligibility for compensation claims. Designed to streamline the claim process to 3 days, InsureWise Cam aims for a 50% increase in customer satisfaction. Project evaluation is scheduled after 6 months. The project encompasses three pivotal processes:

## Data Pipeline:
1. **Source of Data (Kaggle):**
   - Acquire relevant datasets from Kaggle.
2. **Load Data into PostgreSQL:**
   - Upload datasets into PostgreSQL for storage and management.
3. **Save Data to CSV:**
   - Export datasets to CSV for backup and reference.
4. **Data Transformation (Cleaning, Fixing Datatype):**
   - Cleanse and standardize datasets, ensuring data consistency.
5. **Secondary Data Loading into PostgreSQL:**
   - Reload cleansed datasets back into PostgreSQL for analysis.
6. **Load Data into Elasticsearch:**
   - Index datasets into Elasticsearch for efficient search and retrieval.

## Modeling Process:
- **Computer Vision Model:**
  - Utilizes VGG16 transfer learning model with additional hidden layers.
- **Machine Learning Model:**
  - Includes K-Nearest Neighbors, Decision Tree, Random Forest, Gradient Boosting, CatBoost, and XGBoost Classifiers. The XGBoost Classifier is chosen for deployment after training.

## Integration and Analysis:
- **Huggingface for Prediction:**
  - Access the [Huggingface Prediction Link](https://huggingface.co/spaces/batraccoon/InsureWise-Cam-Prediction).
- **Tableau Public Dashboard:**
  - Explore the [Tableau Public Dashboard Link](https://public.tableau.com/app/profile/muhammad.hafidz.adityaswara/viz/shared/W5TY5R99P).

## Dataset Sources:
- **Computer Vision:**
  - [Vehicle Damage Identification Dataset](https://www.kaggle.com/datasets/gauravduttakiit/vehicle-damage-identification)
- **Machine Learning:**
  - [Analytics Olympiad 2022 Dataset](https://www.kaggle.com/datasets/gauravduttakiit/analytics-olympiad-2022)

## Team Members:
This project was undertaken to fulfill the final requirements of the Full-time Data Science bootcamp at Hacktiv8, led by:
- Angger Rizky Firdaus as Data Engineer (Establishing data pipeline with airflow and deployment with huggingface)
- Basyira Sabita as Data Scientist (Conducting computer vision and machine learning modeling to achieve optimal results)
- Muhammad Hafidz Adistyaswara as Data Analyst (Analyzing the dataset to glean insights into customer behavior using vehicle insurance and crafting dashboards in Tableau).

---