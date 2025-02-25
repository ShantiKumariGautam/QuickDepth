# QuickDepth: The Predictive Genius for RTL Logic Depth!

Welcome to QuickDepth! 🚀

Ever wondered if your combinational logic designs might cause timing issues before you hit the synthesizer? Say hello to **QuickDepth**, the smart tool that predicts the logic depth of your RTL designs. No more waiting for synthesis results or being caught off guard by timing violations. QuickDepth has got your back!

### Why QuickDepth? 🤔
Because every second counts when you're designing hardware. If your logic depth prediction is off, you could end up with timing violations that slow down the whole process. With QuickDepth, you get to predict those issues ahead of time, and that means you can optimize before you even reach synthesis. How cool is that?

### What Does QuickDepth Do? 🛠️
- **Predicts Logic Depth**: Powered by machine learning, it crunches data from your design parameters and spits out the predicted combinational logic depth. Pretty sweet, right?
- **Uses Lasso Regression**: It’s not just any random model – I picked Lasso Regression for its power to handle linear relationships without overfitting. It’s a balanced choice for this kind of task.
- **Works with Real Data**: This isn’t just a theoretical model – it’s based on actual RTL data! So when you run it, you can trust that it’s got real-world potential.
- **Timing Violation Alerts**: The best part? It can help flag timing violations early in the process, which is a lifesaver during design iteration.

### How It Works 🔍
1. **Data Collection**: First off, I gathered important design parameters like Gate Type, Fan-In, Fan-Out, and of course, Logic Depth. These are the building blocks.
2. **Feature Engineering**: To make sure the machine learning model could handle these features, I used Label Encoding for Gate Type and scaling to make the data more digestible.
3. **Training the Model**: I then trained the model using **Lasso Regression**, which did a solid job of predicting logic depth based on those features. Regularization for the win!
4. **Evaluating the Model**: After training, I used **Mean Absolute Error (MAE)** and **R-squared** to measure performance – and trust me, it performed admirably.
5. **Practical Use**: I tested QuickDepth on fresh data to ensure that it can be applied in real-life scenarios. No fluff, all results.

### Tech Stack 💻
- **Python**: The programming language I used to build the project.
- **Scikit-learn**: The superhero of machine learning! It helps train the model and evaluate performance.
- **Pandas & Numpy**: These are like my trusty sidekicks for data manipulation and processing.
- **Matplotlib**: Want to visualize things? I used it to plot graphs and figure out how our model is performing.

## Installation

Run the following commands to set up QuickDepth:  

```bash
git clone https://github.com/yourusername/QuickDepth.git  
cd QuickDepth  
pip install -r requirements.txt  


