# Capstone Notebook — Fix Pack

Ready-to-paste cells addressing every gap found in the review, in the order you should apply them.
Cell numbers refer to your current `Capstone_final.ipynb`.

---

## Fix 1 — Title block (replaces cells 0–3)

**Delete cells 0, 1, 2, 3.** They are Lightning Talk 2 instructions. Also delete cell 66
("You only need to outline your approach here. No need to execute").

Paste this as your new first cell (markdown):

```markdown
# Adult Income Prediction
### Binary Classification of Individuals Earning More Than $50K per Year

**Student:** Ali Hussain Yousif
**Topic:** Income Prediction (Binary Classification)
**Cohort:** DSB PT3
**Submission date:** 1 September 2026

**Data source:** UCI Adult / Census Income dataset (1994 US Census extract),
obtained via Kaggle — https://www.kaggle.com/datasets/mosapabdelghany/adult-income-prediction-dataset
```

---

## Fix 2 — Introduction (new markdown cell, before Problem Statement)

The guideline requires an Introduction separate from the Problem Statement. You don't have one.

```markdown
## Introduction

This project uses the Adult (Census Income) dataset, an extract of the **1994 United States
Census** originally published by the UCI Machine Learning Repository. It contains 32,561
individual survey responses described by 14 demographic and employment attributes — age,
education, occupation, marital status, weekly working hours, and capital gains and losses —
together with a binary label recording whether that person's annual income exceeded $50,000.

The $50K threshold is expressed in 1994 dollars, equivalent to roughly $107,000 today. The
dataset is a long-standing benchmark for tabular binary classification, which makes results
here directly comparable to published work, but it also means all conclusions are tied to the
US labour market as it existed in 1994.

Approximately 24% of records fall in the >$50K class, making this a moderately imbalanced
classification problem — a fact that shapes every metric decision made in this notebook.
```

---

## Fix 3 — Consolidated imports (replaces cell 9; delete cells 58, 59, 61, 62, 63)

Cells 58, 59, 61, 62, 63 are abandoned experiments. Cells 64, 65 and 119–125 are empty.
Delete all of them, then replace cell 9 with:

```python
# ─── Core ──────────────────────────────────────────────────────────────────
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ─── Statistics ────────────────────────────────────────────────────────────
from scipy.stats import chi2_contingency

# ─── Preprocessing & pipeline ──────────────────────────────────────────────
from sklearn.base import clone
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# ─── Model selection ───────────────────────────────────────────────────────
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score

# ─── Models ────────────────────────────────────────────────────────────────
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# ─── Metrics ───────────────────────────────────────────────────────────────
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score,
    confusion_matrix, ConfusionMatrixDisplay, roc_curve
)

# Reproducibility: one seed used throughout the notebook
RANDOM_STATE = 42

# Display settings
pd.set_option('display.max_columns', None)
sns.set_style('whitegrid')
```

Then delete the duplicate `import` lines inside cells 56, 60, 68, 100 and 112.

---

## Fix 4 — Leakage-free missing-value handling (replaces cell 23)

Your cell 54 promises imputation fitted on training data only, but cell 23 computes the mode
from the whole dataset before the split. Two ways to fix it — **Option A is recommended.**

### Option A — treat missing as its own category (simplest, no leakage possible)

```python
# '?' is not random in this dataset — it clusters among the retired and those outside
# the labour force, so the missingness itself carries signal. Rather than overwriting
# 1,836 workclass and 1,843 occupation values with the column mode, we preserve that
# signal by encoding it as an explicit category. This also removes any leakage risk,
# because no statistic is computed from the data at all.
for col in ['workclass', 'occupation', 'native.country']:
    df[col] = df[col].fillna('Unknown')

df.isnull().sum()
```

### Option B — impute inside the pipeline (fits on training folds only)

Leave the NaNs in place (skip cell 23 entirely) and build the preprocessor like this:

```python
numeric_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler',  StandardScaler())
])

categorical_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', numeric_pipe,     numerical_features),
    ('cat', categorical_pipe, categorical_features)
])
```

Note: with Option B the NaNs remain during EDA, so your chi-square crosstabs will silently
drop those rows. Mention that in the markdown if you go this route.

---

## Fix 5 — Feature Selection section (new; goes after the chi-square cell)

This closes the biggest gap in the notebook: cell 54 promises to test `fnlwgt` and review the
`education` / `education.num` redundancy, and neither was ever done.

