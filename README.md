

# QuickDepth

**AI-Powered Prediction of Combinational Logic Depth in RTL Designs**

QuickDepth is an AI-based tool developed to predict the combinational logic depth of signals in RTL (Register Transfer Level) designs before the full synthesis step. This allows chip designers and hardware engineers to detect potential timing violations early, saving critical development time and reducing the need for expensive refactoring.

This project was created as part of the **Google Girl Hackathon 2025**, under the Electronic Design Automation (EDA) innovation track.

---

## What Problem Does It Solve?

Timing violations discovered after synthesis often cause delays and require major redesigns. There is no widely available tool that can predict logic depth issues early in the RTL design phase. QuickDepth bridges that gap by acting as a predictive engine that highlights timing-critical signals before synthesis even begins.

---

## How It Works

1. **Feature Extraction from RTL**
   - Fan-In and Fan-Out of signals
   - Signal dependencies and gate types
   - Critical path indicators

2. **Modeling**
   - Features are transformed into structured data
   - A Lasso Regression model is trained to predict combinational depth
   - The model is validated using cross-validation and tested on unseen RTL modules

3. **Prediction**
   - Given new RTL signal features, the model predicts the logic depth
   - Critical signals with high predicted depth are flagged for potential timing violations

---

## Why Lasso Regression?

After comparing several models, Lasso Regression was chosen due to its balance between accuracy, interpretability, and computational efficiency.

| Model           | Status    | Reason for Rejection                                |
|----------------|-----------|------------------------------------------------------|
| Decision Trees  |  Rejected | Overfitting on complex data                         |
| Random Forest   |  Rejected | Higher memory usage and less interpretability       |
| XGBoost         |  Rejected | Complex tuning and long training time               |
| Neural Networks |  Rejected | Required more data and time                         |
| **Lasso Regression** |  Selected | L1 regularization, simple, efficient, and accurate |

---

## Proof of Correctness

- **Dataset**: Synthetic RTL benchmark datasets were created, including fan-in, fan-out, signal dependencies, gate types, and critical path length.
- **Training & Validation**: Performed using k-fold cross-validation.
- **Evaluation Metrics**:
  - Mean Squared Error (MSE): Low
  - R² Score: High, showing strong predictive performance
- **Testing**: Applied to real RTL modules; prediction results closely matched post-synthesis timing reports.
- **Practical Use**: Identified critical signals and flagged potential violations early in the design cycle.

---

## Complexity Analysis

| Task                     | Time Complexity           | Space Complexity         |
|--------------------------|---------------------------|---------------------------|
| Feature Extraction       | O(N)                      | O(N × F)                  |
| Model Training (Lasso)   | O(N × F²)                 | O(F)                      |
| Cross-Validation         | O(K × N × F²)             | —                         |
| Prediction               | O(F)                      | —                         |

> Where:  
> N = Number of signals  
> F = Number of features  
> K = Number of folds

---

## Tech Stack

- Python
- scikit-learn
- pandas, NumPy
- Jupyter Notebook
- Matplotlib / Seaborn (for analysis)

---


## How to Run Locally

```bash
# Step 1: Clone the repository
git clone https://github.com/yourusername/QuickDepth.git
cd QuickDepth

# Step 2: Set up virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the training script
python train_model.py

# Step 5: Run the prediction script
python predict_depth.py

---

##References
ScienceDirect article on Time Delay Modeling in Digital Circuits

VLSI Physical Design with Timing Analysis (Book)

ISCAS & MCNC Benchmark RTL Circuits (b17, s38584)

Dataset features: Fan-In, Fan-Out, Gate Type, Dependency Count, Critical Path Length