Markdown cell first:

```markdown
## Feature Selection

Two decisions follow from the exploratory analysis:

1. **`fnlwgt`** is the census *sampling weight* — it records how many people in the wider
   population each row represents, not an attribute of the individual. It is conceptually
   invalid as a predictor and correlates -0.010 with the target.
2. **`education` and `education.num`** encode the same variable. `education.num` is simply the
   ordinal encoding of `education`, so including both adds 16 redundant one-hot columns
   without adding information.

Rather than assume, both are tested empirically below using 5-fold cross-validated F1 on the
training set only.
```

Then the code:

```python
def build_pipeline(model, num_cols, cat_cols):
    """Assemble a preprocessing + model pipeline for a given feature subset."""
    pre = ColumnTransformer([
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
    ])
    return Pipeline([('preprocessor', pre), ('model', model)])


full_num = ['age', 'fnlwgt', 'education.num',
            'capital.gain', 'capital.loss', 'hours.per.week']
full_cat = ['workclass', 'education', 'marital.status', 'occupation',
            'relationship', 'race', 'sex', 'native.country']

# Candidate reductions
no_fnlwgt    = [c for c in full_num if c != 'fnlwgt']
no_education = [c for c in full_cat if c != 'education']

experiments = {
    'All features':                  (full_num,   full_cat),
    'Without fnlwgt':                (no_fnlwgt,  full_cat),
    'Without education (keep .num)': (full_num,   no_education),
    'Without both':                  (no_fnlwgt,  no_education),
}

# Cross-validate on the TRAINING set only — the test set stays untouched
rows = []
for name, (nc, cc) in experiments.items():
    pipe = build_pipeline(
        XGBClassifier(random_state=RANDOM_STATE, eval_metric='logloss'), nc, cc
    )
    cv_f1 = cross_val_score(pipe, X_train, y_train,
                            cv=5, scoring='f1', n_jobs=-1).mean()
    rows.append({'Feature set': name,
                 'Columns used': len(nc) + len(cc),
                 'CV F1': round(cv_f1, 4)})

pd.DataFrame(rows).sort_values('CV F1', ascending=False)
```

Then adopt whichever set wins and use it for the rest of the notebook:

```python
# Adopt the reduced feature set for all subsequent modelling
numerical_features   = no_fnlwgt
categorical_features = no_education

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])
```

Write one markdown sentence recording what you found — even "performance was unchanged, so
the simpler model was preferred" is a legitimate, markable result.

---

## Fix 6 — Majority-class baseline (new cell, before the model comparison)

Cell 67 promises this and never delivers it. Without it, 0.72 F1 has nothing to be measured against.

```python
# A model that always predicts the majority class. This is the reference point:
# any real model must beat it to be worth deploying.
dummy = DummyClassifier(strategy='most_frequent')
dummy.fit(X_train, y_train)

dummy_pred = dummy.predict(X_test)
dummy_prob = dummy.predict_proba(X_test)[:, 1]

print("Accuracy :", accuracy_score(y_test, dummy_pred))
print("Recall   :", recall_score(y_test, dummy_pred, zero_division=0))
print("F1-score :", f1_score(y_test, dummy_pred, zero_division=0))
print("ROC-AUC  :", roc_auc_score(y_test, dummy_prob))
```

Expected: ~75.9% accuracy, 0.0 F1, 0.5 ROC-AUC — the exact illustration of why accuracy is
the wrong metric here.

---

## Fix 7 — Threshold selection without leakage (replaces cells 99–104)

**This is the most important technical fix.** Your current code searches thresholds against
`y_test` and then reports the best score on that same `y_test`, which makes F1 = 0.7227
optimistically biased. Your tuned XGBoost already reaches 0.7016 on test at the default
threshold, so this correction costs you nothing.

```python
# ── Select the threshold on data the model has never been scored against ──────
# Carve a validation split OUT OF THE TRAINING SET. The test set stays sealed.
X_tr, X_val, y_tr, y_val = train_test_split(
    X_train, y_train,
    test_size=0.2,
    random_state=RANDOM_STATE,
    stratify=y_train
)

# Same tuned hyperparameters, refitted on the reduced training portion
threshold_model = clone(best_xgb)
threshold_model.fit(X_tr, y_tr)
val_prob = threshold_model.predict_proba(X_val)[:, 1]

# Sweep thresholds against the VALIDATION set
candidate_thresholds = np.arange(0.10, 0.90, 0.01)
val_f1_scores = [
    f1_score(y_val, (val_prob >= t).astype(int), zero_division=0)
    for t in candidate_thresholds
]

chosen_threshold = candidate_thresholds[int(np.argmax(val_f1_scores))]
print(f"Threshold chosen on validation set: {chosen_threshold:.2f}")
print(f"Validation F1 at that threshold   : {max(val_f1_scores):.4f}")
```

```python
# Visualise the sweep
plt.figure(figsize=(8, 5))
plt.plot(candidate_thresholds, val_f1_scores)
plt.axvline(chosen_threshold, linestyle='--', color='grey',
            label=f'Chosen: {chosen_threshold:.2f}')
plt.axvline(0.50, linestyle=':', color='lightgrey', label='Default: 0.50')
plt.xlabel("Classification threshold")
plt.ylabel("F1-score (validation set)")
plt.title("Threshold selection on held-out validation data")
plt.legend()
plt.show()
```

```python
# Apply the chosen threshold ONCE to the untouched test set — this is the honest estimate
xgb_prob   = best_xgb.predict_proba(X_test)[:, 1]
final_pred = (xgb_prob >= chosen_threshold).astype(int)

print("Accuracy :", accuracy_score(y_test, final_pred))
print("Precision:", precision_score(y_test, final_pred, zero_division=0))
print("Recall   :", recall_score(y_test, final_pred, zero_division=0))
print("F1-score :", f1_score(y_test, final_pred, zero_division=0))
print("ROC-AUC  :", roc_auc_score(y_test, xgb_prob))
```

Update your existing confusion-matrix and Final Model Summary cells to use `final_pred`
instead of `final_xgb_pred`, and quote whatever numbers this produces — they will be close
to, but probably slightly below, 0.723. **Report the new figures, not the old ones.**

Also rename the shadowed variable in cell 109:

```python
fpr, tpr, roc_thresholds = roc_curve(y_test, xgb_prob)   # was: thresholds
```

---

## Fix 8 — Model comparison table (new; the guideline requires this explicitly)

```python
def evaluate(name, y_true, y_pred, y_prob, cv_f1=np.nan):
    """Collect all five metrics for one model into a single row."""
    return {
        'Model':     name,
        'Accuracy':  accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred, zero_division=0),
        'Recall':    recall_score(y_true, y_pred, zero_division=0),
        'F1-score':  f1_score(y_true, y_pred, zero_division=0),
        'ROC-AUC':   roc_auc_score(y_true, y_prob),
        'CV F1':     cv_f1,
    }


comparison_df = pd.DataFrame([
    evaluate('Majority-class baseline',     y_test, dummy_pred, dummy_prob),
    evaluate('Logistic Regression (tuned)', y_test, lr_pred,  lr_prob,  lr_grid.best_score_),
    evaluate('Decision Tree (tuned)',       y_test, dt_pred,  dt_prob,  dt_grid.best_score_),
    evaluate('Random Forest (tuned)',       y_test, rf_pred,  rf_prob,  rf_grid.best_score_),
    evaluate('XGBoost (tuned)',             y_test, xgb_pred, xgb_prob, xgb_grid.best_score_),
    evaluate(f'XGBoost @ threshold {chosen_threshold:.2f}',
                                            y_test, final_pred, xgb_prob),
]).round(4)

comparison_df
```

The `CV F1` column is your evidence against overfitting — cross-validated scores track test
scores within about a point for every model. Say so in the markdown underneath.

---

## Fix 9 — Feature importance aggregated to the parent feature

One-hot encoding splits a single feature's importance across all its levels, so the raw chart
understates `education` and `occupation`. Add this after your existing chart:

```python
importance_df = pd.DataFrame({
    'encoded':    best_xgb.named_steps['preprocessor'].get_feature_names_out(),
    'importance': best_xgb.named_steps['model'].feature_importances_
})

# Map each one-hot column back to the original feature it came from.
# Longest names are checked first so 'education.num' is not swallowed by 'education'.
source_columns = sorted(numerical_features + categorical_features, key=len, reverse=True)

def parent_feature(encoded_name):
    name = encoded_name.split('__', 1)[1]          # strip the 'num__' / 'cat__' prefix
    for col in source_columns:
        if name == col or name.startswith(col + '_'):
            return col
    return name

importance_df['feature'] = importance_df['encoded'].apply(parent_feature)

aggregated_importance = (
    importance_df
    .groupby('feature')['importance'].sum()
    .sort_values(ascending=False)
    .reset_index()
)

plt.figure(figsize=(10, 6))
sns.barplot(data=aggregated_importance.head(10), x='importance', y='feature')
plt.title("Feature importance aggregated to the original feature")
plt.xlabel("Total gain")
plt.ylabel("")
plt.show()

aggregated_importance
```

---

## Fix 10 — Cramér's V for the chi-square section

Ranking raw chi-square statistics across features is not valid as an effect-size comparison,
because chi-square scales with the number of categories. Add this beneath your existing test:

```python
def cramers_v(x, y):
    """Effect size for the association between two categorical variables.
    Unlike raw chi-square, this is comparable across features with different
    numbers of categories. Ranges from 0 (no association) to 1 (perfect)."""
    table = pd.crosstab(x, y)
    chi2  = chi2_contingency(table)[0]
    n     = table.values.sum()
    r, k  = table.shape
    return np.sqrt((chi2 / n) / (min(r, k) - 1))


effect_sizes = pd.DataFrame([
    {'Feature': col, "Cramér's V": round(cramers_v(df[col], df['income']), 4)}
    for col in categorical_cols
]).sort_values("Cramér's V", ascending=False)

effect_sizes
```

Then update the markdown to say: significance tells you the association is real; Cramér's V
tells you how strong it is, and only the second is comparable across features.

---

## Fix 11 — Restructured ending (replaces cells 116–118)

Your ending is currently "Final Model Summary → Challenges → Next Steps", which is Lightning
Talk 2 structure. The guideline wants **Conclusion → Model Comparison → Best Model →
Discussion**. Rework it into these four markdown cells:

```markdown
# Conclusion

## Best Model and Justification

XGBoost, after hyperparameter tuning and threshold optimisation, is the selected model.

It leads on both target metrics — F1 on the >$50K class and ROC-AUC — and is the only model
to clear both success criteria set at the outset (F1 ≥ 0.70, ROC-AUC ≥ 0.85). Its
cross-validated F1 sits within roughly one point of its test F1, indicating the result
generalises rather than reflecting one favourable split.

Logistic Regression achieves higher recall but at substantially lower precision, meaning a
large share of the individuals it flags as high earners are not. Random Forest is the closest
competitor but trails on both F1 and ROC-AUC. The Decision Tree is the weakest of the four.

The trade-off worth naming: XGBoost costs interpretability. Logistic Regression yields one
coefficient per feature; XGBoost yields an ensemble of 300 trees and a gain score. Where an
organisation must justify individual decisions, that difference may outweigh the performance gap.
```

```markdown
## Business Implications

- **Education is the actionable lever.** `education.num` is the strongest numeric predictor and
  one of the few factors an individual or a programme can genuinely change. Marital status
  predicts well but cannot be the target of an intervention.
- **The model should rank, not decide.** At 0.92 ROC-AUC it separates the classes reliably
  enough to prioritise outreach across a large population, but ranking is not a decision.
  It should route human attention, never allocate outcomes on its own.
- **The threshold is a policy choice, not a modelling one.** Lowering it trades precision for
  reach. Where the cost of missing someone exceeds the cost of contacting them unnecessarily,
  the lower threshold is correct.
- **Occupation clusters justify sector targeting.** Exec-managerial and Prof-specialty roles
  show the highest proportion of >$50K earners, giving programmes concrete pathways to build toward.
```

```markdown
## Limitations

1. **The data is thirty years old.** This is a 1994 US Census extract. Occupation categories,
   wage levels and the $50K threshold are all fixed to that year and do not transfer to the
   present day or to other labour markets.
2. **Protected attributes are used as predictors.** `race`, `sex` and `native.country` all
   enter the model. `sex` alone produces a chi-square statistic of 1,517. Any deployment that
   allocated support on the basis of these predictions would require a formal fairness audit
   before use, and this analysis does not provide one.
3. **`fnlwgt` is a survey artefact.** It is a census sampling weight rather than a personal
   attribute, and was excluded on those grounds.
4. **Missingness was simplified.** The `?` placeholder is likely informative rather than
   random, and treating it as a single category is an approximation.
5. **The predictive framing is imperfect.** The stated goal is targeted career support, but the
   model optimises for identifying people who *already* earn well. Its most defensible use is
   factor identification rather than individual targeting.
```

```markdown
## Future Improvements

1. **Fairness analysis** — measure equalised odds and demographic parity across `race` and
   `sex`, then retrain without protected attributes to quantify the performance cost of
   removing them.
2. **Feature engineering** — construct interaction terms such as education × occupation, and
   binned hours-per-week bands, neither of which the current linear features capture.
3. **Alternative gradient-boosting libraries** — LightGBM and CatBoost handle categorical
   features natively without one-hot expansion, which would shrink the feature matrix
   substantially.
4. **Bayesian hyperparameter optimisation** — would cover a wider search space than grid
   search at lower computational cost.
5. **Validation on recent data** — apply the same pipeline to a current census release to test
   whether the relationships identified here still hold.
```

---

## Fix 12 — References & Appendix (new final section; currently missing entirely)

```markdown
# References & Appendix

## Data Source
- Becker, B. and Kohavi, R. (1996). *Adult*. UCI Machine Learning Repository.
  https://doi.org/10.24432/C5XW20
- Dataset accessed via Kaggle:
  https://www.kaggle.com/datasets/mosapabdelghany/adult-income-prediction-dataset
- Format: CSV, 32,561 rows × 15 columns. Original source: 1994 US Census database.

## Libraries and Tools
| Library | Purpose |
| --- | --- |
| pandas | Data loading, cleaning and tabular manipulation |
| NumPy | Numerical operations and array handling |
| Matplotlib / seaborn | Visualisation |
| SciPy | Chi-square tests of independence |
| scikit-learn | Pipelines, preprocessing, Logistic Regression, Decision Tree, Random Forest, grid search, metrics |
| XGBoost | Gradient-boosted tree classifier |
| joblib | Model serialisation |

## Appendix
- `adult_income_xgb_model.pkl` — the fitted pipeline and its chosen classification threshold,
  saved together so predictions can be reproduced exactly.
- Random seed fixed at 42 for the train/test split, all model initialisations and the
  validation split, making the notebook fully reproducible end to end.
```

Add a version-capture cell so a reviewer can reproduce your environment:

```python
import sklearn, xgboost, scipy, sys
print("Python      :", sys.version.split()[0])
print("pandas      :", pd.__version__)
print("NumPy       :", np.__version__)
print("SciPy       :", scipy.__version__)
print("scikit-learn:", sklearn.__version__)
print("XGBoost     :", xgboost.__version__)
```

---

## Fix 13 — Comment the code cells

The guideline explicitly requires well-commented code, and roughly 90% of your code cells have
no comments at all. You don't need a comment on every line — one or two per cell explaining
*why*, not *what*. Examples:

```python
# Stratified split preserves the 76/24 class balance in both train and test,
# so the test set reflects the real-world distribution.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)
```

```python
# 'balanced' reweights the loss inversely to class frequency, which stops the
# model from optimising accuracy by ignoring the minority class entirely.
models = {
    "Logistic Regression": LogisticRegression(class_weight='balanced',
                                              max_iter=1000, random_state=RANDOM_STATE),
    ...
}
```

```python
# scoring='f1' targets the minority (>50K) class specifically. Tuning on accuracy
# here would push every model toward the majority-class prediction.
lr_grid = GridSearchCV(lr_pipe, lr_params, cv=5, scoring='f1', n_jobs=-1)
```

---

## Final checklist before submitting

- [ ] Title block names you, the topic and cohort DSB PT3
- [ ] Lightning Talk 2 cells (0–3, 66) deleted
- [ ] Empty and abandoned cells (58, 59, 61–65, 119–125) deleted
- [ ] Introduction section added
- [ ] Feature Selection section with the fnlwgt / education experiment
- [ ] Majority-class baseline built and reported
- [ ] Threshold selected on a validation split, not the test set
- [ ] All quoted metrics updated to match the corrected threshold
- [ ] Model comparison table present, including the CV F1 column
- [ ] Conclusion restructured: Best Model → Implications → Limitations → Future Work
- [ ] References & Appendix section added
- [ ] Every code cell carries at least one explanatory comment
- [ ] **Kernel → Restart & Run All** completes without error, top to bottom
- [ ] Notebook figures and slide figures agree with each other
